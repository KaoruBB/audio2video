{
  description = "A minimal template for Python projects using uv2nix";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      uv2nix,
      pyproject-nix,
      pyproject-build-systems,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        lib = nixpkgs.lib;

        # Load the uv workspace from the current directory
        workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };

        # Create the base overlay from uv.lock
        overlay = workspace.mkPyprojectOverlay {
          # Prefer wheels, but be prepared for overrides
          sourcePreference = "wheel";
        };

        # Overrides based on nixpkgs scipy derivation
        pyprojectOverrides = final: prev: { };

        python = pkgs.python311;

        # Construct the final Python package set
        pythonSet =
          (pkgs.callPackage pyproject-nix.build.packages {
            inherit python;
          }).overrideScope
            (
              lib.composeManyExtensions [
                pyproject-build-systems.overlays.default # Provides common build systems
                overlay # Adds packages from uv.lock
                pyprojectOverrides # Adds manual fixes (should now find pythran in final)
              ]
            );

      in
      {
        # Default package (a virtual environment with runtime dependencies)
        # Build with: nix build .#
        packages.default = pythonSet.mkVirtualEnv "uv2nix-template-env" workspace.deps.default;

        # Apps (runnable scripts) - Commented out as no scripts defined in pyproject.toml yet
        # apps.${system} = {
        #   default = {
        #     type = "app";
        #     # Assuming a script named 'my-script' defined in [project.scripts]
        #     program = "${self.packages.${system}.default}/bin/my-script";
        #   };
        # };

        # Development Shells
        # Enter with: nix develop .# (for uv2nix shell) or nix develop .#impure
        devShells = rec {
          # Impure shell: Uses system uv to manage venv manually
          impure = pkgs.mkShell {
            packages = [
              python
              pkgs.uv
            ];
            env =
              {
                UV_PYTHON_DOWNLOADS = "never";
                UV_PYTHON = python.interpreter;
              }
              // lib.optionalAttrs pkgs.stdenv.isLinux {
                LD_LIBRARY_PATH = lib.makeLibraryPath pkgs.pythonManylinuxPackages.manylinux1;
              };
            shellHook = ''
              unset PYTHONPATH
              echo "Impure shell: Run 'uv venv' and 'uv sync' manually."
            '';
          };

          # Pure uv2nix shell: Nix manages the venv with editable installs
          uv2nix =
            let
              # Create an overlay enabling editable mode for all local dependencies.
              editableOverlay = workspace.mkEditablePyprojectOverlay {
                # Use environment variable
                root = "$REPO_ROOT";
                # Optional: Only enable editable for these packages
                # members = [ "hello-world" ];
              };

              # Override previous set with our overrideable overlay.
              editablePythonSet = pythonSet.overrideScope (
                lib.composeManyExtensions [
                  editableOverlay

                  # Apply fixups for building an editable package of your workspace packages
                  (final: prev: {
                    uv2nix-template = prev.uv2nix-template.overrideAttrs (old: {
                      nativeBuildInputs =
                        (old.nativeBuildInputs or [ ]) # Ensure list exists even if null
                        ++ final.resolveBuildSystem {
                          editables = [ ];
                        };
                    });

                  })
                ]
              );

              # Build the development virtual environment with *all* dependencies (including dev)
              virtualenv = editablePythonSet.mkVirtualEnv "uv2nix-template-dev-env" workspace.deps.all;

            in
            pkgs.mkShell {
              packages = [
                virtualenv
                pkgs.uv
              ];

              env = {
                UV_NO_SYNC = "1"; # Don't let uv sync automatically
                UV_PYTHON = "${virtualenv}/bin/python"; # Force uv to use Python interpreter from venv
                UV_PYTHON_DOWNLOADS = "never"; # Prevent uv from downloading managed Python's
              };

              shellHook = ''
                unset PYTHONPATH # Avoid interference from system Python path
                export REPO_ROOT=$(git rev-parse --show-toplevel)
              '';
            };
          default = uv2nix;
        };
      }
    );
}

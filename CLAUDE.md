# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `audio2video` - a Python CLI tool that converts audio files (WAV, MP3, FLAC, AAC) combined with static images into MP4 videos. The tool is designed for content creators who want to upload audio content to YouTube and other video platforms.

## Installation Options

### For End Users
```bash
# Install from PyPI
pip install audio2video

# Or run without installation using uvx
uvx audio2video -a audio.wav -i image.png -o output.mp4
```

### For Development
```bash
# Using uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

## Development Commands

### Running the Application
```bash
# Run directly from source with uv
uv run audio2video -a test.wav -i test.png -o test.mp4

# After installation
audio2video -a audio.wav -i image.png -o output.mp4

# Run without installation using uvx (requires PyPI publication)
uvx audio2video -a audio.wav -i image.png -o output.mp4
```

### Testing
```bash
# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=audio2video
```

### Development Environment
```bash
# Enter Nix development shell (pure uv2nix)
nix develop

# Or impure shell with system uv
nix develop .#impure
```

### Building and Publishing
```bash
# Build package
uv build

# Publish to PyPI (requires authentication)
uv publish
```

## Architecture

### Core Implementation
- **src/audio2video/cli.py**: Contains the core `wav_to_mp4()` function and CLI interface
- **src/audio2video/__init__.py**: Package initialization and version management
- **src/audio2video/__main__.py**: Allows running as `python -m audio2video`
- **Dependencies**: Built on MoviePy for video processing, with FFmpeg handling the underlying encoding
- **Output**: Generates MP4 videos optimized for web platforms

### Key Features
- Multiple audio format support (WAV, MP3, FLAC, AAC)
- Multiple image format support (PNG, JPG, JPEG, BMP, GIF)
- Configurable video quality (CRF values)
- Custom resolution support
- Configurable frames per second (FPS)
- Verbose output option for debugging

### Command Line Interface
- Simple CLI with required arguments: audio file, image file, output file
- Optional arguments: CRF quality, resolution, FPS, verbose mode
- All configuration is handled through command-line arguments
- No configuration file support (simplified design)

## Important Notes

- The project uses uv for dependency management and packaging
- Nix flake configuration supports both pure and impure development environments
- Test suite includes integration tests using real media files
- PyPI-ready package with proper entry points for `uvx` usage
- CRF video quality option is properly implemented with FFmpeg parameters
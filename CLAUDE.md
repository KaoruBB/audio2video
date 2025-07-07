# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `audio2video` - a Python CLI tool that converts audio files (WAV, MP3, FLAC, AAC) combined with static images into MP4 videos. The tool is designed for content creators who want to upload audio content to YouTube and other video platforms.

## Development Commands

### Environment Setup
```bash
# Using uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

### Running the Application
```bash
# Run directly from source with uv
uv run audio2video -a test.wav -i test.png -o test.mp4

# Or after installation
audio2video -a audio.wav -i image.png -o output.mp4
```

### Testing
```bash
# Run tests (if present)
pytest tests/
```

### Development Environment
```bash
# Enter Nix development shell (pure uv2nix)
nix develop

# Or impure shell with system uv
nix develop .#impure
```

## Architecture

### Core Implementation
- **main.py**: Contains the core `wav_to_mp4()` function that uses MoviePy to combine audio and image files
- **Dependencies**: Built on MoviePy for video processing, with FFmpeg handling the underlying encoding
- **Output**: Generates MP4 videos optimized for web platforms

### Key Features
- Multiple audio format support (WAV, MP3, FLAC, AAC)
- Multiple image format support (PNG, JPG, JPEG, BMP, GIF)
- Configurable video quality (CRF values)
- Custom resolution support
- Audio fade effects
- Platform-specific presets (YouTube, Instagram)

### Configuration
- Supports `audio2video.toml` configuration file with default settings
- Platform-specific presets available for YouTube and Instagram
- Command-line arguments override configuration file settings

## Important Notes

- The project uses uv for dependency management and packaging
- Nix flake configuration supports both pure and impure development environments
- No test suite is currently implemented
- The main implementation is currently minimal and may need CLI argument parsing to match the documented interface
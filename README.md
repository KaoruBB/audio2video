# audio2video

[![PyPI version](https://badge.fury.io/py/audio2video.svg)](https://badge.fury.io/py/audio2video)
[![Python Support](https://img.shields.io/pypi/pyversions/audio2video.svg)](https://pypi.org/project/audio2video/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Convert audio files with static images to video format for YouTube and social media**

Transform your podcasts, NotebookLM audio, or any audio content into engaging videos by combining them with custom thumbnails. Perfect for content creators who want to upload audio content to YouTube or other video platforms.

## ✨ Features

- 🎵 **Multiple audio formats**: WAV, MP3, FLAC, AAC
- 🖼️ **Multiple image formats**: PNG, JPG, JPEG, BMP, GIF
- 📹 **High-quality output**: Optimized MP4 videos for web platforms
- ⚡ **Fast processing**: Efficient conversion using MoviePy
- 🛠️ **Simple CLI**: Easy-to-use command-line interface
- 📱 **Platform ready**: YouTube, TikTok, Instagram compatible output

## 🚀 Quick Start

### Installation

```bash
pip install audio2video
```

### Basic Usage

```bash
# Convert audio + image to video
audio2video -a podcast.wav -i thumbnail.png -o output.mp4

# Using short flags
audio2video -a audio.mp3 -i image.jpg -o video.mp4

# Enable verbose output
audio2video -a audio.wav -i image.png -o output.mp4 --verbose
```

### Advanced Options

```bash
# Specify output quality (18=high, 23=medium, 28=web)
audio2video -a audio.wav -i image.png -o output.mp4 --crf 18

# Set custom resolution
audio2video -a audio.wav -i image.png -o output.mp4 --resolution 1920x1080

# Set frames per second
audio2video -a audio.wav -i image.png -o output.mp4 --fps 30
```

## 📖 Use Cases

### 🎙️ Podcast to YouTube
Transform your podcast episodes into YouTube-ready videos with custom artwork.

### 🤖 NotebookLM Content
Convert AI-generated podcast content from NotebookLM into shareable video format.

### 📚 Educational Content
Create video lectures from audio recordings with presentation slides or graphics.

### 🎵 Music Releases
Combine music tracks with album artwork for music platform uploads.

## 💡 Examples
### Batch Processing
```bash
# Process multiple files
for audio in *.wav; do
    audio2video -a "$audio" -i default_thumbnail.png -o "videos/${audio%.wav}.mp4"
done
```

## 🛠️ Development

### Prerequisites
- Python 3.9+
- FFmpeg (automatically handled by MoviePy)

### Local Installation
```bash
# Clone repository
git clone https://github.com/KaoruBB/audio2video.git
cd audio2video

# Install with uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

### Running Tests
```bash
pytest tests/
```

### Development with uv
```bash
# Run directly from source
uv run audio2video -a test.wav -i test.png -o test.mp4

# Install dependencies
uv pip install -r requirements.txt
```

## 📋 Command Line Options

```
usage: audio2video [-h] -a AUDIO -i IMAGE -o OUTPUT [--crf CRF] 
                   [--resolution RESOLUTION] [--fps FPS] [--verbose]

Convert audio files with static images to video format

required arguments:
  -a, --audio AUDIO     Input audio file (WAV, MP3, FLAC, AAC)
  -i, --image IMAGE     Input image file (PNG, JPG, JPEG, BMP, GIF)
  -o, --output OUTPUT   Output video file (MP4)

optional arguments:
  -h, --help            Show this help message and exit
  --crf CRF             Video quality (18=high, 23=medium, 28=web) [default: 23]
  --resolution RESOLUTION
                        Output resolution (e.g., 1920x1080) [default: 1920x1080]
  --fps FPS             Frames per second [default: 1]
  --verbose             Enable verbose output
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

### Ways to Contribute
- 🐛 Report bugs
- ✨ Request features
- 🔧 Submit pull requests
- 📝 Improve documentation
- 🧪 Add tests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [MoviePy](https://zulko.github.io/moviepy/) for video processing
- Inspired by the need to convert NotebookLM podcasts to YouTube videos
- Thanks to the open-source community for the amazing tools

## 🔗 Related Projects

- [moviepy](https://github.com/Zulko/moviepy) - Video editing library
- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) - FFmpeg wrapper
- [youtube-upload](https://github.com/tokland/youtube-upload) - YouTube upload automation

## 📞 Support

- 📖 [Documentation](https://github.com/KaoruBB/audio2video/wiki)
- 🐛 [Issue Tracker](https://github.com/KaoruBB/audio2video/issues)
- 💬 [Discussions](https://github.com/KaoruBB/audio2video/discussions)

---

⭐ **Star this repo if you find it useful!**

Made with ❤️ for content creators who want to bring their audio to the visual world.

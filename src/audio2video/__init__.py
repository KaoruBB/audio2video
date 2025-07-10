"""
audio2video - Convert audio files with static images to video format.

This package provides a simple CLI tool for converting audio files (WAV, MP3, FLAC, AAC)
combined with static images into MP4 videos, perfect for YouTube and social media uploads.
"""

__version__ = "0.1.1"

from .cli import wav_to_mp4

__all__ = ["wav_to_mp4"]
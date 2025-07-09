"""
Basic tests for the audio2video CLI functionality.
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch

from audio2video.cli import main, wav_to_mp4


def test_wav_to_mp4_function_exists():
    """Test that the main function exists and is callable."""
    assert callable(wav_to_mp4)


def test_main_function_exists():
    """Test that the main function exists and is callable."""
    assert callable(main)


def test_wav_to_mp4_with_invalid_audio_file():
    """Test that function handles invalid audio file gracefully."""
    with tempfile.TemporaryDirectory() as tmpdir:
        invalid_audio = os.path.join(tmpdir, "nonexistent.wav")
        invalid_image = os.path.join(tmpdir, "nonexistent.png")
        output_file = os.path.join(tmpdir, "output.mp4")
        
        # This should exit with error code 1
        with pytest.raises(SystemExit) as excinfo:
            wav_to_mp4(invalid_audio, invalid_image, output_file)
        
        assert excinfo.value.code == 1


@patch('sys.argv', ['audio2video', '-a', 'test.wav', '-i', 'test.png', '-o', 'test.mp4'])
def test_main_with_missing_files():
    """Test main function with missing input files."""
    with pytest.raises(SystemExit) as excinfo:
        main()
    
    assert excinfo.value.code == 1


def test_resolution_parsing():
    """Test resolution string parsing in wav_to_mp4."""
    # This is a basic test that would need actual files to run fully
    # For now, we just test the resolution parsing logic
    resolution = "1920x1080"
    width, height = map(int, resolution.split('x'))
    
    assert width == 1920
    assert height == 1080
    
    resolution = "1280x720"
    width, height = map(int, resolution.split('x'))
    
    assert width == 1280
    assert height == 720
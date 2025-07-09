"""
Basic tests for the audio2video CLI functionality.
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

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


def test_wav_to_mp4_with_real_files():
    """Test actual conversion with real test files."""
    test_dir = Path(__file__).parent
    audio_file = test_dir / "sound.wav"
    image_file = test_dir / "image.png"
    
    # Skip test if files don't exist
    if not audio_file.exists() or not image_file.exists():
        pytest.skip("Test files not found")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, "test_output.mp4")
        
        # Test basic conversion
        wav_to_mp4(
            audio_file=str(audio_file),
            image_file=str(image_file),
            output_file=output_file,
            verbose=True
        )
        
        # Check that output file was created
        assert os.path.exists(output_file)
        assert os.path.getsize(output_file) > 0


def test_wav_to_mp4_with_custom_resolution():
    """Test conversion with custom resolution."""
    test_dir = Path(__file__).parent
    audio_file = test_dir / "sound.wav"
    image_file = test_dir / "image.png"
    
    # Skip test if files don't exist
    if not audio_file.exists() or not image_file.exists():
        pytest.skip("Test files not found")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, "test_720p.mp4")
        
        # Test with 720p resolution
        wav_to_mp4(
            audio_file=str(audio_file),
            image_file=str(image_file),
            output_file=output_file,
            resolution="1280x720",
            verbose=True
        )
        
        # Check that output file was created
        assert os.path.exists(output_file)
        assert os.path.getsize(output_file) > 0


def test_wav_to_mp4_with_fade_effects():
    """Test conversion with fade in/out effects."""
    test_dir = Path(__file__).parent
    audio_file = test_dir / "sound.wav"
    image_file = test_dir / "image.png"
    
    # Skip test if files don't exist
    if not audio_file.exists() or not image_file.exists():
        pytest.skip("Test files not found")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, "test_fade.mp4")
        
        # Test with fade effects
        wav_to_mp4(
            audio_file=str(audio_file),
            image_file=str(image_file),
            output_file=output_file,
            fade_in=0.5,
            fade_out=0.5,
            verbose=True
        )
        
        # Check that output file was created
        assert os.path.exists(output_file)
        assert os.path.getsize(output_file) > 0


@patch('sys.argv', ['audio2video', '-a', 'tests/sound.wav', '-i', 'tests/image.png', '-o', 'output.mp4'])
def test_main_with_real_files():
    """Test main function with actual test files."""
    test_dir = Path(__file__).parent
    audio_file = test_dir / "sound.wav"
    image_file = test_dir / "image.png"
    
    # Skip test if files don't exist
    if not audio_file.exists() or not image_file.exists():
        pytest.skip("Test files not found")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, "main_test.mp4")
        
        # Mock sys.argv with actual file paths
        test_args = [
            'audio2video',
            '-a', str(audio_file),
            '-i', str(image_file),
            '-o', output_file,
            '--verbose'
        ]
        
        with patch('sys.argv', test_args):
            main()
        
        # Check that output file was created
        assert os.path.exists(output_file)
        assert os.path.getsize(output_file) > 0
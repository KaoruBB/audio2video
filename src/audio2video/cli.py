import argparse
import sys
from pathlib import Path
from moviepy import AudioFileClip, ImageClip

def wav_to_mp4(audio_file, image_file, output_file, crf=23, resolution="1920x1080", fps=1, verbose=False):
    """Convert audio file with static image to video format."""
    try:
        if verbose:
            print(f"Loading audio: {audio_file}")
        audio = AudioFileClip(audio_file)
        
        if verbose:
            print(f"Loading image: {image_file}")
        image = ImageClip(image_file)
        
        # Parse resolution
        width, height = map(int, resolution.split('x'))
        image = image.resized((width, height))
        
        if verbose:
            print(f"Creating video with resolution: {resolution}, fps: {fps}")
        video = image.with_duration(audio.duration).with_audio(audio)
        video = video.with_fps(fps)
        
        if verbose:
            print(f"Writing video: {output_file}")
        video.write_videofile(
            output_file,
            codec='libx264',
            audio_codec='aac'
        )
        
        if verbose:
            print("Video creation completed successfully!")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Convert audio files with static images to video format"
    )
    
    # Required arguments
    parser.add_argument(
        "-a", "--audio", 
        required=True, 
        help="Input audio file (WAV, MP3, FLAC, AAC)"
    )
    parser.add_argument(
        "-i", "--image", 
        required=True, 
        help="Input image file (PNG, JPG, JPEG, BMP, GIF)"
    )
    parser.add_argument(
        "-o", "--output", 
        required=True, 
        help="Output video file (MP4)"
    )
    
    # Optional arguments
    parser.add_argument(
        "--crf", 
        type=int, 
        default=23, 
        help="Video quality (18=high, 23=medium, 28=web) [default: 23]"
    )
    parser.add_argument(
        "--resolution", 
        default="1920x1080", 
        help="Output resolution (e.g., 1920x1080) [default: 1920x1080]"
    )
    parser.add_argument(
        "--fps", 
        type=int, 
        default=1, 
        help="Frames per second [default: 1]"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Validate input files exist
    audio_path = Path(args.audio)
    image_path = Path(args.image)
    
    if not audio_path.exists():
        print(f"Error: Audio file not found: {args.audio}", file=sys.stderr)
        sys.exit(1)
    
    if not image_path.exists():
        print(f"Error: Image file not found: {args.image}", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert audio to video
    wav_to_mp4(
        audio_file=str(audio_path),
        image_file=str(image_path),
        output_file=str(output_path),
        crf=args.crf,
        resolution=args.resolution,
        fps=args.fps,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()

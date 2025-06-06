import argparse
import whisper
from pathlib import Path


def transcribe_audio(input_path: str, output_path: str, model_name: str = "base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(input_path)
    text = result.get("text", "")
    Path(output_path).write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Transcribe MP3 files using OpenAI Whisper")
    parser.add_argument("input", help="Path to input MP3 file")
    parser.add_argument("output", nargs="?", help="Path to output text file; defaults to input filename with .txt")
    parser.add_argument("--model", default="base", help="Whisper model size to use (tiny, base, small, medium, large)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix('.txt')

    transcribe_audio(str(input_path), str(output_path), model_name=args.model)
    print(f"Transcription saved to {output_path}")


if __name__ == "__main__":
    main()


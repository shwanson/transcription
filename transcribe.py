import argparse
import whisper
from pathlib import Path


def transcribe_audio(
    input_path: str, output_path: str, model_name: str = "base", fp16: bool | None = None
):
    """Transcribe a single MP3 file using Whisper.

    Parameters
    ----------
    input_path: str
        Path to the MP3 file to transcribe.
    output_path: str
        Where to write the resulting text file.
    model_name: str, default "base"
        Whisper model size to use.
    fp16: bool | None, optional
        Whether to use half precision. If ``None``, the setting is determined by
        the device the model is loaded on.
    """
    model = whisper.load_model(model_name)
    if fp16 is None:
        fp16 = model.device.type != "cpu"
    result = model.transcribe(input_path, fp16=fp16)
    text = result.get("text", "")
    Path(output_path).write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe all MP3 files in a folder using OpenAI Whisper"
    )
    parser.add_argument("input", help="Path to folder with MP3 files")
    parser.add_argument(
        "output",
        nargs="?",
        help="Output folder; defaults to the input folder",
    )
    parser.add_argument(
        "--model",
        default="base",
        help="Whisper model size to use (tiny, base, small, medium, large)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path

    if not input_path.is_dir():
        parser.error("input path must be a folder")

    output_path.mkdir(parents=True, exist_ok=True)

    mp3_files = sorted(input_path.glob("*.mp3"))
    if not mp3_files:
        print("No MP3 files found in the input folder")
        return

    for mp3_file in mp3_files:
        out_file = output_path / mp3_file.with_suffix(".txt").name
        transcribe_audio(str(mp3_file), str(out_file), model_name=args.model)
        print(f"Transcription saved to {out_file}")


if __name__ == "__main__":
    main()


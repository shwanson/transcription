# Transcription Tool

This repository provides a simple command line script for transcribing MP3 files to text using [OpenAI Whisper](https://github.com/openai/whisper).

## Requirements

Install the dependencies with pip:

```bash
pip install -r requirements.txt
```

You will also need `ffmpeg` installed on your system.

## Usage

Run the `transcribe.py` script with the path to your audio file. Optionally specify an output text file and the model size (e.g. `tiny`, `base`, `small`, `medium`, `large`).

```bash
python transcribe.py path/to/file.mp3 output.txt --model base
```

If no output file is provided, a `.txt` file with the same name as the input will be created.


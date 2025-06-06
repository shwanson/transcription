# Transcription Tool

This repository provides a simple command line script for transcribing MP3 files to text using [OpenAI Whisper](https://github.com/openai/whisper).

## Requirements

Install the dependencies with pip:

```bash
pip install -r requirements.txt
```

You will also need `ffmpeg` installed on your system.

## Usage

Run the `transcribe.py` script with the path to a folder of MP3 files. Optionally specify an output folder and the model size (e.g. `tiny`, `base`, `small`, `medium`, `large`).

```bash
python transcribe.py path/to/folder path/to/output --model base
```

If no output folder is provided, the transcriptions will be written alongside the MP3 files in the input folder. Each MP3 is saved with the same base name and a `.txt` extension.



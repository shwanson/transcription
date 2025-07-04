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



## Graphical Interface

A simple Tkinter-based GUI is provided in `transcribe_gui.py`. Run it with:

```bash
python transcribe_gui.py
```

Use the **Add Files** button to select one or more MP3 files. If you add a file by mistake, select it in the list and click **Remove Selected** (or press the **Delete** key) to remove it. Choose the Whisper model size and whether to run on the **CPU** or **GPU** from the dropdowns, then click **Start** to transcribe the selected files. Each transcription is saved next to its audio file with a `.txt` extension.
While transcribing, a progress bar and status message show which file is being processed.



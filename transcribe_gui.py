import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import threading

from transcribe import transcribe_audio


class TranscriptionApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("MP3 Transcription Tool")
        self.files = []

        self.file_listbox = tk.Listbox(root, width=60)
        self.file_listbox.pack(padx=10, pady=10)

        controls = tk.Frame(root)
        controls.pack(padx=10, pady=5)

        self.model_var = tk.StringVar(value="base")
        tk.Label(controls, text="Model:").pack(side=tk.LEFT)
        tk.OptionMenu(controls, self.model_var, "tiny", "base", "small", "medium", "large").pack(side=tk.LEFT)

        tk.Button(controls, text="Add Files", command=self.add_files).pack(side=tk.LEFT, padx=5)
        tk.Button(controls, text="Start", command=self.start_transcription).pack(side=tk.LEFT)

        self.status_var = tk.StringVar()
        tk.Label(root, textvariable=self.status_var).pack(pady=5)

    def add_files(self):
        filenames = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        for name in filenames:
            if name not in self.files:
                self.files.append(name)
                self.file_listbox.insert(tk.END, name)

    def start_transcription(self):
        if not self.files:
            messagebox.showwarning("No files", "Please add MP3 files to transcribe.")
            return
        threading.Thread(target=self._transcribe_files, daemon=True).start()

    def _transcribe_files(self):
        self.status_var.set("Starting transcription...")
        model = self.model_var.get()
        for path in self.files:
            mp3_path = Path(path)
            out_file = mp3_path.with_suffix(".txt")
            self.status_var.set(f"Transcribing {mp3_path.name}...")
            transcribe_audio(str(mp3_path), str(out_file), model_name=model)
        self.status_var.set("Done")


def main():
    root = tk.Tk()
    app = TranscriptionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

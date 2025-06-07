import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import threading

from transcribe import transcribe_audio


class TranscriptionApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("MP3 Transcription Tool")
        self.files = []

        self.file_listbox = tk.Listbox(root, width=60, selectmode=tk.MULTIPLE)
        self.file_listbox.pack(padx=10, pady=10)
        self.file_listbox.bind("<Delete>", lambda _event: self.remove_selected())

        controls = tk.Frame(root)
        controls.pack(padx=10, pady=5)

        self.model_var = tk.StringVar(value="base")
        model_row = tk.Frame(controls)
        model_row.pack(pady=(0, 5))
        tk.Label(model_row, text="Model:").pack(side=tk.LEFT)
        tk.OptionMenu(model_row, self.model_var, "tiny", "base", "small", "medium", "large").pack(side=tk.LEFT)

        button_row = tk.Frame(controls)
        button_row.pack()
        tk.Button(button_row, text="Add Files", command=self.add_files).pack(side=tk.LEFT, padx=5)
        tk.Button(button_row, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=5)
        tk.Button(button_row, text="Start", command=self.start_transcription).pack(side=tk.LEFT, padx=5)

        self.status_var = tk.StringVar()
        tk.Label(root, textvariable=self.status_var).pack(pady=5)

        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=1)
        self.progress_bar.pack(fill=tk.X, padx=10, pady=(0, 10))

    def remove_selected(self):
        indices = list(self.file_listbox.curselection())
        for index in reversed(indices):
            self.file_listbox.delete(index)
            del self.files[index]

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
        self.progress_var.set(0)
        self.progress_bar.config(maximum=len(self.files))
        threading.Thread(target=self._transcribe_files, daemon=True).start()

    def _transcribe_files(self):
        self.status_var.set("Starting transcription...")
        model = self.model_var.get()
        total = len(self.files)
        for index, path in enumerate(self.files, start=1):
            mp3_path = Path(path)
            out_file = mp3_path.with_suffix(".txt")
            self.status_var.set(f"Transcribing {mp3_path.name} ({index}/{total})...")
            transcribe_audio(str(mp3_path), str(out_file), model_name=model)
            self.progress_var.set(index)
            self.root.update_idletasks()
        self.status_var.set("Done")


def main():
    root = tk.Tk()
    app = TranscriptionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

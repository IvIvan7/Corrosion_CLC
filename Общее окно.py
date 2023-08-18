import tkinter as tk
from tkinter import ttk
import threading
import time

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Изменяющийся ProgressBar")

        self.progressbar = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progressbar.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Начать", command=self.start_progress)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Остановить", command=self.stop_progress)
        self.stop_button.pack()

        self.running = False
        self.value = 0
        self.progress_thread = None

    def update_progress(self):
        while self.running and self.value < 100:
            self.value += 1
            self.progressbar["value"] = self.value
            time.sleep(0.1)

    def start_progress(self):
        if not self.running:
            self.running = True
            self.progress_thread = threading.Thread(target=self.update_progress)
            self.progress_thread.start()

    def stop_progress(self):
        self.running = False

root = tk.Tk()
app = App(root)
root.mainloop()
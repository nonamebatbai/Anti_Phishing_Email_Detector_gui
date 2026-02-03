import os
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------------- PATHS ----------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FOLDER = os.path.join(BASE_DIR, "data")

# ---------------- GUI ----------------
class EvaluateGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Phishing Model Evaluation")
        self.geometry("700x400")
        self.configure(bg="white")

        self.label_title = tk.Label(
            self, text="Phishing Model Evaluation Plots",
            font=("Arial", 16, "bold"), bg="white"
        )
        self.label_title.pack(pady=10)

        # Frame for images
        self.frame_images = tk.Frame(self, bg="white")
        self.frame_images.pack(pady=5)

        # Load latest plots
        self.conf_matrix_img = self.load_latest_plot("confusion_matrix")
        self.roc_curve_img = self.load_latest_plot("roc_auc_curve")

        # Display Confusion Matrix
        if self.conf_matrix_img:
            self.cm_label = tk.Label(self.frame_images, image=self.conf_matrix_img, bg="white")
            self.cm_label.grid(row=0, column=0, padx=10)

        # Display ROC Curve
        if self.roc_curve_img:
            self.roc_label = tk.Label(self.frame_images, image=self.roc_curve_img, bg="white")
            self.roc_label.grid(row=0, column=1, padx=10)

        # Close button
        self.btn_close = ttk.Button(self, text="Close", command=self.destroy)
        self.btn_close.pack(pady=15)

    def load_latest_plot(self, prefix):
        """
        Load the latest plot file from DATA_FOLDER with given prefix.
        Returns a PhotoImage object.
        """
        files = [f for f in os.listdir(DATA_FOLDER) if f.startswith(prefix) and f.endswith(".png")]
        if not files:
            return None

        # Get the latest file by modification time
        files.sort(key=lambda x: os.path.getmtime(os.path.join(DATA_FOLDER, x)), reverse=True)
        latest_file = os.path.join(DATA_FOLDER, files[0])

        # Open image and resize to fit GUI
        img = Image.open(latest_file)
        img.thumbnail((320, 320))  # Resize to fit nicely
        return ImageTk.PhotoImage(img)

# ---------------- RUN GUI ----------------
if __name__ == "__main__":
    app = EvaluateGUI()
    app.mainloop()

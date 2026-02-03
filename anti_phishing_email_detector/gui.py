import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from PIL import Image, ImageTk
from classifier import predict_email
from database import save_email_history, get_email_history
from email_parser import parse_email_headers
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def launch_dashboard():
    root = tk.Tk()
    root.title("Anti-Phishing Email Detector Dashboard")
    root.geometry("1000x700")

    tab_control = ttk.Notebook(root)

    # ---------------- Email Analyzer Tab ----------------
    tab_analyze = ttk.Frame(tab_control)
    tab_control.add(tab_analyze, text="Analyze Email")

    tk.Label(tab_analyze, text="Paste Email:").pack(anchor="w", padx=10, pady=5)
    email_textbox = scrolledtext.ScrolledText(tab_analyze, height=15)
    email_textbox.pack(fill="x", padx=10)

    def analyze_email():
        email_text = email_textbox.get("1.0", tk.END)
        if not email_text.strip():
            messagebox.showwarning("Warning", "Email content is empty!")
            return

        headers = parse_email_headers(email_text)
        risk_score, verdict = predict_email(email_text, headers)
        if risk_score is None:
            messagebox.showerror("Error", "Model prediction failed!")
            return

        messagebox.showinfo("Analysis Result",
                            f"Verdict: {verdict}\nRisk Score: {risk_score:.2f}")
        save_email_history(headers.get("From", ""), headers.get("Subject", ""), risk_score, verdict)
        update_history_table()

    tk.Button(tab_analyze, text="Analyze Email", command=analyze_email).pack(pady=5)

    # ---------------- History Tab ----------------
    tab_history = ttk.Frame(tab_control)
    tab_control.add(tab_history, text="Email History")

    columns = ("ID", "Sender", "Subject", "Risk Score", "Verdict")
    history_table = ttk.Treeview(tab_history, columns=columns, show="headings")
    for col in columns:
        history_table.heading(col, text=col)
    history_table.pack(fill="both", expand=True, padx=10, pady=10)

    def update_history_table():
        for row in history_table.get_children():
            history_table.delete(row)
        rows = get_email_history()
        for r in rows:
            history_table.insert("", tk.END, values=r)

    update_history_table()

    # ---------------- Evaluation Tab ----------------
    tab_eval = ttk.Frame(tab_control)
    tab_control.add(tab_eval, text="ML Evaluation")

    def load_plot(frame, filename, maxsize=(450, 350)):
        path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(path):
            tk.Label(frame, text=f"{filename} not found").pack()
            return
        img = Image.open(path)
        img.thumbnail(maxsize)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(frame, image=photo)
        label.image = photo
        label.pack(pady=10)

    tk.Label(tab_eval, text="Confusion Matrix").pack()
    load_plot(tab_eval, "confusion_matrix.png")

    tk.Label(tab_eval, text="ROC / AUC Curve").pack()
    load_plot(tab_eval, "roc_auc_curve.png")

    tab_control.pack(expand=1, fill="both")
    root.mainloop()

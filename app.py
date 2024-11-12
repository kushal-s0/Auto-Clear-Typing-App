import tkinter as tk
from tkinter import messagebox
from threading import Timer

class TypingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Typing App")
        self.root.geometry("500x300")
        self.root.configure(bg="#2c3e50")

        header = tk.Label(root, text="Auto-Clear Typing App", font=("Helvetica", 18, "bold"), fg="#ecf0f1", bg="#2c3e50")
        header.pack(pady=10)

        instructions = tk.Label(root, text="Type anything you want, but if you stop for 5 seconds, it will disappear!",
                                font=("Arial", 10), fg="#ecf0f1", bg="#34495e")
        instructions.pack(pady=5)

        self.text_entry = tk.Text(root, width=40, height=8, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50", bd=3, relief="sunken")
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyRelease>", self.reset_timer)
        reset_button = tk.Button(root, text="Clear Text Now", font=("Arial", 10), bg="#e74c3c", fg="white", command=self.clear_text)
        reset_button.pack(pady=5)
        self.timer = None
        self.timeout = 5

    def reset_timer(self, event=None):
        if self.timer:
            self.timer.cancel()

        self.timer = Timer(self.timeout,self.clear_text)
        self.timer.start()

    def clear_text(self):
        self.text_entry.delete("1.0",tk.END)

root= tk.Tk()
app = TypingApp(root)
root.mainloop()
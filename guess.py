import random
import tkinter as tk
from tkinter import messagebox

secret = random.randint(1, 10)


def make_guess(n):
    if n == secret:
        messagebox.showinfo("Resultat", "Du gættede rigtigt!")
    else:
        messagebox.showinfo("Resultat", f"Forkert. Det rigtige tal var {secret}.")
    root.destroy()


root = tk.Tk()
root.title("Gæt et tal")

label = tk.Label(root, text="Gæt et tal mellem 1 og 10:")
label.grid(row=0, column=0, columnspan=5, pady=10)

for i in range(10):
    n = i + 1
    btn = tk.Button(root, text=str(n), width=5, command=lambda n=n: make_guess(n))
    btn.grid(row=1 + i // 5, column=i % 5, padx=5, pady=5)

root.mainloop()

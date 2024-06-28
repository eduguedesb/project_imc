# Script para testar se tkinter está funcionando
import tkinter as tk

root = tk.Tk()
root.title("Teste Tkinter")
root.geometry("300x200")
label = tk.Label(root, text="Tkinter está funcionando!")
label.pack()

root.mainloop()

import ctypes
import tkinter as tk
from tkinter import messagebox

# Ocultar janela do console
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

class DiscordIDApp:
    def __init__(self, master):
        self.master = master
        master.title("Discord ID Menu")

        # Configurações para um visual mais estilizado
        master.geometry("480x270")
        master.configure(bg="#303030")  # Fundo mais escuro

        # Removendo a barra de título padrão
        master.overrideredirect(True)

        # Inicializando as variáveis para o movimento da janela
        self.x, self.y = 0, 0

        # Adicionando eventos para permitir o movimento da janela
        master.bind("<ButtonPress-1>", self.start_move)
        master.bind("<B1-Motion>", self.on_motion)

        self.label_frame = tk.Frame(master, bg="#303030")  # Container para rótulo e entrada
        self.label_frame.pack(side="top", fill="x", pady=10)

        self.name_label = tk.Label(self.label_frame, text="Evasi0n", fg="white", bg="#303030", font=("Arial", 16))
        self.name_label.pack(side="left", pady=5, padx=10)

        self.key_label = tk.Label(self.label_frame, text="Insirt your Key for access the Panel", fg="white", bg="#303030", font=("Arial", 12))
        self.key_label.pack(side="left", pady=5)

        self.discord_id_entry = tk.Entry(master, font=("Arial", 12), bg="#404040", fg="white", insertbackground="white", selectbackground="#555555", borderwidth=0, highlightthickness=0)
        self.discord_id_entry.pack(pady=10, padx=20, ipady=8)  # Adiciona algum espaço interno e aumenta o tamanho vertical

        # Ajustando a disposição dos elementos
        self.name_label.pack_forget()
        self.key_label.pack_forget()
        self.name_label.pack(side="top", pady=5, padx=10)
        self.key_label.pack(side="top", pady=5)

        # Alterando a cor do botão "Login" para um cinza mais escuro
        self.login_button = tk.Button(master, text="Access", command=self.login, bg="#404040", fg="white", font=("Arial", 12), relief="flat", padx=10)
        self.login_button.pack(pady=10)

        # Adicionando botão "X" para fechar a janela
        self.close_button = tk.Button(master, text="X", command=self.close_app, bg="#303030", fg="white", font=("Arial", 10), relief="flat")
        self.close_button.place(relx=1, rely=0, anchor='ne')

    def login(self):
        discord_id = self.discord_id_entry.get()

        if discord_id and discord_id.isdigit():
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Erro de Login", "Por favor, insira um Discord ID válido.")

    def start_move(self, event):
        self.x, self.y = event.x, event.y

    def on_motion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry(f"+{x}+{y}")

    def close_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiscordIDApp(root)
    root.mainloop()

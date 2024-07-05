import customtkinter as ctk
from tkinter import *

window = ctk.CTk()


class Aplication:

    def __init__(self):
        self.theme()
        self.screen()
        self.screen_login()
        self.window = window
        self.window.mainloop()

    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def screen(self):
        window.geometry("700x400")
        window.title("Tela de Login")
        window.iconbitmap("icon.ico")
        window.resizable(False, False)

    def screen_login(self):
        # Banner Login
        image = PhotoImage(file="Banner.png")
        label_img = ctk.CTkLabel(master=window, image=image, text=None)
        label_img.place(x=5, y=65)

        # Frames
        login_frame = ctk.CTkFrame(master=window, width=350, height=396)
        login_frame.pack(side=RIGHT)

        label = ctk.CTkLabel(
            master=login_frame,
            text="Tela de Login",
            font=("Roboto", 25, "bold"),
            text_color=("white"),
        )
        label.place(x=90, y=10)

        # Username Entry
        username_entry = ctk.CTkEntry(
            master=login_frame,
            placeholder_text="Nome de Usuário",
            width=300,
            font=("Roboto", 16),
        ).place(x=25, y=105)

        username_label = ctk.CTkLabel(
            master=login_frame,
            text="O campo nome de usuario é obrigatorio",
            text_color="green",
            font=("Roboto", 12),
        ).place(x=25, y=135)

        # Password Entry
        password_entry = ctk.CTkEntry(
            master=login_frame,
            placeholder_text="Senha",
            width=300,
            font=("Roboto", 16),
            show="•",
        ).place(x=25, y=175)

        password_label = ctk.CTkLabel(
            master=login_frame,
            text="O campo senha é obrigatorio",
            text_color="green",
            font=("Roboto", 12),
        ).place(x=25, y=205)

        # Button Login

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300).place(
            x=25, y=250
        )

        label_tt = ctk.CTkLabel(
            master=window,
            text="Faça login para acessar a plataforma",
            font=("Roboto", 18, "bold"),
            text_color="#00B0F0",
        ).place(x=10, y=15)


Aplication()

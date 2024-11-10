from base64 import standard_b64decode
import customtkinter as ctk
from tkinter import *
from tkinter import simpledialog
import Cliente as client
import threading

root = ctk.CTk()

root.title("Chat - Client")
root.geometry("320x320+620+150")
root.config(background="#4B5267")
ctk.set_appearance_mode("System")


def enviar_mensagem(chat_callback, username, msg, client_connected):
    client.main("", "", "", "", chat_callback, close, username, msg, client_connected)
    message_entry.delete(0, END)


def close():
    for widget in root.winfo_children():
        widget.destroy()
    root.quit()


def conectado(client):
    print("Conexão feita com sucesso!")
    conn_frame.destroy()
    chat_frame.pack(fill="both", expand=1)

    message_label = ctk.CTkLabel(chat_frame, text="Mensagem", width=60, bg_color="#4B5267", anchor="center", font=("Inter", 15))
    message_label.pack(fill="x")
    message_entry.pack(fill="x", pady=5, padx=20)
    message_button = Button(
        chat_frame,
        text="Enviar",
        bg="#171c2f",
        fg="white",
        font=("Inter", 12),
        activebackground="#171c2f",
        activeforeground="white",
        cursor="hand2",
        command=lambda: enviar_mensagem(chat, username, message_entry.get(), client),
        bd=0,
    )
    message_button.pack(fill="x", padx=30)

    chat_label = ctk.CTkLabel(chat_frame, text="Chat", width=60, bg_color="#4B5267", anchor="center", font=("Inter", 15))
    chat_label.pack(fill="x", pady=10)

    chat_textbox.pack(fill="both", expand=1, padx=20, pady=10)


def erro_conexao():
    global var_conectado
    var_conectado = 0
    option_title.configure(text="Não foi possível conectar!")


def chat(msg):
    chat_textbox.configure(state="normal")
    chat_textbox.insert(END, msg + "\n")
    chat_textbox.configure(state="disabled")


def conectar():
    global username, var_conectado  # Variável é utilizada para impedir que o usuário tente fazer conexão duas vezes
    if not var_conectado:
        if client.validarIp(ip_entry.get()):
            print("IP Válido")
            var_conectado = 1
            username = simpledialog.askstring("Input", "Digite seu usuário: ", parent=conn_frame)
            server_thread = threading.Thread(
                target=client.main, args=(ip_entry.get(), int(port_entry.get()), conectado, erro_conexao, chat, close, username)
            )
            server_thread.daemon = True
            server_thread.start()
        else:
            print("IP Inválido")


username = ""

var_conectado = 0  # Variável para verificar se já foi conectado

conn_frame = ctk.CTkFrame(root, width=320, height=400, bg_color="#4B5267", fg_color="#4B5267")
conn_frame.grid(row=0, column=0)

option_title = Label(conn_frame, text="Conexão", bg="#4B5267", fg="white", font=("Inter", 15), anchor="center")
option_title.grid(row=0, column=0, pady=(10, 0), columnspan=2)

config_frame = ctk.CTkFrame(conn_frame, width=320, height=400, bg_color="#4B5267", fg_color="#4B5267")
config_frame.grid(row=1, column=0)
ip_label = ctk.CTkLabel(config_frame, text="IP: ", width=60, bg_color="#4B5267", font=("Inter", 15)).grid(
    row=1, column=0, pady=(50, 0)
)
ip_entry = ctk.CTkEntry(config_frame, width=245, bg_color="#4B5267")
ip_entry.grid(row=1, column=1, pady=(50, 0))

port_label = ctk.CTkLabel(config_frame, text="Porta: ", width=60, bg_color="#4B5267", font=("Inter", 15)).grid(
    row=2, column=0, pady=(50, 0)
)
port_entry = ctk.CTkEntry(config_frame, width=245, bg_color="#4B5267")
port_entry.grid(row=2, column=1, pady=(50, 0))

chat_frame = ctk.CTkFrame(root, width=320, height=400, bg_color="#4B5267", fg_color="#4B5267")
chat_textbox = ctk.CTkTextbox(chat_frame, font=("Inter", 15), state="disabled")
chat_input = ctk.CTkEntry(chat_frame, font=("Inter", 15))

message_entry = ctk.CTkEntry(chat_frame, width=60)

Button(
    config_frame,
    width=20,
    text="Conectar",
    bg="#171c2f",
    fg="white",
    font=("Inter", 12),
    activebackground="#171c2f",
    activeforeground="white",
    cursor="hand2",
    command=lambda: conectar(),
    bd=0,
).grid(row=3, column=0, columnspan=2, pady=(80, 0), padx=(30, 0))

root.mainloop()

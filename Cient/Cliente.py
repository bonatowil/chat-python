import threading
import socket
import ipaddress
import datetime


# função para validar o IP
def validarIp(IPserver):
    try:
        ipaddress.ip_address(IPserver)
        return True
    except ValueError:
        return False


# função que recebe as mensagens
def receiveMessages(client, close_callback, message_callback):
    while True:
        try:
            msg = client.recv(2048).decode("utf-8")
            message_callback(msg)
        except:
            client.close()
            close_callback()
            break


# função que envia as mensagens
def sendMessages(client, username, message_callback, conexao=False, msg=""):
    try:
        if conexao:
            client.send(f"Usuário {username} conectado!".encode("utf-8"))
            return
        if not msg:
            return
        client.send(f"{datetime.datetime.now().strftime('%H:%M')} | {username}: {msg}".encode("utf-8"))
        message_callback(f"{datetime.datetime.now().strftime('%H:%M')} | {username}: {msg}")
    except Exception as e:
        print(e)
        print("\nErro ao enviar mensagem.")


# função main
def main(IPserver, port, conexao_callback, failed_callback, message_callback, close_callback, username="", msg="", client=""):

    # Coleta de dados
    if client == "":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destiny = IPserver, int(port)

        # fazer conexão com o servidor de destino
        try:
            client.connect(destiny)
        except Exception as e:
            print(e)
            failed_callback()
            return False

        sendMessages(client, username, message_callback, True)
        conexao_callback(client)
        print("\nConectado")

    # Iniciar threads para receber e enviar mensagens
    thread1 = threading.Thread(target=receiveMessages, args=(client, close_callback, message_callback))
    thread2 = threading.Thread(target=sendMessages, args=(client, username, message_callback, False, msg))

    thread1.start()
    thread2.start()


def callback():
    pass


if __name__ == "__main__":
    IPserver = input("Insira o ip do servidor\n")
    port = int(input("Insira a porta\n"))
    main(IPserver, port, callback, callback, callback)

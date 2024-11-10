import threading
import socket
import ipaddress


def validarIp(IPserver):
    try:
        ipaddress.ip_address(IPserver)
        return True
    except ValueError:
        return False


clients = []


def receiveMessages(client, message_callback):
    while True:
        try:
            msg = client.recv(2048).decode("utf-8")
            message_callback(msg)
            messageBroadcast(msg, client)  # Chame a função de broadcast passando a mensagem
        except:
            print("Não foi possível permanecer conectado no servidor!")
            deleteClient(client)
            break


# função que envia as mensagens
def messageBroadcast(msg, sender_client):
    for client in clients:
        if client != sender_client:  # Envie apenas para os outros clientes
            try:
                client.send(msg.encode("utf-8"))
            except:
                print("Erro ao enviar mensagem para um cliente. Cliente será removido.")
                deleteClient(client)


# função para deletar cliente
def deleteClient(client):
    clients.remove(client)
    client.close()


# função main
def main(IPserver, port, conexao_callback, failed_callback, message_callback):
    # coleta de dados
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # conexão com o servidor
    try:
        server.bind((IPserver, int(port)))
        server.listen(10)  # O parametro indica a quantidade de conexoes que serao permitidas
    except:
        failed_callback()
        return False

    # Adicionando os clientes no servidor
    conexao_callback()
    while True:
        client, addr = server.accept()
        clients.append(client)

        thread1 = threading.Thread(target=receiveMessages, args=(client, message_callback))
        thread1.start()


def callback():
    pass


if __name__ == "__main__":
    IPserver = input("Insira o ip do servidor\n")
    port = int(input("Insira a porta\n"))
    main(IPserver, port, callback, callback, callback)

# Exemplo basico socket (lado ativo)

import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect((HOST, PORTA)) 

#faz a verificação se o arquivo existe com o try para não gerar mensagem de erro
inputClient = input("Escreva o arquivo que sera aberto: ")
try:
    file = (open(inputClient+'.txt','r'))
    print("arquivo aberto")
    file_string = file.read()
    while(inputClient != ("end")):
        file_string = file_string.encode()
        # envia uma mensagem para o par conectado
        sock.send(file_string)
        
        #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
        msg = sock.recv(1024) # argumento indica a qtde maxima de bytes da mensagem
    
        # imprime a mensagem recebida
        print("\nA mensagem recebida do servidor passivo foi ",str(msg,  encoding='utf-8'))
        file.close()
        inputClient = input("\nDeseja enviar mais uma? Escreva o nome do arquivo ou end para terminar: ")
        if(inputClient!="end"):
            file = (open(inputClient+'.txt','r'))
            print("arquivo aberto")
            file_string = file.read()
    # encerra a conexao
    sock.close() 
    
    print("\nconexão encerrada!")
except:
    print("arquivo nao encontrado")


    

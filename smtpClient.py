from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM) # creating a TCP socket
    clientSocket.connect((mailserver, port)) # establishing a TCP connection with the mailserver and port
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM: <alice@email.com>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptCommand = 'RCPT TO: <leul@email.com>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '354':
    #    print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    msg1 = 'Do you like olives? How about dates?\r\n'
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    end = '.\r\n'
    sendMsg = msg1 + end
    clientSocket.send(sendMsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1) 
    if recv1[:3] != '221':
        print('221 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
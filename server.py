import select
from socket import *
#import act_comm
#import create
import player

addr = ('', 4000)

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(addr)
server.listen(100)
print 'listening'

clients = []
data = []
nome = []


def send_to_all(sender, string):
  for c in clients:
    if not c == sender:
      c.send(string)

def send_to(pg, string):
  pg.send(string)

def chat(pg, argument):
  send_to_all(pg.client, "%s chatta %s\n" % (pg.name, argument))

def new_char(pg):
  del nome[:]
  nome.append("")
  pg.send("come ti chiami?  ")
  for ca in pg.recv(4096).strip():
    if ca == '\n':
      break
    nome.append(ca)
  new_player.name = ''.join(nome[1:])
  return 

while True:
  sockets = [server] + clients
  readable, writeable, exceptional = select.select(sockets, [], [])

  for sock in readable: 
    if sock == server:
      client, addr = server.accept()
      new_player = player.Player(sock, addr)
      print "Nuova Connessione: %s" % str(addr)
      client.send("Benvenuto!\n")
      clients.append(client)
      new_char(client)
#      client.send ("Ciao %s\n" % classes.char.name)
    else:
      if new_player.handler(sock) == 'kill':
        print "%s Disconnesso: %s" % (new_player.name, str(addr))
        clients.remove(sock)
        sock.close()
    break

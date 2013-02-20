import select
from socket import *
#import act_comm
#import create
import classes

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

  return 

def handler(client):
  classes.char.client = client
  classes.char.name = ''.join(nome[1:])
  input = client.recv(4096).strip()
  args = input.split(" ",1)
  command = args[0]
  string = ''.join(args[1:])
  if(command == ''):
    return ''
  if('chatta'.startswith(command)):
#    act_comm.chat(client, string)
     chat(classes.char, string)
     return
  if('qui'.startswith(command)):
    client.send("Devi scrivere 'quit' per intero\n")
    return ''
  if('quit'.startswith(command)):
    client.send("comando trovato!\n")
    return 'kill'

while True:
  sockets = [server] + clients
  readable, writeable, exceptional = select.select(sockets, [], [])

  for sock in readable: 
    if sock == server:
      client, addr = server.accept()
      print "Nuova Connessione: %s" % str(addr)
      client.send("Benvenuto!\n")
      clients.append(client)
      new_char(client)
#      client.send ("Ciao %s\n" % classes.char.name)
    else:
      if handler(sock) == 'kill':
        print "%s Disconnesso: %s" % (classes.char.name, str(addr))
        clients.remove(sock)
        sock.close()
    break

from socket import *
import select

import player

addr = ('', 4000)
players = []


#def send_to_all(sender, string):
#  for c in clients:
#    if not c == sender:
#      c.send(string)
#
#def send_to(pg, string):
#  pg.send(string)
#
#def chat(pg, argument):
#  send_to_all(pg.client, "%s chatta %s\n" % (pg.name, argument))
#
#def new_char(pg):
#  del nome[:]
#  nome.append("")
#  pg.send("come ti chiami?  ")
#  for ca in pg.recv(4096).strip():
#    if ca == '\n':
#      break
#    nome.append(ca)
#  new_player.name = ''.join(nome[1:])
#  return 


def server_loop(listener)
  sockets = [listener] + [p.socket for p in players]
  readable, writeable, exceptional = select.select(sockets, [], [])

  if listener in readable
    new_player = player.Player(listener.accept())
    players.append(new_player)

    print "Nuova connessione: %s" % str(new_player.addr)

  for player in players:
    if player.socket not in readable: continue
    if player.handler(players) == 'kill':
        print "%s Disconnesso: %s" % (new_player.name, str(addr))
        player.socket.close()
        players.remove(player)


if __module__ == '__main__':
  server = socket(AF_INET, SOCK_STREAM)
  server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  server.bind(addr)
  server.listen(100)
  print 'listening'
  while True: server_loop(server)


class Player:

  def __init__(self, connection):
    self.socket, self.addr = connection
    self.name = ''


  def handler(self, players):

    msg = self.socket.recv(4096).strip() + ' '
    command, args = msg.split(" ", 1)

    if not self.name:
      if command == 'nome':
        self.name = args.strip()
      else:
        self.socket.send('usa il comando "nome" seguito dal tuo nome.\n')
      return

    if(command == ''):
      return

    if('chatta'.startswith(command)):
      msg = "%s chatta %s\n" % (self.name, args)
      for p in players: p.socket.send(msg)
      return

    if('qui'.startswith(command)):
      self.socket.send("Devi scrivere 'quit' per intero\n")
      return

    if('quit'.startswith(command)):
      self.socket.send("comando trovato!\n")
      return 'kill'


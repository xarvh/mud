class Player:

  def __init__(self, connection):
    self.socket, self.addr = connection
    self.name = ''
    self.socket.send('Benvenuto!\nDigita il tuo nome:\n')


  def handler(self, players):

    msg = self.socket.recv(4096).strip()
    if not self.name:
      self.name = msg
      return

    command, args = (msg+' ').split(" ", 1)

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


class Player:
  def __init__(self, socket):
    self.socket = socket
    self.name = ''

  def handler(self):
    data = self.socket.recv(4096)


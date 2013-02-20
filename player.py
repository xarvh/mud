class Player:
  def __init__(self, socket, addr):
    self.socket = socket
    self.name = ''

  def handler(client):
 #   classes.char.client = client
 #   classes.char.name = ''.join(nome[1:])
    input = client.recv(4096).strip()
    args = input.split(" ",1)
    command = args[0]
    string = ''.join(args[1:])
    if(command == ''):
      return ''
    if('chatta'.startswith(command)):
#      act_comm.chat(client, string)
       chat(classes.char, string)
       return
    if('qui'.startswith(command)):
      client.send("Devi scrivere 'quit' per intero\n")
      return ''
    if('quit'.startswith(command)):
      client.send("comando trovato!\n")
      return 'kill'

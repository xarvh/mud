AREE_PATH="aree/"
totale_stanze = 2



class Load_room():
  def __init__(self):
    self.num = ''
    self.name = ''
    self.desc = []

def carica(area):

  lista = []
  afile = open("%s%s" % (AREE_PATH, area), "r")
  for i in range (totale_stanze):
#    print i
    riga = []

#    while True:
    riga = afile.readline()
#    print riga[:-1]
#    if riga == "EOF\n": break
    r = Load_room()
    r.num = int(riga[:-1])
    r.name = afile.readline()[:-1]
    while ( True ):                          #leggo la descrizione
      riga = afile.readline()[:-1]
      if riga == "'''" : break
      r.desc.append(riga)
    lista.append(r)
#  print lista[1].desc
  return lista


#  print lista[0].num
#  print lista[1].num
carica("area_prova")

import pygame

class Harcos:
  def __init__(self, nev, eletero, harciero):
    self.nev = nev
    self.eletero = eletero
    self.harciero = harciero

  def getEletero(self):
    return self.eletero

  def getHarciero(self):
    return self.harciero

  def sebzodik(self, harciero):
    self.eletero -= harciero

  def harcol(self, harcos):
    self.sebzodik(harcos.getHarciero())
    harcos.sebzodik(self.getHarciero())
    if self.getEletero() < 1 or harcos.getEletero() < 1:
      return True
    return False

  def __repr__(self):
    return f'<object.harcos: {self.nev}, HE:{self.getHarciero()}, EE:{self.getEletero()})>'

h1 = Harcos('Spartakus', 20, 2)
h2 = Harcos('Herkules', 10, 2)

kor = 1
while not h1.harcol(h2):
  print(f'{kor}. kör:')
  print(h1)
  print(h2)
  kor+=1

if h1.getEletero()<1 and h2.getEletero()<1:
  print('Mindketten veszítettel!')
elif h1.getEletero() < 1:
  print(f'Nyertes: {h2}')
else:
  print(f'Nyertes: {h2}')
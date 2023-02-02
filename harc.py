h1 = Harcos('Spartakus', 200, 2)
h2 = Harcos('Herkules', 120, 2)

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
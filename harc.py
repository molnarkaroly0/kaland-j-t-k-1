import random

dobas = [random.randint(1,6) for _ in range(2)]
dobas2 = random.randint(1,6)
dobas3 = random.randint(1,6)

sajathp = sum(dobas) + 12
sajatdmg = dobas2 + 6
sajatluck = dobas3 + 6

def Tolvaj():
    Thp = 6
    Tdmg = 7
    return f'Tolvaj ellenfél; Életereje: {Thp}, Ügyessége {Tdmg}'

print(*dobas)
print(dobas2)
print(dobas3)
print(f'Saját Életerő: {sajathp}')
print(f'Saját Ügyesség: {sajatdmg}')
print(f'Saját Szerencse: {sajatluck}')
print(Tolvaj())
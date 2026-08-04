# Hash
from random import choice, randint

legions = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
table_region = [None] * 15
table_id = [None] * 1000

def hash_id(clave: int) -> int:
    
    return clave % 1000

for i in range (10):
    trooper = f'{choice(legions)}-{randint(1000, 9999)}'
    
    print(trooper)
    
def hash_legion(clave: str) -> int:
    h = 0
    for caracter in clave:
        h = h * 33 + ord(caracter)
    return h % 15

#for legion in legions:
#    print( legion, hash_legion(legion))
    
for i in range(100):
    trooper = f'{choice(legions)}-{randint(1000, 9999)}'
    index = hash_legion(trooper[:2])
    index_id = hash_id(int(trooper[3:]))
    
    if table_id[index_id] is None:
        table_id[index_id] = []
    
    if table_region[index] is None:
        table_region[index] = []
        
    table_region[index].append(trooper)
    
#print(table_region)

index_id = hash_id(781)
for trooper in table_id[index_id]:
    print(trooper)
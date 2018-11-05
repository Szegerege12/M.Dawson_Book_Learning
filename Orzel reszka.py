### Program wyrzucajacy 100 razy moneta, i zwracaacy liczbe wylosowanych

import random
orzel = 0
reszka = 0
for i in range(100):
    if random.randint(0,1):
        orzel += 1
    else:
        reszka +=1

print("Ilosc orlow:",orzel)
print("Ilosc reszek:",reszka)
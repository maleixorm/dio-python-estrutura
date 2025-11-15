string = "abracadabra"
contador = dict()

for caractere in string:
    if caractere in contador:
        contador[caractere] += 1
    else:
        contador[caractere] = 1

print(contador)
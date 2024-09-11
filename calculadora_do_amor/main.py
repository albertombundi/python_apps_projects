import random

# o valor conterá diígitos  entre 0-9

st = '123456789'

#  resultado será em dois dígitos 
digitos = 2


# variável que contém o resultado
resultado = "".join(random.sample(st, digitos))
print(resultado)
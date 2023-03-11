#EXEMPLOS DE SORTEIO OU NUMEROS ALEATORIOS

#Sorteia 1 unico numero DE 0 A 10
import random
y = random.randint(0,10)
print(y)
# 5 NUMEROS SORTEADOS EM UMA UNICA LINHA DE 0 A 10
import random
x = [random.randint(0, 10) for p in range(0, 5)]
print(x)

#Sorteia Apenas numero par , de 0 a 100
import random
x = random.randrange(0,101,2)
print(x)

#Sorteio de 10 N°  De 0 a 20 que nao se repete o mesmo numero
import random
x = random.sample(range(21),10)
print(x)

#sorteador de 0 a 10  float
import random
y = random.uniform(0,11)
print(f"{y:,.2f}")

#SORTEADOR DE NOME
import random
JokeAle=['Maria', 'João', 'Pedro', 'Cláudia']
Nome=(random.choice(JokeAle))
print(f"oi {Nome}")
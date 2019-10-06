a=int(input())
print(a)

n_notas_100=0
n_notas_50=0
n_notas_20=0
n_notas_10=0
n_notas_5=0
n_notas_2=0
n_notas_1=0

while (a >= 1):
    if (a>=100):
        n_notas_100=(a//100)
        a=a%100
    elif (a>=50):
        n_notas_50=(a//50)
        a=a%50
    elif (a>=20):
        n_notas_20=(a//20)
        a=a%20
    elif (a>=10):
        n_notas_10=(a//10)
        a=a%10
    elif (a>=5):
        n_notas_5=(a//5)
        a=a%5
    elif (a>=2):
        n_notas_2=(a//2)
        a=a%2
    elif (a>=1):
        n_notas_1=(a//1)
        a=a%1

print("{} nota(s) de R$ 100,00".format(n_notas_100))
print("{} nota(s) de R$ 50,00".format(n_notas_50))
print("{} nota(s) de R$ 20,00".format(n_notas_20))
print("{} nota(s) de R$ 10,00".format(n_notas_10))
print("{} nota(s) de R$ 5,00".format(n_notas_5))
print("{} nota(s) de R$ 2,00".format(n_notas_2))
print("{} nota(s) de R$ 1,00".format(n_notas_1))

a=input().split('.')
notas=int(a[0])
moedas=int(a[1])

n_notas_100=0
n_notas_50=0
n_notas_20=0
n_notas_10=0
n_notas_5=0
n_notas_2=0
n_notas_1=0

n_moedas_100=0
n_moedas_50=0
n_moedas_25=0
n_moedas_10=0
n_moedas_5=0
n_moedas_1=0

while (notas >= 1):
    if (notas>=100):
        n_notas_100=(notas//100)
        notas=notas%100
    elif (notas>=50):
        n_notas_50=(notas//50)
        notas=notas%50
    elif (notas>=20):
        n_notas_20=(notas//20)
        notas=notas%20
    elif (notas>=10):
        n_notas_10=(notas//10)
        notas=notas%10
    elif (notas>=5):
        n_notas_5=(notas//5)
        notas=notas%5
    elif (notas>=2):
        n_notas_2=(notas//2)
        notas=notas%2
    elif (notas>=1):
        n_moedas_100=(notas//1)
        notas=notas%1

while (moedas >= 1):
    if (moedas>=50):
        n_moedas_50=(moedas//50)
        moedas=moedas%50
    elif (moedas>=25):
        n_moedas_25=(moedas//25)
        moedas=moedas%25
    elif (moedas>=10):
        n_moedas_10=(moedas//10)
        moedas=moedas%10
    elif (moedas>=5):
        n_moedas_5=(moedas//5)
        moedas=moedas%5
    elif (moedas>=1):
        n_moedas_1=(moedas//1)
        moedas=moedas%1

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(n_notas_100))
print("{} nota(s) de R$ 50.00".format(n_notas_50))
print("{} nota(s) de R$ 20.00".format(n_notas_20))
print("{} nota(s) de R$ 10.00".format(n_notas_10))
print("{} nota(s) de R$ 5.00".format(n_notas_5))
print("{} nota(s) de R$ 2.00".format(n_notas_2))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(n_moedas_100))
print("{} moeda(s) de R$ 0.50".format(n_moedas_50))
print("{} moeda(s) de R$ 0.25".format(n_moedas_25))
print("{} moeda(s) de R$ 0.10".format(n_moedas_10))
print("{} moeda(s) de R$ 0.05".format(n_moedas_5))
print("{} moeda(s) de R$ 0.01".format(n_moedas_1))

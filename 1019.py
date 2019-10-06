a=int(input())

horas=0
minutos=0
segundos=0

while (a >= 1):
    if (a >= 3600):
        horas=(a//3600)
        a=a%3600
    elif (a >= 60):
        minutos=(a//60)
        a=a%60
    elif (a >= 1):
        segundos=a
        a=0

print("{}:{}:{}".format(horas,minutos,segundos))

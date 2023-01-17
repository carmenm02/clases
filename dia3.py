def impar(lista):
    for i in lista:
        if i % 2 == 1:
            print(" %s Es impar"% (i))

#impar([2,4,5,6,8])

def ejer(listaa):
    lista = []
    if len(listaa)%2==0:
        for i in range(int(len(listaa)/2)):
            if i == 0:
                var = listaa[i] + "" + listaa[i+1]
            else:
                i*=2
                var = listaa[i] + "" + listaa[i+1]
            lista.append(var)
    else:
        for i in range(int((len(listaa)-1)/2)):
            if i == 0:
                var = listaa[i] + "" + listaa[i+1]
            else:
                i*=2
                var = listaa[i] + "" + listaa[i+1]
            lista.append(var)
        lista.append(listaa[len(listaa)-1]+"_") 

    return lista

print(ejer("Holaa")) 


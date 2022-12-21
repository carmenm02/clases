def cuadrados():
    numero = int(input("Introduce un numero:"))
    dic = {}
    for i in range(1,numero+1):
        dic[i]=i**2

    return dic

#print(cuadrados())

def numeroveces():
    dic={}
    cadena=input("Introduce algo: ")
    for i in cadena:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic

#print(numeroveces())

def frutas():
    dic={"manzana":3,"pera":2}
    salir=True
    while salir:
        fruta=input("Introduce una fruta: ")
        if fruta.lower() not in dic:
            print("No existe la fruta")
        else:
            cantidad = int(input("Cuanta fruta quieres:"))
            precio=cantidad*dic[fruta]
            print(precio)
        fruta2 = input("Quieres algo mas?")
        while fruta2 != "n" and fruta2 != "s":
            fruta2=input("Quieres algo mas?")
        if fruta2 == "n":
            salir=False
frutas()
def programa():
    while True:
        print("1.AÑADIR ALUMNO")
        print("2.AÑADIR ASIGNATURA A ALUMNO")
        print("3.BORRAR DATOS")
        print("4.SALIR")

        pedir = int(input("Introduce una opcion: "))

        dic = {}

        if pedir == 1:
            nom = input("Introduce un nombre: ")
            dic[nom]={"a":"a"}
        elif pedir == 2:
            nom = input("Introduce un nombre: ")
            if nom not in dic:
                dic[nom]={}
            asig = input("Introduce una asignatura: ")
            lis = []
            parar = True
            while parar:
                notas = input("Introduce una nota: ")
                if notas != "x":
                    lis.append(int(notas))
                else:
                    parar = False
            dic[nom][asig] = lis
        elif pedir == 3:
            al = input("Introduce un nombre para borrar: ")
            if al in dic:
                del dic[al]
            else:
                print("No existe")
        elif pedir == 4:
            return dic
        elif pedir==5:
            print(dic)

print(programa())
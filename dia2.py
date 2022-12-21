def agenda():
    dic = {}
    while True:
        print("1.Añadir")
        print("4.Listar")
        print("2.Buscar")
        print("3.Borrar")
        print("5.Salir")
    
        opcion = int(input("Dime una opcion: "))

        if opcion == 1:
            nombre = input("Introduce un nombre: ")
            if nombre in dic:
                print(nombre,dic[nombre])
                pr = input("Quiere modificar?")
                if pr == "Si":
                    nuevonumero = input("Introduce el nuevo numero: ")
                    print(nombre,nuevonumero)
                    dic[nombre] = nuevonumero
            else:
                num_añadido = input("Introduce el numero que quieres añadir: ")
                dic[nombre] = num_añadido
        elif opcion == 2:
            nombre = input("Introduce el nombre que deseas buscar:")
            for i in dic:
                if i.startswith(nombre):
                    print("nombre: %s , numero: %s" %(i,dic[i]))
        elif opcion == 3:
            nombre = input("Introduce el nombre que deseas borrar: ")
            if nombre in dic:
                del dic[nombre]
        elif opcion == 4:
            for i in dic:
                print(i,dic[i])
        elif opcion == 5:
            break

#agenda()

def ejer():
    frase = input("Introduce una frase: ")
    frase2 = ""
    for i in frase:
        if i.isupper():
            frase2 += " " + i
        else:
            frase2 += i
    return frase2

print(ejer())
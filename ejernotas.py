ALUMNO = 0; ASIGNATURA = 1; PRACTICA = 2; NOTAS = 3

notas = [
    ['Brutus', 'Algebra', 'mal', [3.2, 5.1, 0.8]],
    ['Brutus', 'Discreta', 'regular', [5.2, 3.7, 5.0]],
    ['Brutus', 'Programacion', 'mal', [0.5, 3.2, 4.0]],
    ['Flavia', 'Algebra', 'bien', [7.2, 5.6, 7.1]],
    ['Flavia', 'Discreta', 'regular', [4.9, 8.5, 5.2]],
    ['Flavia', 'Programacion', 'bien', [9.5, 8.3, 10.0]],
    ['Jovina', 'Programacion', 'bien', [7.4, 9.3, 8.2]],
    ['Secundus', 'Algebra', 'mal', [3.1, 5.5, 6.1]],
    ['Secundus', 'Discreta', 'bien', [7.3, 6.7, 8.5]],
    ['Secundus', 'Programacion', 'mal', [4.5, 3.3, 4.2]],
    ['Sextus', 'Algebra', 'bien', [9.3, 9.8, 9.9]],
    ['Sextus', 'Programacion', 'bien', [8.9, 9.3, 8.9]]    
]

def lista():
    al = []
    asig = []
    for lista in notas:
        if lista[0] not in al:
            al.append(lista[0])
        if lista[1] not in asig:
            asig.append(lista[1])
    return al, asig
print(lista())

def nota():
    nom = []
    for lista in notas:
        if lista[2] == 'bien':
            for i in lista[3]:
                if i >= 9.0:
                    if lista[0] not in nom:
                        nom.append(lista[0])
    return nom
print(nota())

def menu_nombre():
    while True:
        print("1.Buscar por nombre")
        print("2.Buscar por asignaturas")
        print("3.Buscar por practicas")
        print("4.Buscar por notas")
        print("5.Salir")
        
        pedir = int(input("Que quieres buscar: "))

        if pedir == 1:
            nom = input("Introduce un nombre: ")
            dic = {}
            datos = {}
            datos['asignatura'] = []
            datos['practica'] = []
            datos['notas'] = []
            for i in notas:
                if nom == i[0]:
                    datos['asignatura'].append(i[1])
                    datos['practica'].append(i[2])
                    datos['notas'].append(i[3])
            dic[nom] = datos
            print(dic)
        
        elif pedir == 2:
            n = input('Dime que asignatura quieres buscar: ')
            dic={}
            d={}

            for l in notas:
                if l[ASIGNATURA]==n:
                    lista2=[]
                    lista2.append(l[NOTAS])
                    lista2.append(l[PRACTICA])
                    d[l[ALUMNO]]=lista2
            
            dic[n]=d
            print(dic)
        
        elif pedir == 3:
            prac = input("Introduce la practica: ")
            dic = {}
            lis = []
            for i in notas:
                if prac == i[PRACTICA]:
                    tup = (i[ALUMNO],i[ASIGNATURA])
                    lis.append(tup)
            dic[prac]=lis
            print(dic)
        
        elif pedir == 4:
            nota = int(input("Introduce una nota: "))
            dic = {}
            lis = []
            for i in notas:
                lista = []
                for j in i[NOTAS]: 
                    if j >= nota:
                        lista.append(j)
                        t = (i[ALUMNO],i[ASIGNATURA],lista)
                        lis.append(t)
            dic[nota]=lis
            print(dic)
        
        elif pedir == 5:
            break

print(menu_nombre())           
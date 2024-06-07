import ex1
import ex2
import ex3
import ex4

def menu():
    op=0
    while op<1 or op>5:
        print("""
        Programa principal
        1.Llistes i numeros aleatoris
        2.Fitxers
        3.Joc
        4.Aplicacio que treballa amb objectes
        5.Sortir
        """)
        op = int(input("Introdueix una opcio: "))
        if op<1 or op>5:
            print("Opcio no valida, torni a elegir una opcio \n")
        else:
            return op





#Programa principal
op=1
while op!=5:
    op=menu()
    match(op):
        case 1:
            ex1.pex1()
        case 2:
            ex2.pex2()
        case 3:
            ex3.pex3()
        case 4:
            ex4.pex4()
        case 5:
            print("Gracies per emprar-me")
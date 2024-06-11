import random
# Función para generar una lista aleatoria de 3 números entre 1 y 9
def gllistaaletoria():
    l = []
    for i in range(3):
        l.append(random.randint(1, 9))
    return l

# Función para leer una lista de 3 números introducidos por el usuario
def llegir_llista():
    l = []
    for i in range(3):
        l.append(int(input("Introdueix el numero: ")))
    return l

# Función para comparar dos listas y proporcionar feedback
def comparar(l, m):
    a = [0, 0, 0]  # Inicializar la lista de resultados con ceros

    # Comparar los elementos de las dos listas
    for i in range(3):
        if l[i] == m[i]:  # Si el elemento está en la posición correcta
            a[i] = 10

    # Si todos los elementos están en la posición correcta
    if a[0] == 10 and a[1] == 10 and a[2] == 10:
        print("Enorabona, ho has encontrat tot!")
        return 0  # Indicar que se ha encontrado la solución correcta

    # Verificar si los elementos existen pero no están en la posición correcta
    for i in range(3):
        if a[i] != 10 and m[i] in l:
            a[i] = 5

    # Proporcionar feedback al usuario
    for i in range(3):
        if a[i] == 10:
            print("L'element {} es correcte".format(m[i]))
        elif a[i] == 5:
            print("L'element {} existeix, pero no esta al seu lloc".format(m[i]))
        else:
            print("L'element {} no existeix".format(m[i]))

# Función principal para ejecutar
def pex1():
    op = 1
    l = gllistaaletoria()  # Generar la lista aleatoria
    while op != 0:
        m = llegir_llista()  # Leer la lista del usuario
        op = comparar(l, m)  # Comparar las listas y obtener el feedback

# Ejecutar el juego si el archivo se ejecuta directamente
if __name__ == '__main__':
    pex1()
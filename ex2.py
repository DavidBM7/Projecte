def guardar_a_archivo(nom_archivo, contenido):
    with open(nom_archivo, 'a') as archivo:
        archivo.write(contenido + '\n')

def eliminar_archivo(nom_archivo):
    try:
        import os
        os.remove(nom_archivo)
        print(f"El archivo '{nom_archivo}' ha sido eliminado.")
    except FileNotFoundError:
        print(f"El archivo '{nom_archivo}' no existe.")

def mostrar_contenido(nom_archivo):
    try:
        with open(nom_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nom_archivo}' no existe.")

def pex2():
    nombre_archivo = 'mi_archivo.txt'

    while True:
        print("\n--- Menú ---")
        print("1. Añadir información")
        print("2. Eliminar archivo")
        print("3. Mostrar información")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            informacion = input("Introduce la información a añadir: ")
            guardar_a_archivo(nombre_archivo, informacion)
            print("Información añadida correctamente.")
        elif opcion == '2':
            eliminar_archivo(nombre_archivo)
        elif opcion == '3':
            mostrar_contenido(nombre_archivo)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    pex2()
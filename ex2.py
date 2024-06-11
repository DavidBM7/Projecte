# Función para guardar contenido en un archivo
def guardar_a_archivo(nom_archivo, contenido):
    # Abrimos el archivo en modo de append ('a') para añadir contenido al final del archivo
    with open(nom_archivo, 'a') as archivo:
        archivo.write(contenido + '\n')  # Escribimos el contenido en el archivo y añadimos un salto de línea

# Función para eliminar un archivo
def eliminar_archivo(nom_archivo):
    try:
        import os  # Importamos el módulo os para manejar operaciones del sistema
        os.remove(nom_archivo)  # Intentamos eliminar el archivo
        print(f"El archivo '{nom_archivo}' ha sido eliminado.")  # Confirmamos la eliminación del archivo
    except FileNotFoundError:
        print(f"El archivo '{nom_archivo}' no existe.")  # Mensaje si el archivo no se encuentra

# Función para mostrar el contenido de un archivo
def mostrar_contenido(nom_archivo):
    try:
        # Abrimos el archivo en modo de lectura ('r')
        with open(nom_archivo, 'r') as archivo:
            contenido = archivo.read()  # Leemos todo el contenido del archivo
            print("Contenido del archivo:")  # Mensaje de cabecera
            print(contenido)  # Imprimimos el contenido del archivo
    except FileNotFoundError:
        print(f"El archivo '{nom_archivo}' no existe.")  # Mensaje si el archivo no se encuentra

# Función principal que maneja el menú y las operaciones del usuario
def pex2():
    nombre_archivo = 'mi_archivo.txt'  # Nombre del archivo que vamos a manejar

    while True:
        # Mostramos el menú de opciones al usuario
        print("\n--- Menú ---")
        print("1. Añadir información")
        print("2. Eliminar archivo")
        print("3. Mostrar información")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")  # Leemos la opción seleccionada por el usuario

        if opcion == '1':
            informacion = input("Introduce la información a añadir: ")  # Pedimos la información a añadir
            guardar_a_archivo(nombre_archivo, informacion)  # Llamamos a la función para guardar la información
            print("Información añadida correctamente.")  # Confirmamos que se ha añadido la información
        elif opcion == '2':
            eliminar_archivo(nombre_archivo)  # Llamamos a la función para eliminar el archivo
        elif opcion == '3':
            mostrar_contenido(nombre_archivo)  # Llamamos a la función para mostrar el contenido del archivo
        elif opcion == '4':
            break  # Salimos del bucle y terminamos el programa
        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Mensaje de error para opción no válida

# Ejecutar la función principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    pex2()

#//importa librerias para manipular archivos pdf, zip, (imagenes en formato apple) y para manipular el sistema operativo
#//convierte cualquier imagen a formato jpg
#//crea un pdf con todos los archivos jpg que esten dentro del directorio datos dentro de donde se ejecuta el script

import os
import sys
import glob
import zipfile
import subprocess
import shutil
import img2pdf

#//define una funcion para convertir cualquier imagen a jpg
def convertir():
    #//define el directorio donde estan las imagenes
    os.chdir("datos")
    #//crea una lista con todos los archivos que esten en el directorio
    imagenes = glob.glob("*")
    #//recorre la lista de imagenes
    for imagen in imagenes:
        #//define el nombre del archivo con su extension
        nombre = imagen
        #//define el nombre del archivo sin su extension
        nombre_sin_extension = os.path.splitext(nombre)[0]
        #//define el nombre del archivo con la extension jpg
        nombre_jpg = nombre_sin_extension + ".jpg"
        #//define el comando para convertir la imagen a jpg
        comando = "sips -s format jpeg " + nombre + " --out " + nombre_jpg
        #//ejecuta el comando
        subprocess.call(comando, shell=True)
        #//elimina la imagen original
        os.remove(nombre)
    #//vuelve al directorio donde se ejecuta el script
    os.chdir("..")
    #//vuelve a ejecutar el menu
    main()
#//define una funcion para crear un pdf con todas las imagenes jpg que esten dentro del directorio "datos"
def pdf():
    #//pregunta al usuario la ubicacion del archivo pdf
    ubicacion = input("Ingrese la ubicacion del archivo pdf: ")
    os.chdir(ubicacion)
    #//crea una lista con todos los archivos que esten en el directorio
    imagenes = glob.glob("*.jpg")
    #//crea un archivo pdf con el nombre "imagenes.pdf"
    with open("imagenes.pdf", "wb") as f:
        #//crea el pdf con las imagenes jpg
        f.write(img2pdf.convert(imagenes))
    #//vuelve al directorio donde se ejecuta el script
    os.chdir("..")
    #//vuelve a ejecutar el menu
    main()
#//Define una funcion para poner una contraseña a un archivo pdf
def password():
    #//selecciona el archivo pdf recien creado y aplicale una contraseña
    os.chdir("datos")
    #//la contraseña la debe ingresar el usuario
    password = input("Ingrese la contraseña: ")
    #//confirma la contraseña
    password2 = input("Confirme la contraseña: ")
    #//si las contraseñas coinciden
    if password == password2:

        #//aplica la contraseña al archivo pdf
        comando = "qpdf --encrypt " + password + " " + password + " 128 -- " + "imagenes.pdf" + " " + "imagenes.pdf"
        #//ejecuta el comando
        subprocess.call(comando, shell=True)
        #//
        os.chdir("..")
        #//vuelve a ejecutar el menu
        main()
    else:
        print("Las contraseñas no coinciden")
        password()

#//crea la funcion principal del script con un menu para elegir que hacer
def main():
    #//limpia la pantalla
    os.system("clear")
    #//imprime el menu
    print("1. Convertir imagenes")
    print("2. Crear pdf")
    print("3. Aplicar contraseña")
    print("4. Salir")
    #//pide al usuario que ingrese una opcion
    opcion = input("Ingrese una opcion: ")
    #//si el usuario ingresa 1
    if opcion == "1":
        #//ejecuta la funcion convertir
        convertir()
    #//si el usuario ingresa 2
    elif opcion == "2":
        #//ejecuta la funcion pdf
        pdf()
    #//si el usuario ingresa 3
    elif opcion == "3":
        #//ejecuta la funcion password
        password()
    #//si el usuario ingresa 4
    elif opcion == "4":
        #//sale del script
        sys.exit()
    #//si el usuario ingresa otra opcion
    else:
        #//vuelve a ejecutar el menu
        main()
#//ejecuta la funcion principal
main()

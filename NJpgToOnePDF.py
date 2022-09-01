import os
import sys
import glob
import zipfile
import subprocess
import shutil
import img2pdf
def convertir():
    os.chdir("datos")
    imagenes = glob.glob("*")
    for imagen in imagenes:
        nombre = imagen
        nombre_sin_extension = os.path.splitext(nombre)[0]
        nombre_jpg = nombre_sin_extension + ".jpg"
        comando = "sips -s format jpeg " + nombre + " --out " + nombre_jpg
        subprocess.call(comando, shell=True)
        os.remove(nombre)
    os.chdir("..")
    main()
def pdf():
    ubicacion = input("Ingrese la ubicacion del archivo pdf: ")
    os.chdir(ubicacion)
    imagenes = glob.glob("*.jpg")
    with open("imagenes.pdf", "wb") as f:
        f.write(img2pdf.convert(imagenes))
    os.chdir("..")
    main()
def password():
    os.chdir("datos")
    password = input("Ingrese la contraseña: ")
    password2 = input("Confirme la contraseña: ")
    if password == password2:
        comando = "qpdf --encrypt " + password + " " + password + " 128 -- " + "imagenes.pdf" + " " + "imagenes.pdf"
        subprocess.Popen(comando)
        os.chdir("..")
        main()
    else:
        print("Las contraseñas no coinciden")
        password()
def main():
    os.system("clear")
    print("1. Convertir imagenes")
    print("2. Crear pdf")
    print("3. Aplicar contraseña")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        convertir()
    elif opcion == "2":
        pdf()
    elif opcion == "3":
        password()
    elif opcion == "4":
        sys.exit()
    else:
        main()
main()

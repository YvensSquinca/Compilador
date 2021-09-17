import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\Users\\SEUUSUARIO\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6" #Carrega as bibliotecas
os.environ['TK_LIBRARY'] = "C:\\Users\\SEUUSUARIO\\SEUUSUARIO\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6" #Alterar SEUUSUARIO, para o caminho de acordo com sua instalação

setup(
    name = "Programa", #Nome do Programa
    version = "1.0.0", #Versão
    options = {"build_exe":{
        'packages': ["os","sys","ctypes","win32con"],
        #Aqui incluimos nossos arquvios, como icones e imagens
        'include_files': ['C:\\Users\\SEUUSUARIO\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tcl86t.dll','C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tk86t.dll', #Essas 2 DLLs são importantes
        'transfer.png','transfer.ico','verde.png','vermelho.png','cinza.png'], #Alguns exemplos de Imagens e icones
        'include_msvcr': True,
        },
    },
    executables = [Executable("NomedoScript.py",base="Win32GUI",icon="NomedoIcone.ico")] #Nome do Script que sera compilado.
    )

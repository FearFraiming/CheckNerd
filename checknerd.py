#!/usr/bin/python
import os
import time
# Version
os.system("clear")
print ("\033[1;33mCREATED BY: CIA \033[0m")
os.system("cmatrix")
print ("")
## Show menu ##
print (30 * '-') 
print ("\033[1;32mGENERADOR DE BIN \033[0m") 
print (30 * '-')
print ("\033[1;32mFROM : CIA FOR : SENTINEL SOCIETY\033[0m")
print (30 * '-') 
print ("\033[1;33m1.\033[1;36mGenerar bin\033[0m") 
print ("\033[1;33m2.\033[1;36mGuardar bins en texto\033[0m") 
print ("\033[1;33m3.\033[1;36mGenerador de correo temporal\033[0m")
print ("\033[1;33m4.\033[1;36mBin Checker\033[0m")
print ("\033[1;33m5.\033[1;36mVer bin guardados\033[0m")
print ("\033[1;33m0.\033[1;31mBYE BITCH...!!\033[0m")
print (30 * '-')
 
## Get input ###
choice = raw_input('\033[1;33mingresa tu opcion cara de np: \033[0m')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Generador bin validos...") 
        os.system("python2 check.py")
        time.sleep(3)

elif choice == 2:
    os.system("clear")
    os.system("bash guardar")

elif choice == 3:
        os.system("clear")
        print("Ingresando al generador de correo temporal")
        print("Inicie una nueva ventana para usar el generador")
        print("para salir del navegador digite [ Q ] ")
        time.sleep(5)
        os.system("w3m https://temp-mail.org/es/")
elif choice == 4:
         os.system("python2 checker")
elif choice == 5:
         OS . sistema ( "cat Binguardados.txt" )
elif elección == 0:          
          salir ()
else: 
## default ##
        print ("Opcion invalida...Sigue intentando cara de Np")

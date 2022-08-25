import qrcode_terminal
import argparse
import hashlib
import struct
import hmac
import time
import re
import os

from cripto import Cripto as AES

"""

TAREA:
Crear un programa que permita registrar una clave inicial y genere una contraseña nueva cada vez que se solicite.
Puede utilizarse cualquier librería que no sea TOTP (es decir, que no haga el trabajo sucio).
"-g": recibe un fichero con una clave hexadecimal de 64 caracteres mínimo y la guarda en un fichero "ft_otp.key".
"-k": recibe un fichero cifrado (como "ft_otp.key") y genera una contraseña temporal, mostrándola por pantalla.
El fichero "ft_otp.key" siempre estará cifrado.

"""
# Leer los argumentos de entrada de la línea de comandos.
def leer_argumentos():
    # Inicializar el analizador de argumentos
    analizador = iniciar_analizador()

    return analizador.g, analizador.k, analizador.qr

#Inicializar el parser de la línea de comandos.
def iniciar_analizador():
    # Analizador de argumentos de la línea de comandos.
    analizador = argparse.ArgumentParser(


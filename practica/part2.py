#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Funciones

# Hace una pregunta Si/No
def mood():
    m = raw_input("¿Estás aburrido?\n")
    print vine(m)

# Devuelve una URL de Vine.
def vine(m):
    _m = m.lower()
    video = "Mira esto: https://vine.co/v/"
    if _m == "sí" or _m == 'si':
        return video + id(0)
    elif _m == "no":
        return video + id(1)
    else:
        return "Por favor, responde 'sí' or 'no'"

# Criptografía para ingenuos.
def id(n):
    token = "MgjaoO5j5jepuv6Ae52Sh2ps_WawMY602mFHjx703Llvwq_i3"
    if type(n) != int :
        # Nunca debería llegar aqui, pero igual tomé mis previciones.
        return "No tengo nada para ti."
    elif n == 0:
        m = max(36, 23, 33, 0.744, 47, 4.77, 2.2222222)
        v1 = token[19+9:m+n-8]
        return v1
    elif n == 1:
        m = min(4569,46.789,789.03, 9993.223, 5678239888, 8, 8.888, 32)
        v2 = token[m-3:m*2]
        return v2

# Ejecuta la función princial.
mood()
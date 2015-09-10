#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Listas y Diccionarios

def waiter():
    menu = ['pizza','hamburguesa', 'arepa']
    print "¿Qué te gustaría comer?"
    print "Tenemos %s, %s y %s" % (menu[0], menu[1], menu[2])
    opcion = raw_input("¿Qué te gustaría comer? \n").lower()
    if opcion == menu[0] or opcion == menu[1] or opcion == menu[2]:
        detalles(opcion)
    else:
        print "Esa opción no está disponible :("

def detalles(opcion):
    menu = {
        'pizza': ['Pizza Monaco', 'Pizza Caracas', 'Pizza Madrid'],
        'hamburguesa': ['Extra queso', 'Triple carne', 'Pollo Crocante'],
        'arepa': ['Lunes Temprano', 'Jueves de Noche', 'Sabado Tipo 6']
    }
    print "Tenemos las siguientes opciones de %s" % (opcion)
    for opc in menu[opcion]:
        print opc
    opcion_final = raw_input("¿Cuál le traemos?")
    preparar(opcion_final)

def preparar(opcion_final):
    ingredientes = ['tomates', 'cebollas moradas', 'chiles', 'queso azul', 'tocineta', 'chistorra', 'pesto holandes', 'hongos suizos', 'salsa persa', 'especias indias picantes']
    ingredientes.sort()
    n = 0
    for ing in ingredientes:
        n += 1
        print "%s. %s" % (n, ing)
    adicional = raw_input("¿Cuáles de estos ingredientes adicionales desea? (máximo 4, separados con coma) \n")
    extra = raw_input("¿Y le gustaría alguno que no está en el menú? ¿Nos dirías cual? La casa invita... \n")
    ingredientes.append(extra)
    print "¡Fabuloso!"
    print "En 35 minutos estará listo..."
    print "..."
    print "..."
    print "..."
    print "..."
    print "..."
    print "..."
    print "(35 minutos más tarde)"
    print "Acá está su cena:"
    print opcion_final
    print "Más " + ingredientes[len(ingredientes)-1]

waiter()
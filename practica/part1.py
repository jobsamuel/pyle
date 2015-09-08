#!/usr/bin/env python
# Condicionales

print "Hola tu..."
print "Ups, no me se tu nombre."
name = raw_input("¿Cuál es? \n")

if len(name) and name.isalpha():
    print "Mucho gusto %s!" % (name)
elif name.isalpha():
    print "Eso no es un nombre :("
else:
    print "¿Por qué no me dices tu nombre?"
    raw = raw_input("¿Ah? ¿por qué? \n")
    why = str(raw)
    if len(why):
        n = len(why)
        why_a = why.upper()
        why_b = why.lower()
        why_c = why[n -1] + why[n -1] + why[n -1]
        response = "%s %s %s... baaah" % (why_a, why_b, why_b + why_c)
        print response
    else:
        print "¬¬"
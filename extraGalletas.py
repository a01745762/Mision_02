# Autor: Brandon Julien Celaya Torres - A01745762
# Descripción: programa que calcula el número de ingredientes necesitados para "x" número de galletas.

# El programa inicia desde aquí.

galletasUsr = int(input("Introduce el número de galletas que quieres hacer: "))

azucar = (galletasUsr*1.5)/48
mantequilla = (galletasUsr*1)/48
harina = (galletasUsr*2.75)/48

print("""
          Para hacer %d galletas necesitas:
          Azúcar que necesitas: %.2f gramos
          Mantequilla que necesitas: %.2f gramos
          Harina que necesitas: %.2f gramos""" % (galletasUsr,azucar,mantequilla,harina))

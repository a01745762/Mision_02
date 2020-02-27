# Autor: Brandon Julien Celaya Torres
# Descripcion: Programa que calcula el IVA, la propina y el total de una cuenta en un restaurante.

# Escribe tu programa después de esta línea.

subtotal = int(input("Introduce la cantidad de tu consumo: "))

iva = (subtotal*0.16)
propina = (subtotal*0.13)
total = (subtotal+iva+propina)

print ("Costo de su comida: $%.2f" % (subtotal))
print ("""Propina: $%.2f
Iva : $%.2f
Total a pagar: $%.2f""" % (propina,iva,total))
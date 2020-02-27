# Autor: Brandon Julien Celaya Torres - A01745762
# Descripcion: Programa que calcule el número total de alumnos y el porcentaje de hombres y mujeres de acuerdo al número introducido por el usuario

# Escribe tu programa después de esta línea.

mujeres = int(input("Número de mujeres en la case: "))
hombres = int(input("Número de hombres en la clase: "))

total = mujeres+hombres
porcentajeMujeres = (mujeres*100)/total
porcentajeHombres = (hombres*100)/total

print (""" Mujeres inscritas %.1f
           Hombres inscritos %.1f
           Total inscritos: %.1f
           Porcentaje de mujeres: %.1f%%
           Porcentaje de hombres: %.1f%% """ % (mujeres,hombres,total,porcentajeMujeres,porcentajeHombres))
       
# Autor: Brandon Julien Celaya Torres
# Programa que pregunta la velocidad y calcula la distancia y el tiempo en diferentes circunstancias dadas. 

# Escribe tu programa después de esta línea.

velocidad = int(input("Introduce la velocidad en km/h: "))

t1 = 6
t2 = 3.5
d1 = 485

dt1 = velocidad*t1
dt2 = velocidad*t2
tt = d1/velocidad

print(""" Velocidad del auto en km/h: %.1f
          Distancia recorrida en 6 horas: %.1f kilómetros. 
          Distancia recorrida en 3.5 horas: %.1f kilómetros.
          Tiempo para recorrer 485 kilómetros: %.1f horas. """ % (velocidad, dt1, dt2, tt))

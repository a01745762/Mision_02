# Autor: Brandon Julien Celaya Torres - A01745762
# Descripción: Programa que calcula la distancia entre dos puntos, con base a las coordenadas que ponga el usuario

# Después de esta línea inicia el programa

x1 = int(input("Introduce la coordenada 'x' de tu primer punto: "))
y1 = int(input("Introduce la coordenada 'y' de tu primer punto: "))
x2 = int(input("Introduce la coordenada 'x' de tu segundo punto: "))
y2 = int(input("Introduce la coordenada 'y' de tu segundo punto: "))
d= (((x2-x1)**2) + ((y2-y1))**2)**0.5

print ("""
           x1: %d
           y1: %d
           x2: %d
           y2: %d
           distancia: %.3f """ % (x1,y1,x2,y2,d))


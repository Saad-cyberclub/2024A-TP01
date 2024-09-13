# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

import math
speed = 0
angle = 0
speed = float(input('Vitesse initiale (m/s): '))
angle = float(input('Angle de lancer (en degrés): '))


sin = (angle*3.14)/180
distance = ((speed**2)*(math.sin(sin*2)))/9.8

print ('Distance parcourue: ', round(distance , 2),'m' )

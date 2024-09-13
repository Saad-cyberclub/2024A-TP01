# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math
water_quantity = 0
water_quantity =float(input('Quelle quantité d\'eau faut-il assainir ? '))
filtre =  math.ceil(water_quantity/5)
lampes =math.ceil((water_quantity*3)/5)
chlore = (water_quantity*(1/2))/5
#print('Voici les éléments requis pour assainir ',water_quantity,'L d\'eau:') 
#print('               - Filtre(s) :', filtre)
#print('-\tLampe(s) UV :' , lampes,)
#print('-\tChlore :', chlore, 'kg')

a= f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:\n
        \t- Filtre(s) : {filtre}\n
        \t- Lampe(s) UV : {lampes}\n
        \t- Chlore : {chlore}kg\n"""
print(a)




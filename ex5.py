#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input('Pays concerné ? ')
code_medals = input('Chaine représentant les médailles ? ')
x=0
y=0
z=0
for i in (code_medals):
    if i=='G':
        x= x+1
    elif i=='S':
        y= y + 1
    elif i=='B':
        z= z+1
    else: 
        print('Veuillez entrer des lettres correctes')

print(country+':')
print('-',  x,'OR' )
print('-',  y,'Argent')
print('-', z,'Bronze')

print('Benvenuto al Programma "Capisci se è una vocale o no"');

def searchVocal():
  letter = input('Inserisci una lettera --> ')
  vocal = ('a','e','i','o','u');
  if letter in vocal:
    print('La lettera: ' + letter + ' è una vocale')
  else:
    print('La lettera: ' + letter + ' non è una vocale')
    
searchVocal()
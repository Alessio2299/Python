def isPalindroma():
  word = input('Inserisci la parola da analizzare --> ').lower()
  wordReverse = list(word)
  wordReverse.reverse()
  newWord = ''.join(wordReverse)

  if(newWord == word):
    print ('La parola ' + word + ' è palindroma')
  else:
    print ('La parola ' + word + ' non è palindroma')

isPalindroma()
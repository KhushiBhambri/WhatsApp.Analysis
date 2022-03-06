# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet
syns = wordnet.synsets("bad")
print(syns[0].lemmas())


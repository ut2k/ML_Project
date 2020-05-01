import nltk

brown = nltk.corpus.brown

corpus = [word.lower() for word in brown.words()]
print(corpus)

# Train on 95% f the corpus and test on the rest
spl = int(95*len(corpus)/100)
train = corpus[:spl]
test = corpus[spl:]

print("test:", test)
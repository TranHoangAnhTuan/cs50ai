import nltk
import string
corpus = nltk.corpus.brown

# Create a list of all words in the corpus
words = corpus.words()

# Create a set of unique words in the corpus
unique_words = set(words)

pos_tag = nltk.pos_tag(unique_words)
# print(pos_tag)

terminal = {}
set_of_pos = set()
for word in pos_tag:
    # if word[1]  in string.punctuation + " ''" + "``":
    #     continue
    set_of_pos.add(word[1])



# print(set_of_pos)

for pos in set_of_pos:
    terminal[pos] = set()

for word in pos_tag:
    terminal[word[1]].add(word[0])


print(terminal['DT'])




import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# download required resources

def extract_nouns(document):
    # example English text

    # tokenize the text into words
    words = word_tokenize(document)

    # identify the parts of speech for each word
    pos_tags = nltk.pos_tag(words)

    # extract the nouns
    nouns = [word for word, pos in pos_tags if (pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS') and len(word) > 1]
    # nouns = [word for word, pos in pos_tags if (pos == 'NN')]


    # print the list of nouns
    return nouns

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

# Import required libraries
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser

# Example text
sample_text = "The quick brown fox jumps over the lazy dog"

# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(sample_text))

#Extract all parts of speech from any text
chunker = RegexpParser("""
					NP: {<DT>?<JJ>*<NN>} #To extract Noun Phrases  
					P: {<IN>}			 #To extract Prepositions
					V: {<V.*>}			 #To extract Verbs
					PP: {

<p> <NP>}		 #To extract Prepositional Phrases
					VP: {<V> <NP|PP>*}	 #To extract Verb Phrases
					""")

# Print all parts of speech in above sentence
output = chunker.parse(tagged)
print("After Extracting\n", output)

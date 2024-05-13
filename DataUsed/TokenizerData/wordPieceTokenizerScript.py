from transformers import BertTokenizer
from collections import Counter
import csv

# Load the BERT-base-uncased tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Read the contents of a text file
with open('SMSSpamCollection.txt', 'r') as file:
    text = file.read()

# Get the subwords used for the text in the file
subwords = tokenizer.tokenize(text)

# Count the frequency of each subword
word_freq = Counter(subwords)

# Sort the subwords by frequency
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Write the results to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subword', 'Frequency'])
    for word, freq in sorted_words:
        writer.writerow([word, freq])

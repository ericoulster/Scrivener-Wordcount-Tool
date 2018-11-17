import os
import glob
import nltk
import re
import datetime
import csv

# determine project folter
project_folder = r'C:\Users\Eric\Desktop\Programming Files\Wordcount Tool\Word folder'

wordcount_record = r'C:\Users\Eric\Desktop\Programming Files\Wordcount Tool\Wordcount_records.csv'
# initialize list & Regex pattern
wordcount = []
r = re.compile(r'\w+')

# initialize time
now = datetime.datetime.now()

# loop grabs files
for filepath in glob.glob(os.path.join(project_folder, '*.txt')):
    # opens files in the loop
    with open(filepath, "r", encoding='utf8') as file:
        # reading files
        content = file.read()
        # tokenizing words, then filtering
        filetoken = nltk.word_tokenize(content)
        filetoken_filter = list(filter(r.match, filetoken))
        # getting 'length' of list (# of words) then appending to file
        wordcount_list = len(filetoken_filter)
        wordcount.append(wordcount_list)

# now for the easy part:

timeword_list = [now.strftime("%d-%m-%y"), sum(wordcount)] 

with open(wordcount_record, 'a', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(timeword_list)


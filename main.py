import markov
import parse
import scrape
import os

def author_freq(directory, length, punctuation):
    frequencies = dict()
    files = parse.process_folder(directory, punctuation)
    for file in files:
        temp = markov.markov(file, length)
        for t in temp.keys():
            if t not in frequencies:
                frequencies[t] = temp.get(t)
            else:
                frequencies[t].extend(temp.get(t))
    os.chdir("..")
    return frequencies

def merge_authors(authors):
    frequencies = dict()
    for author in authors:
        for a in author.keys():
            if a not in frequencies:
                frequencies[a] = author.get(a)
            else:
                frequencies[a].extend(author.get(a))
    return frequencies

def run():
    welcome()
    auth = input().split(',')
    lang = input("Enter your language (sorry these instructions are only available in English): ")
    '''for a in auth:
		print('Downloading ' + a.title())
		scrape.download(a,lang)'''
    directories = []
    for a in auth:
        temp = a.split()
        directories.append('_'.join(temp).title())
    i = 0
    length = int(input('Phrase length? (numbers only) (3 works well): '))
    punc = input('Keep punctuation? (y/n): ')
    if punc == 'y':
        punctuation = True
    elif punc == 'n':
        punctuation = False
    while i < len(directories):
        print("Calculating frequencies for " + directories[i].replace('_',' '))
        directories[i] = author_freq(directories[i], length, punctuation)
        i += 1
    m = merge_authors(directories)
    l = int(input("Sentence length? (numbers only): "))
    i = 0
    print(str(i) + ': ' + markov.chain(m, l, length))
    i += 1
    command = input('enter to continue, r to restart, q to quit' + '\n')
    while command != 'q':
        if command == 'r':
            print('under construction :(')
        else:
            print(str(i) + ': ' + markov.chain(m, l, length) + '\n')
            i += 1
            command = input('enter to continue, r to restart, q to quit' + '\n')

def welcome():
    print("Welcome to Markov Maker. Please enter your favorite authors, separated by ',':")
    print("(note that only public domain writers are available (works published before 1923))")
    print('If more than one author is entered, their works will be combined into a single markov chain')

run()

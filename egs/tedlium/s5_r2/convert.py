#!/usr/bin/python

f = open('data/local/dict_nosp/lexicon_words_orig.txt', 'r')
o = open('data/local/dict_nosp/lexicon_words.txt', 'w')
for line in f:
    new_line = line.split(' ');
    o.write(new_line[0])
    o.write(' ')
    for x in range(0, len(new_line[0]) - 1):
        letter = new_line[0][x]
        o.write(letter)
        o.write(' ')
    o.write(new_line[0][len(new_line[0]) - 1])
    o.write('\n')
o.close()
f.close()

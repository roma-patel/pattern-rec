import numpy as np
import scipy.stats as stats
import json
import sys
import re
#from suffix_tree import SuffixTree

annotypes = ['Participants', 'Intervention', 'Outcome']

def get_pos_single_file(xml_file):
    pos_finder = re.compile('(?<=<POS>).*(?=</POS>)')
    ner_finder = re.compile('(?<=<NER>).*(?=</NER>)')
    word_finder = re.compile('(?<=<word>).*(?=</word>)')
    begin_finder = re.compile('(?<=<CharacterOffsetBegin>).*(?=</CharacterOffsetBegin>)')
    end_finder = re.compile('(?<=<CharacterOffsetEnd>).*(?=</CharacterOffsetEnd>)')
    sent_id_finder = re.compile('(<sentence id=").*(")')

    pos_tags = []
    with open(xml_file) as f:
        for line in f.readlines():
            m = pos_finder.search(line)
            if m != None:
                pos = m.group(0).strip()
                pos_tags.append(pos)

    ner_tags = []
    with open(xml_file) as f:
        for line in f.readlines():
            m = ner_finder.search(line)
            if m != None:
                ner = m.group(0).strip()
                ner_tags.append(ner)
    words = []
    with open(xml_file) as f:
        for line in f.readlines():
            m = word_finder.search(line)
            if m != None:
                w = m.group(0).strip()
                words.append(w)

    begin = []
    with open(xml_file) as f:
        for line in f.readlines():
            m = begin_finder.search(line)
            if m != None:
                b = m.group(0).strip()
                begin.append(b)
    end = []
    with open(xml_file) as f:
        for line in f.readlines():
            m = end_finder.search(line)
            if m != None:
                e = m.group(0).strip()
                end.append(e)

    nsents = 0
    with open(xml_file) as f:
        for line in f.readlines():
            m = sent_id_finder.search(line)
            if m != None:
                nsents += 1

    return pos_tags, ner_tags, words, begin, end, nsents

def test():
    path = '/Users/romapatel/Desktop/PICO-data-master/'
    anno_path = path + 'annotations/PICO-annos-professional-union-word.json'
    '''f = open(anno_path, 'r')
    for line in f:
        gold_dict = json.loads(line)'''
    filepath = '/Users/romapatel/Desktop/stanford-corenlp/23114870.txt.xml'
    pos, ner, words, begin, end, nsents = get_pos_single_file(filepath)
      
if __name__ == '__main__':
    test()
    

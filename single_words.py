import nltk
import glob
import xml.etree.ElementTree as ET
import sys

def group(filepath, destination, pike):
    tree = ET.parse(filepath)
    root = tree.getroot()

    sentence = ""
    grouping_counter = 0
    group_word_counter = 0

    for child in root.iter():
        if child.tag == "{http://www.tei-c.org/ns/1.0}w":
            sentence += child.get("lemma")
            sentence += " "

    if len(sentence) > 0:
        if pike:
            sentence += " . "

        destination.write(sentence)

if len(sys.argv) < 3:
    print("missing arguments")
    sys.exit(1)

corpus = sys.argv[1]
actual_corpus = sys.argv[2]

open("./data/" + corpus + "_single_concat.txt", 'w').close()
destination_file1 = open("./data/" + corpus + "_single_concat.txt", "a+", encoding="utf8")
open("./data/" + corpus + "_single_concat_pike.txt", 'w').close()
destination_file2 = open("./data/" + corpus + "_single_concat_pike.txt", "a+", encoding="utf8")

for file in glob.iglob("./" + actual_corpus + "/*.xml"):
    group(file, destination_file1, False)
    group(file, destination_file2, True)
    print(file)

destination_file1.close()
destination_file2.close()

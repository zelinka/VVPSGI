import nltk
import glob
import xml.etree.ElementTree as ET


def group(filepath, destination):

    tree = ET.parse(filepath)
    root = tree.getroot()
    # print(root.findall("{http://www.tei-c.org/ns/1.0}text"))

    #i = 0
    # for child in root.iter(tag="{http://www.tei-c.org/ns/1.0}w"):

    sentence = ""
    grouping_counter = 0
    group_word_counter = 0
    # len(sentence) = 0

    for child in root.iter():

        if child.tag == "{http://www.tei-c.org/ns/1.0}w":
            # print(child.get("lemma"))

            sentence += child.get("lemma")
            sentence += " "

        #elif child.tag == "{http://www.tei-c.org/ns/1.0}s":
        
        #   if len(sentence) > 0:
        #        sentence += ". "

        
        
    if len(sentence) > 0:
        #sentence += " . "
        destination.write(sentence)
        #destination.write(("\n\n"))



destination_name = "gigafida_single_concat.txt"
open(destination_name, 'w').close()
destination_file = open(destination_name, "a+", encoding="utf8")

for file in glob.iglob('.\\ccGigafidaV1_0\\*.xml'):
    group(file, destination_file)
    print(file)

destination_file.close()


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

        elif child.tag == "{http://www.tei-c.org/ns/1.0}s":
        
            if len(sentence) > 0:
                sentence += ". "

        
        
    if len(sentence) > 0:
        #sentence += " . "
        destination.write(sentence)
        destination.write(("\n\n"))



#group('C:\\Users\\Tilen Zelinka\\Documents\\DIPLOMA\\cckresV1_0\\F0000018.xml')
open('.\\data\\cckres_single_concat_pike.txt', 'w').close()
destination_file = open('.\\data\\cckres_single_concat_pike.txt', "a+", encoding="utf8")

for file in glob.iglob('.\\cckresV1_0\\*.xml'):
    group(file, destination_file)
    print(file)

destination_file.close()

#ccres_location = "C:\\Users\\Tilen Zelinka\\Documents\\DIPLOMA\\cckresV1_0-text"
#txt_file = open(ccres_location + "\\F0000018.txt", encoding="utf8")
#txt_file = open("testni.txt", encoding="utf8")
#txt = txt_file.read()
#txt_file.close()

#tokens = nltk.word_tokenize(txt)
#print(txt)
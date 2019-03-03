import nltk
import glob
import xml.etree.ElementTree as ET


def fix_lone_grouping(groups):

    for charI in range(len(groups), 0, -1):
        #print(charI)
        if groups[charI-1] == " ":
            groups = groups[:charI-1] + " " + groups[charI:]
            break

    return groups


def group(filepath, destination):

    tree = ET.parse(filepath)
    root = tree.getroot()
    # print(root.findall("{http://www.tei-c.org/ns/1.0}text"))

    #i = 0
    # for child in root.iter(tag="{http://www.tei-c.org/ns/1.0}w"):

    sentence = ""
    shift_amount = 1
    grouping_counter = shift_amount
    group_word_counter = 0
    # len(sentence) = 0

    for child in root.iter():

        if child.tag == "{http://www.tei-c.org/ns/1.0}w":
            # print(child.get("lemma"))
            if len(sentence) > 0:
                if grouping_counter > 2:
                    grouping_counter = 0
                    sentence += " "
                elif sentence[len(sentence) - 1] != " ":
                    sentence += " "

            sentence += child.get("lemma")
            grouping_counter += 1
            group_word_counter += 1

            ''' VSAK ZNAK LOCI GRUPE

        elif child.tag == "{http://www.tei-c.org/ns/1.0}c":

            if grouping_counter == 1 and group_word_counter > 1:
                sentence = fix_lone_grouping(sentence)

            grouping_counter = 0
            group_word_counter = 0
            sentence += " " + child.text + " "

        elif child.tag == "{http://www.tei-c.org/ns/1.0}s":
            print(sentence)
            sentence = ""
            
            '''

            '''SAMO STAVKI LOCIJO GRUPE'''

        elif child.tag == "{http://www.tei-c.org/ns/1.0}s":

            if grouping_counter == 1 and group_word_counter > 0:
                sentence = fix_lone_grouping(sentence)

            grouping_counter = shift_amount
            group_word_counter = 0
            if len(sentence) > 0:
                sentence += " ."
                sentence += " "
                #print(sentence)
                destination.write(sentence)
            sentence = ""

            '''KONEC TEGA ZMEDENEGA SWITCHA'''

    if grouping_counter == 1 and group_word_counter > 1:
        sentence = fix_lone_grouping(sentence)

    if len(sentence) > 0:
        #print(sentence)
        sentence += " ."
        destination.write(sentence)
        #destination.write(("\n\n"))



#group('C:\\Users\\Tilen Zelinka\\Documents\\DIPLOMA\\cckresV1_0\\F0000018.xml')
open('.\\data\\cckres_singles_pike.txt', 'w').close()
destination_file = open('.\\data\\cckres_singles_pike.txt', "a+", encoding="utf8")


for file in glob.iglob('C:\\Users\\Tilen Zelinka\\Documents\\DIPLOMA\\cckresV1_0\\*.xml'):
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
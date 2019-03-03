parseme = []
VIDs = []

#1 prvotno, 2 lemma
word_type = 2

with open(".\\PARSEME\\SL\\train.cupt", encoding="utf8") as ins:

    for line in ins:
        
        if len(line) > 2:
            if line[0] != "#":
                parseme.append(line.split())

with open(".\\PARSEME\\SL\\test.cupt", encoding="utf8") as ins:

    for line in ins:
        
        if len(line) > 2:
            if line[0] != "#":
                parseme.append(line.split())


for i in range(len(parseme)):

    #check if word is at the start of a MWE
    if len(parseme[i][10]) > 1:

        marks = parseme[i][10].split(";")
        
        for mark in marks:

            category = mark.split(":")

            if len(category) > 1:

                if category[1] == "VID":

                    #print("nov match: ", i, category[0])

                    mwe_id = category[0]
                    buffer = ""

                    VID = parseme[i][word_type]
                    end_VID = False

                    for j in range(i+1, len(parseme)):

                        marks_j = parseme[j][10].split(";")

                        duplicate = False

                        for mark_j in marks_j:

                            if len(mark_j) == 1:

                                if mark_j == mwe_id and duplicate == False:
                                    VID += buffer + " " + parseme[j][word_type]
                                    buffer = ""
                                    duplicate = True
                                
                                elif mark_j == mwe_id and duplicate == True:
                                    VID += buffer
                                    buffer = ""

                                elif duplicate == False:
                                    buffer += "#*" + parseme[j][word_type]
                                    duplicate = True

                            else:
                                
                                category_j = mark_j.split(":")

                                #print(category_j, len(category_j))

                                if int(category_j[0]) == int(mwe_id):
                                    end_VID = True
                                    break

                                elif duplicate == False:

                                    buffer += " " + parseme[j][word_type]
                                    duplicate = True
                            
                        
                        if end_VID == True:
                            break

                    if "#*" not in VID:
                        VIDs.append(VID)

VIDs = sorted(VIDs)
VIDs = set(VIDs)

print(len(VIDs))

with open('parseme_VIDs_prunes.txt', 'w', encoding="utf8") as f:
    for item in VIDs:
        f.write("%s\n" % item)

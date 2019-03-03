from operator import itemgetter

VIDs = []

with open(".\\data\\parseme_VIDs.txt", encoding="utf8") as ins:

    for line in ins:
        VIDs.append(line.rstrip())


txt_f= open(".\\data\\gigafida_single_concat_pike.txt", encoding="utf8")
txt = txt_f.read()

#txt = txt[0:10000]

#print(txt.count("biti"))

VID_count = []

for VID in VIDs:
    txt = txt.replace(VID, VID.replace(" ", "_"))

txt_ls = txt.split()

with open(".\\gigafida_grouped_VIDs.txt", "w", encoding="utf8") as out:
    i=0
    while i < len(txt_ls)-5:
        
        i_increase = 1
        group = ""

        if "_" not in txt_ls[i] and txt_ls[i] != ".":

            if "_" not in txt_ls[i+1] and txt_ls[i+1] != ".":

                if "_" not in txt_ls[i+2] and txt_ls[i+2] != ".":

                    if "_" not in txt_ls[i+3] and txt_ls[i+3] != ".":

                        if "_" not in txt_ls[i+4] and txt_ls[i+4] != ".":

                            group = txt_ls[i] + "_" + txt_ls[i+1] + "_" + txt_ls[i+2] + " "
                            i_increase = 3

                        else:
                            group = txt_ls[i] + "_" + txt_ls[i+1] + " " + txt_ls[i+2] + "_" + txt_ls[i+3] + " "
                            i_increase = 4
                    else:
                        group = txt_ls[i] + "_" + txt_ls[i+1] + "_" + txt_ls[i+2] + " "
                        i_increase = 3
                else:
                   group = txt_ls[i] + "_" + txt_ls[i+1] + " "
                   i_increase = 2 
            else:
                group = txt_ls[i]

        elif "_" in txt_ls[i]:
        #else:
            group = txt_ls[i] + " "
        
        i+= i_increase

        out.write("%s" % group)
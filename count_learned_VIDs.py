from operator import itemgetter

VIDs = []

with open(".\\data\\parseme_VIDs_prunes.txt", encoding="utf8") as ins:

    for line in ins:
        VIDs.append(line.rstrip())


#txt_f= open(".\\data\\cckres_grouped_VIDs.txt", encoding="utf8")
txt_f= open(".\\vectors\\cckres_grouped_VIDs.vec", encoding="utf8")
txt = txt_f.read()

#print(txt.count("biti"))

VID_count = []

for VID in VIDs:
    tmp = []
    tmp.append(VID)
    VID = VID.replace(" ", "_") + " "
    tmp.append(txt.count(VID))
    VID_count.append(tmp)


VID_count = sorted(VID_count, key=itemgetter(1), reverse=True)

with open(".\\VID_count_vecs.txt", "w", encoding="utf8") as out:
    for item in VID_count:
        out.write("%s " % item[1])
        out.write("%s\n" % item[0])
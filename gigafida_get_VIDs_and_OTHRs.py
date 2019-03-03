import random

VIDs = []

with open(".\\data\\parseme_VIDs_prunes.txt", encoding="utf8") as ins:

    for line in ins:
        VIDs.append(line.rstrip())

VEC = []

with open(".\\vectors\\gigafida_grouped_VIDs.vec", encoding="utf8") as ins:
    for line in ins:
        VEC.append(line.split())

VID_vec = []

VID_wc = 0
OTHR_wc = 0

for VID in VIDs:

    VID = VID.replace(" ", "_")

    #print(VID)

    for line in VEC:
        if VID == line[0]:
            VID_vec.append(line)
            VID_wc += line[0].count("_")
            #print("neki")


OTHR_vec = []

while len(OTHR_vec) < len(VID_vec):

    v = random.choice(VEC)

    if v not in VID_vec and v not in OTHR_vec:
        OTHR_vec.append(v)
        OTHR_wc += v[0].count("_")


#print(VID_vec[0])
print(len(VID_vec))
print(VID_wc/len(VID_vec))
print(OTHR_wc/len(OTHR_vec))
#print(OTHR_vec[0])

with open(".\\gigafida_VIDs.vec", "w", encoding="utf8") as out:
    for item in VID_vec:
        #out.write("%s\n" % item)
        for e in item:
            out.write("%s " % e)
        out.write("\n")
    

with open(".\\gigafida_OTHRs.vec", "w", encoding="utf8") as out:
    for item in OTHR_vec:
        #out.write("%s\n" % item)
        for e in item:
            out.write("%s " % e)
        out.write("\n")
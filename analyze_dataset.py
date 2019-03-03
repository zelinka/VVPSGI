def analyze(lis):

    PosCount = 0
    NegCount = 0
    NonePos = 0
    NoneNeg = 0

    for i in range(len(lis)):
        
        if i < len(lis)/2:
            PosCount += lis[i].count("_") + 1
            NonePos += lis[i].count("None")
        else:
            NegCount += lis[i].count("_") + 1
            NoneNeg += lis[i].count("None")

    print("Positive:")
    print(len(lis), (len(lis)/2))
    print(PosCount/(len(lis)/2))
    print(NonePos)

    print("Negative:")
    print(NegCount/(len(lis)/2))
    print(NoneNeg)



cckres = []

with open(".\\data\\DATASET_cckres.csv", encoding="utf8") as ins:
    for line in ins:
        cckres.append(line)

gigafida = []

with open(".\\data\\DATASET_gigafida.csv", encoding="utf8") as ins:
    for line in ins:
        gigafida.append(line)

cckres.pop(0)
gigafida.pop(0)


analyze(cckres)
print()
analyze(gigafida)


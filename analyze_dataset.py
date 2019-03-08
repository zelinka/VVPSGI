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

f len(sys.argv) < 2:
    print("missing corpus argument")
    sys.exit(1)

corpus = sys.argv[1]
corp_list = []

with open("./data/DATASET_" + corpus + ".csv", encoding="utf8") as ins:
    for line in ins:
        corp_list.append(line)

corp_list.pop(0)

analyze(corp_list)


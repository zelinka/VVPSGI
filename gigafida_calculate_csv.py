from operator import add
from operator import itemgetter
from scipy import spatial
import numpy as np
import math

global_counter = 0

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
       return v
    return v / norm

def get_single_vectors(candidate, singles_array):

    singles = []
    for word in candidate:
        for single in singles_array:
            if single[0] == word:
                singles.append(single)

    return singles

def mag(x): 
    return math.sqrt(sum(i**2 for i in x))

def count_matches(t1, t2):

    matches = 0

    for i in range(len(t1)):
        if t1[i] == t2[i]:
            matches += 1

    return matches


def nearest3(vector, all_vectors, words):

    d1 = 3
    d2 = 3
    d3 = 3

    similar_counter = 0
    similar_dist_sum = 0

    for tmp in all_vectors:

        v = tmp.copy()
        v.pop(0)
        v = [float(i) for i in v]

        w = tmp[0].split("_")

        cos_dist= spatial.distance.cosine(vector, v)

        if(len(words) == len(w)):

            if(count_matches(words, w) == (len(words) - 1)):
                similar_counter += 1
                similar_dist_sum += cos_dist

        if cos_dist > 0:
            if cos_dist < d1:
                d3 = d2
                d2 = d1
                d1 = cos_dist

            elif cos_dist < d2:
                d3 = d2
                d2 = cos_dist
            
            elif cos_dist < d3:
                d3 = cos_dist


    avg_dist_to_similar = None
    global global_counter

    if similar_counter == 0:
        print("no similar groups")
        global_counter += 1
    else:
        avg_dist_to_similar = similar_dist_sum / similar_counter
        
    return d1, d2, d3, avg_dist_to_similar

VIDs = open(".\\vectors\\gigafida_VIDs.vec", encoding="utf8")
OTHRs =  open(".\\vectors\\gigafida_OTHRs.vec", encoding="utf8")

singles_vec = open(".\\vectors\\gigafida_single_concat.vec", encoding="utf8")

group_vec = open(".\\vectors\\gigafida_grouped_VIDs.vec", encoding="utf8")

#txt = singles_vec.read()
#print(txt)


grouped_array = []
singles_array = []
csv_array = []
grouped_array_all = []

with VIDs as ins:

    for line in ins:
        grouped_array.append(line.split())

with OTHRs as ins:

    for line in ins:
        grouped_array.append(line.split())

with singles_vec as ins:
    for line in ins:
        singles_array.append(line.split())

with group_vec as ins:
    for line in ins:
        grouped_array_all.append(line.split())

print("Finished loading arrays.\n")

#the first line contains information about .vec so we remove it
#grouped_array.pop(0)
singles_array.pop(0)


#print(float(grouped_array[0][1]) + float(grouped_array[0][2]))

progress_counter = 0
progress_max = len(grouped_array)

for group in grouped_array:

    #group = grouped_array[75304]

    candidate = group[0].split("_")

    if len(candidate) < 2:
        print("single word")
        progress_counter += 1
        continue


    singles = get_single_vectors(candidate, singles_array)

    if len(singles) > 1:

        vec_singles_sum = [0] * (len(singles[0])-1)



        for vec in singles:
            #gets rid of the word element, keeping only spatial data
            tmp = vec.copy()
            tmp.pop(0)
            #converts to float
            vec_tmp = [float(i) for i in tmp]

            vec_singles_sum = [sum(x) for x in zip(vec_singles_sum, vec_tmp)]

        #normalisation f vector
        #vec_singles_sum[:] = [x / element_sum for x in vec_singles_sum]
        #np_vec = np.asarray(vec_singles_sum)
        #vec_singles_sum = normalize(vec_singles_sum)
        #vec_singles_sum = vec_singles_sum.tolist()

        #getting the vector from group
        tmp = group.copy()
        tmp.pop(0)
        vec_group = [float(i) for i in tmp]

        #calculating attributes

        cos_dist_sum = spatial.distance.cosine(vec_group, vec_singles_sum)

        dot_prod_sum = sum([x*y for x,y in zip(vec_group, vec_singles_sum)])
        
        vec_sum_avg = [x/len(singles) for x in vec_singles_sum]

        mag_avg = mag(vec_sum_avg)
        mag_group = mag(vec_group)

        n1, n2, n3, similar_dist= nearest3(vec_group, grouped_array_all, candidate)

        group_type = 0
        if grouped_array.index(group) < len(grouped_array)/2:
            group_type = 1

        csv_array.append([group[0], mag_group, mag_avg, cos_dist_sum, dot_prod_sum, similar_dist, n1, n2, n3, group_type])

    progress_counter += 1
    print("Groups processed:", progress_counter, "/", progress_max, len(singles))



#print("Sorting...")
#orted_cos_array = sorted(cos_array, key=itemgetter(1))
#print(sorted_cos_array)

print("Global counter: ", global_counter)

with open('DATASET.csv', 'w', encoding="utf8") as f:
    f.write("Group,Mag Group,Mag Avg,CosDist Sum,DotProd Sum,CosDist Sim,N1,N2,N3,Type\n")
    for item in csv_array:

        for i in range(len(item)-1):
            f.write("%s," % item[i])

        f.write("%s\n" % item[len(item)-1])
        #print(item)



#beseda = singles[1]
#beseda.pop(0)
#print(beseda)


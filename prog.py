################################################################################################################
# This program was written for creating unique patterns from the  data sample of relatedness between parasitic #
# offspring and host mothers obtained by Ye Gong,  Kimball-Brain lab group, Biology Department, University of  #
# Florida}                                                                                                     #
#                                                                                                              #
# Copyright (C) {2014}  {Ambuj Kumar, Kimball-Brain lab group, Biology Department, University of Florida}      #
#                                                                                                              #
# This program is free software: you can redistribute it and/or modify                                         #
# it under the terms of the GNU General Public License as published by                                         #
# the Free Software Foundation, either version 3 of the License, or                                            #
# (at your option) any later version.                                                                          #
#                                                                                                              #
# This program is distributed in the hope that it will be useful,                                              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                                               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                #
# GNU General Public License for more details.                                                                 #
#                                                                                                              #
# This program comes with ABSOLUTELY NO WARRANTY;                                                              #
# This is free software, and you are welcome to redistribute it                                                #
# under certain conditions;                                                                                    #
#                                                                                                              #
################################################################################################################



import csv
import os
from itertools import product



def split_pattern(patterns, num):
    ret_list = list()
    for i in range(num):
        ret_list.append(patterns[i*1000:(i+1)*1000])

    return ret_list




dict_obj = dict()

with open("obj.csv", "r") as fp: # obj.csv is the data sample excell sheet
    reader = csv.DictReader(fp)
    for i, row in enumerate(reader):
        if row["female id(independant)"] + "_" + row["year(independent )"] not in dict_obj:
            dict_obj[row["female id(independant)"] + "_" + row["year(independent )"]] = dict()
                        
        dict_obj[row["female id(independant)"] + "_" + row["year(independent )"]][row["ful-sib group"] + "_" + str(i)] = (row["relatedness(independant)"], row["offspring number(dependant)"])

awsm_dict = dict()

whole_obj = list()

count = 1

for key, val in sorted(dict_obj.items()):

    store_obj = list()
    tup_obj = list()

    if len(set([x.split("_")[0] for x, inval in val.items()])) == 1:
        awsm_dict[key] = [tuple([x for x, inval in val.items()])]
    else:
        for i, inkey in enumerate(sorted(val)):
            if inkey.split("_")[0] in [x.split("_")[0] for x in tup_obj] or not tup_obj:
                tup_obj.append(inkey)
            else:
                store_obj.append(tup_obj)
                tup_obj = list()
                tup_obj.append(inkey)
                if i + 1 == len(val.items()):
                    store_obj.append(tup_obj)

        awsm_dict[key] = [tuple(x) for x in store_obj]

    inPat = tuple([x for x in product(*awsm_dict[key])][:2])
    count = count*len(inPat)

    whole_obj.append(inPat)




patterns = [x for x in product(*whole_obj)][0:10000]

def two_to_one(tup_obj):
    retList = list()
    for obj in tup_obj:
        for inObj in obj:
            retList.append(inObj)

    return retList

try:
    os.mkdir("excellData")
except:
    pass

for j, inPat in enumerate(patterns):
    shareList = two_to_one(inPat)
    with open("obj.csv", "r") as fp:
        with open("excellData/pattern" + str(j) + ".csv", "w") as fq:
            writer = csv.DictWriter(fq, fieldnames=row)
            writer.writeheader()
            reader = csv.DictReader(fp)
            for i, row in enumerate(reader):
                if row["ful-sib group"] + "_" + str(i) in shareList:
                    writer.writerow(row)



os.system("Rscript prog.r")










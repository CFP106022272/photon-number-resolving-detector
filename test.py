data_list=[]

with open("single_photon.txt", mode="r") as file:
    for line in file:
        if str(line[4:11]) == str("0000000"):
            0
        else:
            data_list.append(line)

#print(data_list)
with open("nonzero_data_1.txt", mode="w") as file:
    file.write(str(data_list))
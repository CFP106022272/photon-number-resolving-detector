data_list=[]
with open("test.txt", mode="r") as file:
    for line in file:
        if str(line[4:11]) == str("0000000"):
            0
        else:
            data_list.append(line)
            print(line[4:11])
#print(data_list)
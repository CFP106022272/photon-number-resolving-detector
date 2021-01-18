data_list=[]
channel_original_list=[]
channel_binary_list=[]
channel_list=[]
timedata_original_list=[]
timedata_list=[]
sweeps_original_list=[]
sweeps_list=[]

with open("nonzero_data_2.txt", mode="r") as file:
    for line in file:
        #data
        data=str(line)
        data_list.append(data)
        #print("data=", data)

        #channel_original(原始)
        channel_original=str(line[11])
        channel_original_list.append(channel_original)
        #print("channel_original=", channel_original)

        #channel_binary(二進位)
        c_b=bin(int(line[11], 16))
        channel_binary=str(c_b[2:6])
        channel_binary_list.append(channel_binary)
        #print("channel_binary=", channel_binary)

        #channel_decimal(十進位)
        channel=int(c_b[3:6], 2)
        channel_list.append(channel)
        #print("channel=", channel)

        #timedata_original
        timedata_original=str(line[4:11])
        timedata_original_list.append(timedata_original)
        #print("timedata_original=", timedata_original)

        #timedata_decimal
        timedata_decimal=int(line[4:11], 16)
        timedata_list.append(timedata_decimal)
        #print("timedata=", timedata_decimal)

        #sweeps_original
        sweeps_original=str(line[0:4])
        sweeps_original_list.append(sweeps_original)
        #print("sweeps_original=", sweeps_original)

        #sweeps_decimal
        sweeps_decimal=int(line[0:4], 16)
        sweeps_list.append(sweeps_decimal)
        #print("sweeps=", sweeps_decimal, "\n")

#print(sweeps_original_list)
#for i in range(len(data_list)):
    #print("\n",
        #"data=",data_list[i],"\n",
        #"channel_original=",channel_original_list[i],"\n",
        #"channel_binary=",channel_binary_list[i],"\n",
        #"channel=",channel_list[i],"\n",
        #"timedata_original=",timedata_original_list[i],"\n",
        #"timedata=",timedata_list[i],"\n",
        #"sweeps_original=",sweeps_original_list[i],"\n",
        #"sweeps=",sweeps_list[i],"\n"
    #)
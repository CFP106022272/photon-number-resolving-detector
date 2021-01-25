data_list=[]

with open("single_photon_2.txt", mode="r") as file:
    for line in file:
        if int(line, 16) == 000000000000:
            0
        else:
            data_list.append(line)

channel_original_list=[]
channel_binary_list=[]
channel_list=[]
timedata_original_list=[]
timedata_list=[]
sweeps_original_list=[]
sweeps_list=[]

for i in range(len(data_list)):
    data_number=str(data_list[i])

    #channel_original(原始)
    channel_original=str(data_number[11])
    channel_original_list.append(channel_original)

    #channel_binary(二進位)

    c_b=str(bin(int(data_number[11], 16)))
    channel_binary=str(c_b[2:6])
    if len(channel_binary) == 4:
        c_b_f=channel_binary
        channel_binary_list.append(c_b_f)
    elif len(channel_binary) == 3:
        c_b_f="0"+channel_binary
        channel_binary_list.append(c_b_f)
    elif len(channel_binary) == 2:
        c_b_f="00"+channel_binary
        channel_binary_list.append(c_b_f)
    else:
        c_b_f="000"+channel_binary
        channel_binary_list.append(c_b_f)

    #channel_decimal(十進位)
    channel=str(int(c_b_f[1:4], 2))
    channel_list.append(channel)

    #timedata_original
    timedata_original=str(data_number[4:11])
    timedata_original_list.append(timedata_original)

    #timedata_decimal
    timedata_decimal=str(int(data_number[4:11], 16))
    timedata_list.append(timedata_decimal)

    #sweeps_original
    sweeps_original=str(data_number[0:4])
    sweeps_original_list.append(sweeps_original)

    #sweeps_decimal
    sweeps_decimal=str(int(data_number[0:4], 16))
    sweeps_list.append(sweeps_decimal)


#Statistics
count1_list=[]
count2_list=[]
count3_list=[]
count4_list=[]
count5_list=[]
count6_list=[]
count_else_list=[]

different=[]

for i in range(len(sweeps_list)):
    if sweeps_list[i] != sweeps_list[i-1]:
        count1_list.append(1)
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] != sweeps_list[i-2]:
        count2_list.append(2)
        if channel_list[i] != channel_list[i-1]:
            print(i,"is different!")
            different.append("d")
        else:
            0#print("Same!")
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] != sweeps_list[i-3]:
        count3_list.append(3)
        if channel_list[i] == channel_list[i-1] and channel_list[i] == channel_list[i-2]:
            0#print("Same!")
        else:
            print(i,"is different!")
            different.append("d")
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] == sweeps_list[i-3] and sweeps_list[i] != sweeps_list[i-4]:
        count4_list.append(4)
        if channel_list[i] == channel_list[i-1] and channel_list[i] == channel_list[i-2] and channel_list[i] == channel_list[i-3]:
            0#print("Same!")
        else:
            print(i,"is different!")
            different.append("d")
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] == sweeps_list[i-3] and sweeps_list[i] == sweeps_list[i-4] and sweeps_list[i] != sweeps_list[i-5]:
        count5_list.append(5)
        if channel_list[i] == channel_list[i-1] and channel_list[i] == channel_list[i-2] and channel_list[i] == channel_list[i-3] and channel_list[i] == channel_list[i-4]:
            0#print("Same!")
        else:
            print(i,"is different!")
            different.append("d")
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] == sweeps_list[i-3] and sweeps_list[i] == sweeps_list[i-4] and sweeps_list[i] == sweeps_list[i-5] and sweeps_list[i] != sweeps_list[i-6]:
        count6_list.append(6)
        if channel_list[i] == channel_list[i-1] and channel_list[i] == channel_list[i-2] and channel_list[i] == channel_list[i-3] and channel_list[i] == channel_list[i-4] and channel_list[i] == channel_list[i-5]:
            0#print("Same!")
        else:
            print(i,"is different!")
            different.append("d")
    else:
        count_else_list.append(7)

print("There are", len(different), "different channel cases!")

count_else = len(count_else_list)
count6 = len(count6_list) - count_else
count5 = len(count5_list) - count6 - count_else
count4 = len(count4_list) - count5 - count6 - count_else
count3 = len(count3_list) - count4 - count5 - count6 - count_else
count2 = len(count2_list) - count3 - count4 - count5 - count6 - count_else
count1 = len(count1_list) - count2 - count3 - count4 - count5 - count6 - count_else

print("count1:",count1,"\n","count2:",count2,"\n","count3:",count3,"\n","count4:",count4,"\n","count5:",count5,"\n","count6:",count6,"\n","count_else:",count_else)

#plot bar graph
import numpy as np
import matplotlib.pyplot as plt

counts = np.array([1, 2, 3, 4, 5, 6])
accumulated_events = np.array([count1, count2, count3, count4, count5, count6])
plt.bar(counts, accumulated_events)

plt.title('Statistics')
plt.xlabel('counts')
plt.ylabel('accumulated_events')
for x, y in zip(counts, accumulated_events):
    plt.text(x, y, '%.0f' % y, ha='center', va= 'bottom',fontsize=11)
#plt.show()
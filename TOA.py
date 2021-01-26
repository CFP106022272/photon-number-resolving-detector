import numpy as np
import matplotlib.pyplot as plt

data_list=[]
APD1_data=[]
APD2_data=[]

with open("single_photon_3.mpa", mode="r") as file:
    for line in file:
        data_list.append(line)
#print(len(data_list))

APD1_data = list(map(int, data_list[158:16542]))
APD2_data = list(map(int, data_list[16543:32927]))

APD1 = np.array(APD1_data)
APD2 = np.array(APD2_data)
#print(APD2_data[-3])
time = np.linspace(0, 1638.3, 16384)

plt.title("TOA of Photons at APD1")
plt.xlabel("Time(ns)")
plt.ylabel("Number of Counts")
plt.plot(time, APD1)
plt.xlim([0, 1700])
plt.ylim([0, 27])
plt.show()

plt.title("TOA of Photons at APD2")
plt.xlabel("Time(ns)")
plt.ylabel("Number of Counts")
plt.xlim([0, 1700])
plt.plot(time, APD2)
plt.ylim([0, 33])
plt.show()

APD1_first_peak_value = max(APD1[0:5000])
APD1_first_peak_time = int([i for i, v in enumerate(APD1[0:5000]) if v == APD1_first_peak_value][0]) * 0.1
APD1_second_peak_value = max(APD1[5000:8000])
APD1_second_peak_time = int([i for i, v in enumerate(APD1[5000:8000]) if v == APD1_second_peak_value][0]) * 0.1 + 500
APD1_third_peak_value = max(APD1[8000:10000])
APD1_third_peak_time = int([i for i, v in enumerate(APD1[8000:10000]) if v == APD1_third_peak_value][0]) * 0.1 + 800
APD1_forth_peak_value = max(APD1[10000:14000])
APD1_forth_peak_time = int([i for i, v in enumerate(APD1[10000:14000]) if v == APD1_forth_peak_value][0]) * 0.1 + 1000

#tlist=[i for i, v in enumerate(APD1[10000:14000]) if v == APD1_forth_peak_value]

print(
    "APD1_first_peak_value:",APD1_first_peak_value,"\n",
    "APD1_first_peak_time:",APD1_first_peak_time,"ns\n",
    "APD1_second_peak_value:",APD1_second_peak_value,"\n",
    "APD1_second_peak_time:",APD1_second_peak_time,"ns\n",
    "APD1_third_peak_value:",APD1_third_peak_value,"\n",
    "APD1_third_peak_time:",APD1_third_peak_time,"ns\n",
    "APD1_forth_peak_value:",APD1_forth_peak_value,"\n",
    "APD1_forth_peak_time:",APD1_forth_peak_time,"ns\n",
    #tlist
)

APD2_first_peak_value = max(APD2[0:4000])
APD2_first_peak_time = int([i for i, v in enumerate(APD2[0:4000]) if v == APD2_first_peak_value][0]) * 0.1
APD2_second_peak_value = max(APD2[4000:6000])
APD2_second_peak_time = int([i for i, v in enumerate(APD2[4000:6000]) if v == APD2_second_peak_value][0]) * 0.1 + 400
APD2_third_peak_value = max(APD2[6000:10000])
APD2_third_peak_time_1 = int([i for i, v in enumerate(APD2[6000:10000]) if v == APD2_third_peak_value][0]) * 0.1 + 600
APD2_third_peak_value = max(APD2[6000:10000])
APD2_third_peak_time_2 = int([i for i, v in enumerate(APD2[6000:10000]) if v == APD2_third_peak_value][1]) * 0.1 + 600
APD2_forth_peak_value = max(APD2[10000:12000])
APD2_forth_peak_time = int([i for i, v in enumerate(APD2[10000:12000]) if v == APD2_forth_peak_value][0]) * 0.1 + 1000

#tlist=[i for i, v in enumerate(APD2[10000:12000]) if v == APD2_forth_peak_value]

print(
    "APD2_first_peak_value:",APD2_first_peak_value,"\n",
    "APD2_first_peak_time:",APD2_first_peak_time,"ns\n",
    "APD2_second_peak_value:",APD2_second_peak_value,"\n",
    "APD2_second_peak_time:",APD2_second_peak_time,"ns\n",
    "APD2_third_peak_value:",APD2_third_peak_value,"\n",
    "APD2_third_peak_time_1:",APD2_third_peak_time_1,"ns\n",
    "APD2_third_peak_time_2:",APD2_third_peak_time_2,"ns\n",
    "APD2_forth_peak_value:",APD2_forth_peak_value,"\n",
    "APD2_forth_peak_time:",APD2_forth_peak_time,"ns\n",
    #tlist
)

#wave packet area
APD1_area_1 = 0
APD1_area_2 = 0
APD1_area_3 = 0
APD1_area_4 = 0
for i in range(2654):
    APD1_area_1 = APD1_area_1 + int(APD1[int(i + APD1_second_peak_time * 10 + 2654 * (-1) - 1327)])
    APD1_area_2 = APD1_area_2 + int(APD1[int(i + APD1_second_peak_time * 10 + 2654 * 0 - 1327)])
    APD1_area_3 = APD1_area_3 + int(APD1[int(i + APD1_second_peak_time * 10 + 2654 * 1 - 1327)])
    APD1_area_4 = APD1_area_4 + int(APD1[int(i + APD1_second_peak_time * 10 + 2654 * 2 - 1327)])

print(
    "APD1_area_1:",APD1_area_1,"\n",
    "APD1_area_2:",APD1_area_2,"\n",
    "APD1_area_3:",APD1_area_3,"\n",
    "APD1_area_4:",APD1_area_4,"\n",
)

APD2_area_1 = 0
APD2_area_2 = 0
APD2_area_3 = 0
APD2_area_4 = 0
for i in range(2654):
    APD2_area_1 = APD2_area_1 + int(APD2[int(i + APD2_second_peak_time * 10 + 2654 * (-1) - 1327)])
    APD2_area_2 = APD2_area_2 + int(APD2[int(i + APD2_second_peak_time * 10 + 2654 * 0 - 1327)])
    APD2_area_3 = APD2_area_3 + int(APD2[int(i + APD2_second_peak_time * 10 + 2654 * 1 - 1327)])
    APD2_area_4 = APD2_area_4 + int(APD2[int(i + APD2_second_peak_time * 10 + 2654 * 2 - 1327)])

print(
    "APD2_area_1:",APD2_area_1,"\n",
    "APD2_area_2:",APD2_area_2,"\n",
    "APD2_area_3:",APD2_area_3,"\n",
    "APD2_area_4:",APD2_area_4,"\n",
)

#cut wave packet 1
var_area_1_1 = APD1_area_1
var_area_1_2 = APD1_area_2
var_area_1_3 = APD1_area_3
var_area_1_4 = APD1_area_4
i_1_1 = 0
i_1_2 = 0
i_1_3 = 0
i_1_4 = 0
while var_area_1_1 > (APD1_area_1 * 0.9):
    var_area_1_1 = var_area_1_1 - int(APD1[int(i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) - 1327)]) - int(APD1[int(- i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) + 1327)])
    i_1_1 = i_1_1 + 1
print(var_area_1_1)
#cut_APD1_area_1_start = int(i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) - 1327)
#cut_APD1_area_1_end = int(- i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) + 1327)

while var_area_1_2 > (APD1_area_2 * 0.9):
    var_area_1_2 = var_area_1_2 - int(APD1[int(i_1_2 + APD1_second_peak_time * 10 + 2654 * 0 - 1327)]) - int(APD1[int(- i_1_2 + APD1_second_peak_time * 10 + 2654 * 0 + 1327)])
    i_1_2 = i_1_2 + 1
print(var_area_1_2)

while var_area_1_3 > (APD1_area_3 * 0.9):
    var_area_1_3 = var_area_1_3 - int(APD1[int(i_1_3 + APD1_second_peak_time * 10 + 2654 * 1 - 1327)]) - int(APD1[int(- i_1_3 + APD1_second_peak_time * 10 + 2654 * 1 + 1327)])
    i_1_3 = i_1_3 + 1
print(var_area_1_3)

while var_area_1_4 > (APD1_area_4 * 0.9):
    var_area_1_4 = var_area_1_4 - int(APD1[int(i_1_4 + APD1_second_peak_time * 10 + 2654 * 2 - 1327)]) - int(APD1[int(- i_1_4 + APD1_second_peak_time * 10 + 2654 * 2 + 1327)])
    i_1_4 = i_1_4 + 1
print(var_area_1_4)

cut_APD1_area_1_start = int(i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) - 1327)
cut_APD1_area_1_end = int(- i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) + 1327)
cut_APD1_area_2_start = int(i_1_2 + APD1_second_peak_time * 10 + 2654 * 0 - 1327)
cut_APD1_area_2_end = int(- i_1_2 + APD1_second_peak_time * 10 + 2654 * 0 + 1327)
cut_APD1_area_3_start = int(i_1_3 + APD1_second_peak_time * 10 + 2654 * 1 - 1327)
cut_APD1_area_3_end = int(- i_1_3 + APD1_second_peak_time * 10 + 2654 * 1 + 1327)
cut_APD1_area_4_start = int(i_1_4 + APD1_second_peak_time * 10 + 2654 * 2 - 1327)
cut_APD1_area_4_end = int(- i_1_4 + APD1_second_peak_time * 10 + 2654 * 2 + 1327)

print(
    "cut_APD1_area_1:",cut_APD1_area_1_start / 10,"~",cut_APD1_area_1_end / 10,"ns\n",
    "cut_APD1_area_2:",cut_APD1_area_2_start / 10,"~",cut_APD1_area_2_end / 10,"ns\n",
    "cut_APD1_area_3:",cut_APD1_area_3_start / 10,"~",cut_APD1_area_3_end / 10,"ns\n",
    "cut_APD1_area_4:",cut_APD1_area_4_start / 10,"~",cut_APD1_area_4_end / 10,"ns\n"
)

#plot cutted wave packet
c_APD1 = APD1_data[cut_APD1_area_1_start:cut_APD1_area_1_end]
c_APD1.extend(APD1_data[cut_APD1_area_2_start:cut_APD1_area_2_end])
c_APD1.extend(APD1_data[cut_APD1_area_3_start:cut_APD1_area_3_end])
c_APD1.extend(APD1_data[cut_APD1_area_4_start:cut_APD1_area_4_end])
cut_APD1 = np.array(c_APD1)
c_time_1 = [x * 0.1 for x in range(cut_APD1_area_1_start, cut_APD1_area_1_end)]
c_time_1.extend([x * 0.1 for x in range(cut_APD1_area_2_start, cut_APD1_area_2_end)])
c_time_1.extend([x * 0.1 for x in range(cut_APD1_area_3_start, cut_APD1_area_3_end)])
c_time_1.extend([x * 0.1 for x in range(cut_APD1_area_4_start, cut_APD1_area_4_end)])
cut_time_1 = np.array(c_time_1)

plt.title("TOA of Photons at APD1(cutted wave packet)")
plt.xlabel("Time(ns)")
plt.ylabel("Number of Counts")
plt.plot(cut_time_1, cut_APD1)
plt.xlim([0, 1700])
plt.ylim([0, 27])
plt.show()

#cut wave packet 2
var_area_2_1 = APD2_area_1
var_area_2_2 = APD2_area_2
var_area_2_3 = APD2_area_3
var_area_2_4 = APD2_area_4
i_2_1 = 0
i_2_2 = 0
i_2_3 = 0
i_2_4 = 0
while var_area_2_1 > (APD2_area_1 * 0.9):
    var_area_2_1 = var_area_2_1 - int(APD2[int(i_2_1 + APD2_second_peak_time * 10 + 2654 * (-1) - 1327)]) - int(APD2[int(- i_2_1 + APD2_second_peak_time * 10 + 2654 * (-1) + 1327)])
    i_2_1 = i_2_1 + 1
print(var_area_2_1)
#cut_APD2_area_1_start = int(i_2_1 + APD2_second_peak_time * 10 + 2654 * (-1) - 1327)
#cut_APD2_area_1_end = int(- i_2_1 + APD2_second_peak_time * 10 + 2654 * (-1) + 1327)

while var_area_2_2 > (APD2_area_2 * 0.9):
    var_area_2_2 = var_area_2_2 - int(APD2[int(i_2_2 + APD2_second_peak_time * 10 + 2654 * 0 - 1327)]) - int(APD2[int(- i_2_2 + APD2_second_peak_time * 10 + 2654 * 0 + 1327)])
    i_2_2 = i_2_2 + 1
print(var_area_2_2)

while var_area_2_3 > (APD2_area_3 * 0.9):
    var_area_2_3 = var_area_2_3 - int(APD2[int(i_2_3 + APD2_second_peak_time * 10 + 2654 * 1 - 1327)]) - int(APD2[int(- i_2_3 + APD2_second_peak_time * 10 + 2654 * 1 + 1327)])
    i_2_3 = i_2_3 + 1
print(var_area_2_3)

while var_area_2_4 > (APD2_area_4 * 0.9):
    var_area_2_4 = var_area_2_4 - int(APD2[int(i_2_4 + APD2_second_peak_time * 10 + 2654 * 2 - 1327)]) - int(APD2[int(- i_1_4 + APD2_second_peak_time * 10 + 2654 * 2 + 1327)])
    i_2_4 = i_2_4 + 1
print(var_area_2_4)

cut_APD2_area_1_start = int(i_2_1 + APD2_second_peak_time * 10 + 2654 * (-1) - 1327)
cut_APD2_area_1_end = int(- i_2_1 + APD2_second_peak_time * 10 + 2654 * (-1) + 1327)
cut_APD2_area_2_start = int(i_2_2 + APD2_second_peak_time * 10 + 2654 * 0 - 1327)
cut_APD2_area_2_end = int(- i_2_2 + APD2_second_peak_time * 10 + 2654 * 0 + 1327)
cut_APD2_area_3_start = int(i_2_3 + APD2_second_peak_time * 10 + 2654 * 1 - 1327)
cut_APD2_area_3_end = int(- i_2_3 + APD2_second_peak_time * 10 + 2654 * 1 + 1327)
cut_APD2_area_4_start = int(i_2_4 + APD2_second_peak_time * 10 + 2654 * 2 - 1327)
cut_APD2_area_4_end = int(- i_2_4 + APD2_second_peak_time * 10 + 2654 * 2 + 1327)

print(
    "cut_APD2_area_1:",cut_APD2_area_1_start / 10,"~",cut_APD2_area_1_end / 10,"ns\n",
    "cut_APD2_area_2:",cut_APD2_area_2_start / 10,"~",cut_APD2_area_2_end / 10,"ns\n",
    "cut_APD2_area_3:",cut_APD2_area_3_start / 10,"~",cut_APD2_area_3_end / 10,"ns\n",
    "cut_APD2_area_4:",cut_APD2_area_4_start / 10,"~",cut_APD2_area_4_end / 10,"ns\n"
)

#plot cutted wave packet
c_APD2 = APD2_data[cut_APD2_area_1_start:cut_APD2_area_1_end]
c_APD2.extend(APD2_data[cut_APD2_area_2_start:cut_APD2_area_2_end])
c_APD2.extend(APD2_data[cut_APD2_area_3_start:cut_APD2_area_3_end])
c_APD2.extend(APD2_data[cut_APD2_area_4_start:cut_APD2_area_4_end])
cut_APD2 = np.array(c_APD2)
c_time_2 = [x * 0.1 for x in range(cut_APD2_area_1_start, cut_APD2_area_1_end)]
c_time_2.extend([x * 0.1 for x in range(cut_APD2_area_2_start, cut_APD2_area_2_end)])
c_time_2.extend([x * 0.1 for x in range(cut_APD2_area_3_start, cut_APD2_area_3_end)])
c_time_2.extend([x * 0.1 for x in range(cut_APD2_area_4_start, cut_APD2_area_4_end)])
cut_time_2 = np.array(c_time_2)

plt.title("TOA of Photons at APD2(cutted wave packet)")
plt.xlabel("Time(ns)")
plt.ylabel("Number of Counts")
plt.plot(cut_time_2, cut_APD2)
plt.xlim([0, 1700])
plt.ylim([0, 33])
plt.show()


#Statistics
data_list.clear()

with open("single_photon_3.txt", mode="r") as file:
    for line in file:
        if int(line, 16) == 000000000000:
            0
        elif str(line[11]) == str("9") and ( int(line[4:11], 16) < cut_APD1_area_1_start or ( int(line[4:11], 16) >= cut_APD1_area_1_end and int(line[4:11], 16) < cut_APD1_area_2_start) or ( int(line[4:11], 16) >= cut_APD1_area_2_end and int(line[4:11], 16) < cut_APD1_area_3_start) or ( int(line[4:11], 16) >= cut_APD1_area_3_end and int(line[4:11], 16) < cut_APD1_area_4_start) or int(line[4:11], 16) >= cut_APD1_area_4_end ):
            0
        elif str(line[11]) == str("2") and ( int(line[4:11], 16) < cut_APD2_area_1_start or ( int(line[4:11], 16) >= cut_APD2_area_1_end and int(line[4:11], 16) < cut_APD2_area_2_start) or ( int(line[4:11], 16) >= cut_APD2_area_2_end and int(line[4:11], 16) < cut_APD2_area_3_start) or ( int(line[4:11], 16) >= cut_APD2_area_3_end and int(line[4:11], 16) < cut_APD2_area_4_start) or int(line[4:11], 16) >= cut_APD2_area_4_end ):
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

#convert to excel
import openpyxl
from openpyxl import Workbook

excel_file=Workbook()
sheet=excel_file.active

sheet['A1']='DATA'
sheet['B1']='channel'
sheet['C1']=''
sheet['D1']=''
sheet['E1']='timedata'
sheet['F1']=''
sheet['G1']='sweeps'
sheet['H1']=''
for i in range(len(data_list)):
    columnA = data_list[i]
    columnB = channel_original_list[i]
    columnC = channel_binary_list[i]
    columnD = channel_list[i]
    columnE = timedata_original_list[i]
    columnF = timedata_list[i]
    columnG = sweeps_original_list[i]
    columnH = sweeps_list[i]
    sheet.append([columnA,columnB,columnC,columnD,columnE,columnF,columnG,columnH])

#excel_file.save('excel_data(test).xlsx')

#Statistics
count1_list=[]
count2_list=[]
count3_list=[]
count4_list=[]
count5_list=[]
count6_list=[]
count_else_list=[]

for i in range(len(sweeps_list)):
    if sweeps_list[i] != sweeps_list[i-1]:
        count1_list.append(1)
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] != sweeps_list[i-2]:
        count2_list.append(2)
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] != sweeps_list[i-3]:
        count3_list.append(3)
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] == sweeps_list[i-3] and sweeps_list[i] != sweeps_list[i-4]:
        count4_list.append(4)
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] == sweeps_list[i-3] and sweeps_list[i] == sweeps_list[i-4] and sweeps_list[i] != sweeps_list[i-5]:
        count5_list.append(5)
    elif sweeps_list[i] == sweeps_list[i-1] and sweeps_list[i] == sweeps_list[i-2] and sweeps_list[i] == sweeps_list[i-3] and sweeps_list[i] == sweeps_list[i-4] and sweeps_list[i] == sweeps_list[i-5] and sweeps_list[i] != sweeps_list[i-6]:
        count6_list.append(6)
    else:
        count_else_list.append(7)

count_else = len(count_else_list)
count6 = len(count6_list) - count_else
count5 = len(count5_list) - count6 - count_else
count4 = len(count4_list) - count5 - count6 - count_else
count3 = len(count3_list) - count4 - count5 - count6 - count_else
count2 = len(count2_list) - count3 - count4 - count5 - count6 - count_else
count1 = len(count1_list) - count2 - count3 - count4 - count5 - count6 - count_else

print("count1:",count1,"\n","count2:",count2,"\n","count3:",count3,"\n","count4:",count4,"\n","count5:",count5,"\n","count6:",count6,"\n","count_else:",count_else)

#plot bar graph
counts = np.array([1, 2, 3, 4, 5, 6])
accumulated_events = np.array([count1, count2, count3, count4, count5, count6])
plt.bar(counts, accumulated_events)

plt.title('Statistics\n(single_photon_3_cutted_wave_packet)')
plt.xlabel('counts')
plt.ylabel('accumulated_events')
for x, y in zip(counts, accumulated_events):
    plt.text(x, y, '%.0f' % y, ha='center', va= 'bottom',fontsize=11)
plt.show()
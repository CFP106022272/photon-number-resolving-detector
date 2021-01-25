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
#plt.show()

plt.title("TOA of Photons at APD2")
plt.xlabel("Time(ns)")
plt.ylabel("Number of Counts")
plt.xlim([0, 1700])
plt.plot(time, APD2)
plt.ylim([0, 33])
#plt.show()

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
cut_APD1_area_1_start = int(i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) - 1327)
cut_APD1_area_1_end = int(- i_1_1 + APD1_second_peak_time * 10 + 2654 * (-1) + 1327)

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
#plt.show()

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
cut_APD1_area_2_start = int(i_2_1 + APD1_second_peak_time * 10 + 2654 * (-1) - 1327)
cut_APD1_area_2_end = int(- i_2_1 + APD1_second_peak_time * 10 + 2654 * (-1) + 1327)

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
#plt.show()


#Statistics
data_list.clear()

with open("single_photon_3.txt", mode="r") as file:
    for line in file:
        if int(line, 16) == 000000000000:
            0
        else:
            data_list.append(line)


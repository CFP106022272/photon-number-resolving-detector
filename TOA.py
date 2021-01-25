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
plt.plot(time, APD2)
plt.xlim([0, 1700])
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

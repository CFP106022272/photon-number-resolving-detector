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
plt.plot(time, APD2)
plt.xlim([0, 1700])
plt.ylim([0, 33])
plt.show()

#for i in range():#
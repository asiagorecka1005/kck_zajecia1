import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag
dane = pd.read_csv(r"sub-01_trial-07.csv", delimiter=',', engine='python')
sygnal=dane['2']
liczby=dane['6']
t = np.linspace (0, 113.165, 200*113.165)

plt.subplot(2, 1, 1)
plt.plot(t, sygnal)
plt.xlim([0, 35])
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.title("Ryc. 1.1. Sygnał przed filtracją")

przefiltrowany=ag.pasmowozaporowy(sygnal, 200, 49, 51)
przefiltrowany2=ag.pasmowoprzepustowy(przefiltrowany, 200, 1, 50)
plt.subplot(2, 1, 2)
plt.plot(t,przefiltrowany2)
plt.xlim([0, 35])
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.title("Ryc. 1.2. Sygnał przefiltrowany")
plt.show()

plt.plot(t,liczby)
plt.xlim([0, 35])
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

tab=[]
j=0
for i in range(len(sygnal)):
    if przefiltrowany2[i]>0.3:
        j+=1
        if j==1:
            tab.append(liczby[i])
    else:
        j=0
print(tab)

import os
import numpy as np
import matplotlib.pyplot as plt

os.system("g++ marcha_aleatoria.cpp -o marcha.x"
os.system("./marcha.x > datos.dat")

data = np.loadtxt("datos.dat")
          
plt.figure()          
plt.plot(data[:,0], data[:,1])
plt.savefig("caminata.png")
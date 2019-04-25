import numpy as np
import matplotlib.pyplot as plt



data1 = np.loadtxt("euler.dat")
data2 = np.loadtxt("leapfrog.dat")
data3 = np.loadtxt("rk4.dat")
plt.figure()
plt.plot(data1[:,0],data1[:,1])
plt.savefig("graficas1.png")
plt.figure()
plt.plot(data1[:,0],data1[:,1])
plt.savefig("graficas2.png")
plt.figure()
plt.plot(data1[:,0],data1[:,1])
plt.savefig("graficas3.png")

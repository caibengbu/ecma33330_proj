from matplotlib import pyplot as plt
import numpy as np

for handle in ["ei","eu","ui","ue","iu","ie"]:
    data = np.loadtxt(handle + ".dat")
    plt.plot(data[:,0],data[:,1],label=handle)
    plt.savefig(handle+".png")
    plt.close()


from matplotlib import pyplot as plt
import numpy as np

# Plot the transition probability (Fig. 4)
for handle in ["ei","eu","ui","ue","iu","ie"]:
    data = np.loadtxt(handle + ".dat")
    plt.plot(data[:,0],data[:,1],label=handle)
    plt.savefig("trans_prob"+handle+".png")
    plt.close()

# Plot the hypothetical unemployment rate (Fig. 5)
for handle in ["ei","eu","ui","ue","iu","ie"]:
    data = np.loadtxt("urate_" + handle + ".dat")
    plt.plot(data[:,0],data[:,1],label=handle)
    plt.savefig("hypo_unemp_"+handle+".png")
    plt.close()

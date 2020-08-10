import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from recan.simgen import Simgen
from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure(figsize=(15,25))

plt.subplot(3, 1, 1)

sim_obj = Simgen("A.fasta")
sim_obj.get_info()
sim_obj.simgen(window=200, shift=50, pot_rec=1)
sim_obj.simgen(window=200, shift=50, pot_rec=1, region=(1000, 2700))
df=sim_obj.get_data()
sns.set()

#Distance Plot

plt.plot(df.loc["YSkhOWsugj", : ], lw=7, alpha=0.7, label="YSkhOWsugj",color="green" )
plt.plot(df.loc["vfAd9SUTn8", : ], lw=7, alpha=0.7, label="vfAd9SUTn8",color="red")

plt.ylim(0.6, 1.05)
plt.title("Similarity Distance Plot", fontsize=30,color="blue")
plt.ylabel("distance relative to 3ShGv2Rptp", fontsize=16)
plt.xlabel("nucleotide position", fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.axvline(1400, alpha=0.5, color="blue", lw=3,
            linestyle="dashed", label="putative recombination break points")
plt.axvline(2250, alpha=0.5, color="blue", lw=3,
            linestyle="dashed"  )

plt.legend(prop={"size":16})




plt.subplot(3, 1, 2)
sim_obj = Simgen("B.fasta") 


sim_obj.get_info()
sim_obj.simgen(window=200, shift=50, pot_rec=1)
sim_obj.simgen(window=200, shift=50, pot_rec=1, region=(1000, 2700))
df=sim_obj.get_data()
sns.set()

#Distance Plot

plt.plot(df.loc["HgvUN23ZJr", : ], lw=7, alpha=0.7, label="HgvUN23ZJr",color="Yellow" )
plt.plot(df.loc["NmTPPAOnrn", : ], lw=7, alpha=0.7, label="NmTPPAOnrn",color="red")

plt.ylim(0.85, 1.05)
plt.title("Similarity Distance Plot", fontsize=30,color="blue")
plt.ylabel("distance relative to ksLStixJOQ", fontsize=16)
plt.xlabel("nucleotide position", fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.axvline(2400, alpha=0.5, color="blue", lw=3,
            linestyle="dashed", label="putative recombination break points")
plt.axvline(2600, alpha=0.5, color="blue", lw=3,
            linestyle="dashed"  )

plt.legend(prop={"size":16})


plt.subplot(3, 1, 3)
sim_obj = Simgen("C.fasta") 


sim_obj.get_info()
sim_obj.simgen(window=200, shift=50, pot_rec=1)
sim_obj.simgen(window=200, shift=50, pot_rec=1, region=(1000, 2700))
df=sim_obj.get_data()
sns.set()

#Distance Plot


plt.plot(df.loc["uCqmN7ES8c", : ], lw=7, alpha=0.7, label="uCqmN7ES8c",color="black" )
plt.plot(df.loc["m5vT1gLP3H", : ], lw=7, alpha=0.7, label="m5vT1gLP3H",color="red")
plt.ylim(0.8, 1.05)
plt.ylabel("distance relative to pqPNGFPyp1", fontsize=23)
plt.xlabel("nucleotide position", fontsize=23)
plt.xticks(fontsize=23)
plt.yticks(fontsize=23)

plt.axvline(2350, alpha=0.5, color="blue", lw=3,
            linestyle="dashed", label="putative recombination break points")
plt.axvline(1800, alpha=0.5, color="blue", lw=3,
            linestyle="dashed"  )

plt.legend(prop={"size":16})

plt.savefig("hiv_plots.png")

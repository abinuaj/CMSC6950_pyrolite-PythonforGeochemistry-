import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from recan.simgen import Simgen
from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure(figsize=(15,25))

plt.subplot(3, 1, 1)


sim_obj = Simgen("AB.fasta")

sim_obj.get_info()
sim_obj.simgen(window=200, shift=50, pot_rec=1)
sim_obj.simgen(window=200, shift=50, pot_rec=1, region=(1000, 2700))
df=sim_obj.get_data()
sns.set()

#Distance Plot


plt.plot(df.loc["jLGh8X9dvG", : ], lw=7, alpha=0.7, label="jLGh8X9dvG",color="green" )
plt.plot(df.loc["yCW9kOaJDM", : ], lw=7, alpha=0.7, label="yCW9kOaJDM",color="blue")

plt.ylim(0.1, 1.05)
plt.title("Similarity Distance Plot Noro Virus", fontsize=45,color="blue")
plt.ylabel("distance relative to o5YOw4qGRu", fontsize=23)
plt.xlabel("nucleotide position", fontsize=23)
plt.xticks(fontsize=23)
plt.yticks(fontsize=23)

plt.axvline(2680, alpha=0.5, color="red", lw=3,
            linestyle="dashed", label="putative recombination break points")
plt.axvline(2680, alpha=0.5, color="red", lw=3,
            linestyle="dashed"  )

plt.legend(prop={"size":16})

plt.subplot(3, 1, 2)
sim_obj = Simgen("AC.fasta")


sim_obj.get_info()
sim_obj.simgen(window=200, shift=50, pot_rec=1)
sim_obj.simgen(window=200, shift=50, pot_rec=1, region=(1000, 2700))
df=sim_obj.get_data()
sns.set()

#Distance Plot


plt.plot(df.loc["nBofwH0aft", : ], lw=7, alpha=0.7, label="nBofwH0aft",color="purple" )
plt.plot(df.loc["0RyndCwtev", : ], lw=7, alpha=0.7, label="0RyndCwtev",color="yellow")

plt.ylim(0.45, 1.05)
plt.ylabel("distance relative to wAMfw3aaL4", fontsize=23)
plt.xlabel("nucleotide position", fontsize=23)
plt.xticks(fontsize=23)
plt.yticks(fontsize=23)

plt.axvline(1800, alpha=0.5, color="red", lw=3,
            linestyle="dashed", label="putative recombination break points")
plt.axvline(2200, alpha=0.5, color="red", lw=3,
            linestyle="dashed"  )

plt.legend(prop={"size":16})



plt.subplot(3, 1, 3)
sim_obj = Simgen("AD.fasta")


sim_obj.get_info()
sim_obj.simgen(window=200, shift=50, pot_rec=1)
sim_obj.simgen(window=200, shift=50, pot_rec=1, region=(1000, 2700))
df=sim_obj.get_data()
sns.set()

#Distance Plot


plt.plot(df.loc["ZQx4c1evcI", : ], lw=7, alpha=0.7, label="ZQx4c1evcI",color="black" )
plt.plot(df.loc["xRWUnyxboP", : ], lw=7, alpha=0.7, label="xRWUnyxboP",color="red")

plt.ylim(0.85, 1.05)
plt.ylabel("distance relative to uRrupY6iyi", fontsize=20)
plt.xlabel("nucleotide position", fontsize=20)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.axvline(1380, alpha=0.8, color="red", lw=3,
            linestyle="dashed", label="putative recombination break points")
plt.axvline(1450, alpha=0.5, color="red", lw=3,
            linestyle="dashed"  )

plt.legend(prop={"size":16})


plt.savefig("noro_plots.png")


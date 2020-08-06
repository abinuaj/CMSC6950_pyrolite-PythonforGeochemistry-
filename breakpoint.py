from recan.simgen import Simgen
from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns

sim_obj = Simgen("lumpy.fasta") 


sim_obj.get_info()
sim_obj.simgen(window=200, shift=50, pot_rec=1)
sim_obj.simgen(window=200, shift=50, pot_rec=1, region=(1000, 2700))
df=sim_obj.get_data()
sns.set()

#Distance Plot

plt.figure(figsize=(12, 6))
plt.plot(df.loc["AF409138.1_Lumpy_skin_disease_virus_iso", : ], lw=7, alpha=0.7, label="AF409138.1_Lumpy_skin_disease_virus_iso",color="green" )
plt.plot(df.loc["contig_assembly_2", : ], lw=7, alpha=0.7, label="contig_assembly_2",color="yellow")

plt.ylim(0.85, 1.05)
plt.title("Similarity Distance Plot", fontsize=30,color="blue")
plt.ylabel("distance relative to Ba", fontsize=20)
plt.xlabel("nucleotide position", fontsize=20)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.axvline(1500, alpha=0.5, color="red", lw=3,
            linestyle="dashed", label="putative recombination break points")
plt.axvline(1800, alpha=0.5, color="red", lw=3,
            linestyle="dashed"  )

plt.legend(prop={"size":14})
plt.savefig("distance_plot.png")





import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.SeqUtils import GC 
gc = sorted(GC(rec.seq) for rec in SeqIO.parse("BCRA1.fasta", "fasta"))
plt.xlabel("Genes")
plt.ylabel("GC Percentage")
plt.grid()
plt.plot(gc)
plt.savefig("gcplot.png")


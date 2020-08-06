#Line Plot
import matplotlib.pyplot as plt
from Bio import SeqIO

records = [len(rec) for rec in SeqIO.parse("BCRA1.fasta", "fasta")]
plt.xlabel("sequence length",fontsize=16)
plt.ylabel("count",fontsize=16)
plt.grid()
plt.plot(records,color="green")
plt.savefig("line_plot")




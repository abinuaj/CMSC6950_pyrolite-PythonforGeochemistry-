#Line Plot
import matplotlib.pyplot as plt
from Bio import SeqIO

records = [len(rec) for rec in SeqIO.parse("fasta.fasta", "fasta")]
plt.xlabel("sequence length",fontsize=20)
plt.ylabel("count",fontsize=20)
plt.plot(records,color="green")
plt.savefig("line_plot")




import matplotlib.pyplot as plt
from Bio import SeqIO

records = [len(rec) for rec in SeqIO.parse("BCRA1.fasta", "fasta")]


plt.hist(records,bins=12)
plt.xlabel("sequence length",fontsize=16)
plt.ylabel("count",fontsize=16)
plt.savefig("hist.png")



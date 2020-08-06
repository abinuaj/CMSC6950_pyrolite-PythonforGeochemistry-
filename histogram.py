import matplotlib.pyplot as plt
from Bio import SeqIO

records = [len(rec) for rec in SeqIO.parse("fasta.fasta", "fasta")]


plt.hist(records,bins=5)

plt.savefig("hist.png")



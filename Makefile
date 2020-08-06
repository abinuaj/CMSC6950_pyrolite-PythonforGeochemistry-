report.pdf:report.tex line_plot.png distance_plot.png gcplot.png hist.png 
	latexmk -pdf


line_plot.png:BCRA1.fasta lineplot.py
	python lineplot.py

distance_plot.png:lumky.fasta breakpoint.py
	python breakpoint.py

gcplot.png:BCRA1.fasta gcplot.py
	python gcplot.py

hist.png:BCRA1.fasta histogram.py
	python histogram.py

lumky.fasta :
	./makedata

BCRA1:
	./makedata2
.PHONY: clean almost_clean

clean:almost_clean
	rm BCRA1.fasta
	rm lumpy.fasta
	rm report.pdf
	rm line_plot.png
	rm distance_plot.png
	rm gcplot.png
	rm hist.png
	rm report.aux
	rm report.fdb_latexmk
	rm report.fls
	rm report.out
	rm report.log
	rm report.bbl
	rm report.blg
	

almost_clean:
	latexmk -c



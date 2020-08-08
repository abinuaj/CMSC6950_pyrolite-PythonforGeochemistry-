report.pdf:report.tex line_plot.png distance_plot.png gcplot.png hist.png hiv_plot.png noro_plot.png 
	latexmk -pdf

hiv_plot.png:
	python hiv_distanceplots.py

noro_plot.png:
	python noro_distanceplot.py

line_plot.png:BCRA1.fasta lineplot.py
	python lineplot.py

gcplot.png:BCRA1.fasta gcplot.py
	python gcplot.py

hist.png:BCRA1.fasta histogram.py
	python histogram.py

distance_plot.png:lumky.fasta breakpoint.py
	python breakpoint.py

A.fasta B.fasta C.fasta AB.fasta AC.fasta AD.fasta lumky.fasta BCRA1.fasta :
	
	./makedata

.PHONY: clean almost_clean

clean:almost_clean
	rm -f *.png
	rm -f *.fasta	
	rm -f report.pdf
	rm -f *.zip
	rm -f *.bbl
almost_clean:
	latexmk -c

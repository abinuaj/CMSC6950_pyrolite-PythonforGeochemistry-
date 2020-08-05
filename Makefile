report.pdf:report.tex myplot.png
	latexmk -pdf

myplot.png:data.txt myplot.py
	python myplot.py

data.txt:
	./makedata.py

.PHONY: clean almost_clean

clean:almost_clean
	rm report.pdf
	rm ternary.png
	rm lognormal.png
	rm report.aux
	rm report.fdb_latexmk
	rm report.fls
	rm report.out
	rm report.log

almost_clean:
	latexmk -c



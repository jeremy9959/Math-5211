mdfiles := $(wildcard *.md)
pdffiles := $(patsubst %.md,pdfs/%.pdf,$(mdfiles))

all : $(pdffiles)

pdfs/%.pdf : %.md
	pandoc --standalone --mathjax -V header-includes="\\usepackage[all]{xy}" -V include-before="\\input macros.tex" $< -o $@

mdfiles := $(wildcard *.md)
pdffiles := $(patsubst %.md,pdfs/%.pdf,$(mdfiles))
slidefiles := $(patsubst %.md, slides/%.html, $(mdfiles))
beamerfiles := $(patsubst %.md, beamer/%.pdf, $(mdfiles))
all : pdfs slides beamer

pdfs : $(pdffiles)

slides : $(slidefiles)

beamer: $(beamerfiles)

beamer/%.pdf : %.md
	pandoc --standalone --mathjax -t beamer $< -o $@

slides/%.html : %.md
	head -n -3 $< | pandoc --standalone --mathjax  -t slidy -f markdown -o $@

pdfs/%.pdf : %.md
	pandoc --standalone --mathjax -V header-includes="\\usepackage[all]{xy}" -V include-before="\\input macros.tex" $< -o $@
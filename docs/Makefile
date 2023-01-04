mdfiles := $(wildcard *.md)
pdffiles := $(patsubst %.md,pdfs/%.pdf,$(mdfiles))
slidefiles := $(patsubst %.md, slides/%.html, $(mdfiles))
beamerfiles := $(patsubst %.md, beamer/%.pdf, $(mdfiles))
all : pdfs slides beamer

pdfs : $(pdffiles)

slides : $(slidefiles)

beamer: $(beamerfiles)

beamer/%.pdf : %.md
	head -n -3 $< | pandoc --standalone --mathjax --slide-level=3 -V header-includes="\\usepackage[all]{xy}" -V header-includes="\\input macros.tex" -t beamer -f markdown -o $@


pdfs/%.pdf : %.md
	pandoc --standalone --mathjax -V header-includes="\\usepackage[all]{xy}"  -V header-includes="\\input macros.tex" $< -o $@
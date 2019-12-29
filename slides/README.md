# Slides

## Building the slides

You should have pdflatex installed it should include packages like `beamer`, `minted`, and `tikz`. These were all available when I did a full tex install on ubuntu.

```shell
pdflatex -shell-escape slides.tex
```

## Presenting the slides

Install `pdfpc`

```shell
pdfpc -d 45 -n right slides.pdf
```

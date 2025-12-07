# Makefile for Sphinx documentation

.PHONY: help clean html pdf text

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build

help:
	@echo "Sphinx documentation builder commands:"
	@echo ""
	@echo "  make html       - Build standalone HTML files"
	@echo "  make pdf        - Build PDF using LaTeX (requires LaTeX)"
	@echo "  make text       - Build plain text files"
	@echo "  make clean      - Remove all built documentation"
	@echo ""

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) . $(BUILDDIR)/html
	@echo ""
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html"

pdf:
	$(SPHINXBUILD) -b pdf $(SPHINXOPTS) . $(BUILDDIR)/pdf
	@echo ""
	@echo "Build finished. The PDF pages are in $(BUILDDIR)/pdf"

text:
	$(SPHINXBUILD) -b text $(SPHINXOPTS) . $(BUILDDIR)/text
	@echo ""
	@echo "Build finished. The text pages are in $(BUILDDIR)/text"

# Python Version
PYTHON ?= python3

# Source and Build Directories
SPHINXOPTS   =
SPHINXBUILD  = $(PYTHON) ../sphinx/cmd/build.py
SOURCEDIR    = .
BUILDDIR     = _build

# Make Commands
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# $(SPHINXOPTS)
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
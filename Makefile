# Python variables (for the virtual environment)
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ACTIVATE = $(if $(wildcard $(VENV)/bin/activate), . $(VENV)/bin/activate, echo "Not using virtual environment")

MD_FILES = $(shell find . -name '*.md' )
MSGS_FILES = $(shell find . -name '*.msg') $(shell find . -name '*.srv')

.PHONY: docs clean view venv pdf 

docs: html

clean:
	@echo "Removing files"
	@rm html/ autogen/ pdf-build/ magician_msgs.pdf -r 2>>/dev/null || true

view: html
	@xdg-open html/index.html 2>>/dev/null& disown|| open html/index.html 2>>/dev/null

pdf: magician_msgs.pdf

autogen: $(MSGS_FILES)
	@echo "Autogenerating message and service messages documentation"
	@ $(ACTIVATE) && python3 process_messages.py
	

html: $(MD_FILES) autogen index.rst
	@echo "Building documentation"
	$(ACTIVATE) && sphinx-build --conf-dir docs . html

magician_msgs.pdf: $(MD_FILES) 
	@echo "Generating latex files"
	@$(ACTIVATE) && sphinx-build --conf-dir docs . pdf-build --builder latex
	@echo "Running make on pdf-build"
	@make -C pdf-build 
	@cp pdf-build/magicianros2messages.pdf magician_msgs.pdf


venv: $(VENV)/bin/activate requirements.txt

$(VENV)/bin/activate:
	@echo "Creating a new virtual environment..."
	@python3 -m venv $(VENV)
	@echo "Installing dependencies..."
	@$(PIP) install -r requirements.txt
	@touch $(VENV)/bin/activate
	@echo "Dependencies installed."

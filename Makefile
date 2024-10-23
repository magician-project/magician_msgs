doc: 
	echo "Building documentation"
	sphinx-build --conf-dir docs . html README.md

docs/%.md: %.md
	@echo "Creating symboling link for $<"
	@ln -s $(abspath $<) $@


view: doc
	firefox html/index.html

clean:
	@echo "Removing files"
	@rm html/ -r 2>>/dev/null || true

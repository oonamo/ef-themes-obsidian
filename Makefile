.PHONY: clone
clone:
	git clone --depth=1 https://github.com/protesilaos/ef-themes.git ./raw_themes

.PHONY: build
build:
	python ./scripts/parse.py

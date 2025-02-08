.PHONY: clone
clone:
	git clone https://github.com/protesilaos/ef-themes.git ./raw_themes
	cd ./raw_themes
	git checkout 03017b99c673b47957fe813b3934bcd2ae3f9557

.PHONY: build
build:
	python ./scripts/parse.py

.PHY: clean
clean:
	rm raw_themes
	rm theme.css

import variables
import re
import os

from typing import Dict
from template import sub_template

color_pattern  = re.compile(r'\(([\w-]+)\s*"(.*)"\)')
reference_pattern = re.compile(r'\(([\w-]+)\s*([\w-]+)\)')

class EfTheme:
    def __init__(self, filename, name=None, style=None):
        self.filename = filename
        if name is not None:
            self.name = name
        else:
            self.name = re.sub("\-?theme\.el", "", filename)
        self.colors = {}

        if style is not None:
            self.style = style
        else:
            self.style = "dark" if self.name in variables.ef_dark_themes else "light"

    def set_colors(self, colors: Dict[str, str]):
        self.colors = colors

    def get_colors(self) -> Dict[str, str]:
        return self.colors

    def get_name(self):
        return self.name

    def get_style(self):
        return self.style

    def parse(self):
        file = os.path.join(variables.raw_themes, self.filename)
        with open(file, "r") as file:
            for line in file:
                content = line.strip()
                matches = color_pattern.match(content)
                if matches is None: 
                    matches = reference_pattern.match(content)

                if matches is not None and matches[1] is not None and matches[2] is not None:
                    self.colors[matches[1]] = matches[2]

    def resolve_color(self, color) -> str:
        """
        Recursively resolves any reference to another color

        Example:
            "red": "#ff0000"
            ...
            "keyword": "red"

            This is then resolved to be

            "red": "#ff0000"
            "keyword": "#ff0000"

        Return:
            str: The color to use, or "inherit" if not found
        """
        if color[0] == "#":
            return color

        if color in self.colors:
            return self.resolve_color(self.colors[color])

        if color in variables.hex_codes_dict:
            return variables.hex_codes_dict[color]

        if color == "unspecified":
            return "inherit"

        return color

    def resolve_palette(self):
        resolved = {}
        for color in self.colors:
            resolved[color] = self.resolve_color(color)
        self.colors = resolved

    def gen_theme_def(self) -> str:
        self.resolve_palette()
        return sub_template(self.name, self.colors, self.style)

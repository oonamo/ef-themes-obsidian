import re
import os

# Import First
import custom
import variables

from template import template
from theme import EfTheme

def get_ef_themes() -> [str]:
    """
    Returns all ef-themes

    Returns:
        str[]: Filenames of all ef-themes
    """
    themes = os.listdir(variables.raw_themes)
    return [ef_theme for ef_theme in themes if ef_theme != "ef-themes.el" and ef_theme[-3:] == ".el" and ef_theme[0] != "."]


def gen_name_list(style):
    """
    Generates a formatted list of the themes

    Args:
        style (str): The style to generate for. ("light"|"dark")
    """
    generated_list = []
    name_list = variables.ef_dark_themes if style == "dark" else variables.ef_light_themes

    for theme in name_list:
        format_str = f"  - {theme}"
        generated_list.append(format_str)

    for theme in custom.themes:
        if style == theme.get_style():
            format_str = f"  - {theme.get_name()}"
            generated_list.append(format_str)


    return generated_list

def sub_start_end_block(name, replace, old) -> str:
    """
    Substitutes a tag with name 'name'
    Example:
        If name is themedefs, the following will be replaced
        <themedefs:start><themedefs:end>
        /* <themedefs:start><themedefs:end> */

    Returns:
        str: The substituted string
    """
    pattern = f'(\/\* )?<{name}:start>\n*?<{name}:end>( \*\/)?'
    return re.sub(pattern, replace + "\n\n", old)

themes_arr = []
theme_defs = []
themes = get_ef_themes()

for theme in themes:
    tmp = EfTheme(theme)
    tmp.parse()
    theme_defs.append(tmp.gen_theme_def())
    themes_arr.append(tmp)

for theme in custom.themes:
    theme_defs.append(theme.gen_theme_def())
    themes_arr.append(theme)

with open(variables.template_file, "r") as file:
    content = file.read()

    light_themes = gen_name_list("light")
    dark_themes = gen_name_list("dark")

    content = sub_start_end_block("lightthemes", '\n'.join(light_themes), content)
    content = sub_start_end_block("darkthemes", '\n'.join(dark_themes), content)
    content = sub_start_end_block("themedef", '\n'.join(theme_defs), content)

    with open("./theme.css", "w") as output:
        output.write(content)

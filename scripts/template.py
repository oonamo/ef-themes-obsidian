import re

template = r"""
.theme-${_style}.${_name} {
    --bg-main:                ${bg-main};
    --fg-main:                ${fg-main};
    --bg-dim:                 ${bg-dim};
    --fg-dim:                 ${fg-dim};
    --bg-alt:                 ${bg-alt};
    --fg-alt:                 ${fg-alt};
    --bg-active:              ${bg-active};
    --bg-inactive:            ${bg-inactive};
    --red:                    ${red};
    --red-warmer:             ${red-warmer};
    --red-cooler:             ${red-cooler};
    --red-faint:              ${red-faint};
    --green:                  ${green};
    --green-warmer:           ${green-warmer};
    --green-cooler:           ${green-cooler};
    --green-faint:            ${green-faint};
    --yellow:                 ${yellow};
    --yellow-warmer:          ${yellow-warmer};
    --yellow-cooler:          ${yellow-cooler};
    --yellow-faint:           ${yellow-faint};
    --blue:                   ${blue};
    --blue-warmer:            ${blue-warmer};
    --blue-cooler:            ${blue-cooler};
    --blue-faint:             ${blue-faint};
    --magenta:                ${magenta};
    --magenta-warmer:         ${magenta-warmer};
    --magenta-cooler:         ${magenta-cooler};
    --magenta-faint:          ${magenta-faint};
    --cyan:                   ${cyan};
    --cyan-warmer:            ${cyan-warmer};
    --cyan-cooler:            ${cyan-cooler};
    --cyan-faint:             ${cyan-faint};
    --bg-red-intense:         ${bg-red-intense};
    --bg-green-intense:       ${bg-green-intense};
    --bg-yellow-intense:      ${bg-yellow-intense};
    --bg-blue-intense:        ${bg-blue-intense};
    --bg-magenta-intense:     ${bg-magenta-intense};
    --bg-cyan-intense:        ${bg-cyan-intense};
    --bg-red-subtle:          ${bg-red-subtle};
    --bg-green-subtle:        ${bg-green-subtle};
    --bg-yellow-subtle:       ${bg-yellow-subtle};
    --bg-blue-subtle:         ${bg-blue-subtle};
    --bg-magenta-subtle:      ${bg-magenta-subtle};
    --bg-cyan-subtle:         ${bg-cyan-subtle};
    --bg-added:               ${bg-added};
    --bg-added-faint:         ${bg-added-faint};
    --bg-added-refine:        ${bg-added-refine};
    --fg-added:               ${fg-added};
    --bg-changed:             ${bg-changed};
    --bg-changed-faint:       ${bg-changed-faint};
    --bg-changed-refine:      ${bg-changed-refine};
    --fg-changed:             ${fg-changed};
    --bg-removed:             ${bg-removed};
    --bg-removed-faint:       ${bg-removed-faint};
    --bg-removed-refine:      ${bg-removed-refine};
    --fg-removed:             ${fg-removed};
    --bg-graph-red-0:         ${bg-graph-red-0};
    --bg-graph-red-1:         ${bg-graph-red-1};
    --bg-graph-green-0:       ${bg-graph-green-0};
    --bg-graph-green-1:       ${bg-graph-green-1};
    --bg-graph-yellow-0:      ${bg-graph-yellow-0};
    --bg-graph-yellow-1:      ${bg-graph-yellow-1};
    --bg-graph-blue-0:        ${bg-graph-blue-0};
    --bg-graph-blue-1:        ${bg-graph-blue-1};
    --bg-graph-magenta-0:     ${bg-graph-magenta-0};
    --bg-graph-magenta-1:     ${bg-graph-magenta-1};
    --bg-graph-cyan-0:        ${bg-graph-cyan-0};
    --bg-graph-cyan-1:        ${bg-graph-cyan-1};
    --bg-mode-line:           ${bg-mode-line};
    --fg-mode-line:           ${fg-mode-line};
    --bg-completion:          ${bg-completion};
    --bg-hover:               ${bg-hover};
    --bg-hover-secondary:     ${bg-hover-secondary};
    --bg-hl-line:             ${bg-hl-line};
    --bg-paren:               ${bg-paren};
    --bg-err:                 ${bg-err};
    --bg-warning:             ${bg-warning};
    --bg-info:                ${bg-info};
    --border:                 ${border};
    --cursor:                 ${cursor};
    --fg-intense:             ${fg-intense};
    --modeline-err:           ${modeline-err};
    --modeline-warning:       ${modeline-warning};
    --modeline-info:          ${modeline-info};
    --underline-err:          ${underline-err};
    --underline-warning:      ${underline-warning};
    --underline-info:         ${underline-info};
    --bg-char-0:              ${bg-char-0};
    --bg-char-1:              ${bg-char-1};
    --bg-char-2:              ${bg-char-2};
    --bg-fringe:              ${bg-fringe};
    --fg-fringe:              ${fg-fringe};
    --err:                    ${err};
    --warning:                ${warning};
    --info:                   ${info};
    --link:                   ${link};
    --link-alt:               ${link-alt};
    --name:                   ${name};
    --keybind:                ${keybind};
    --identifier:             ${identifier};
    --prompt:                 ${prompt};
    --bg-region:              ${bg-region};
    --fg-region:              ${fg-region};
    --builtin:                ${builtin};
    --comment:                ${comment};
    --constant:               ${constant};
    --fnname:                 ${fnname};
    --keyword:                ${keyword};
    --preprocessor:           ${preprocessor};
    --docstring:              ${docstring};
    --string:                 ${string};
    --type:                   ${type};
    --variable:               ${variable};
    --rx-escape:              ${rx-escape};
    --rx-construct:           ${rx-construct};
    --accent-0:               ${accent-0};
    --accent-1:               ${accent-1};
    --accent-2:               ${accent-2};
    --accent-3:               ${accent-3};
    --date-common:            ${date-common};
    --date-deadline:          ${date-deadline};
    --date-deadline-subtle:   ${date-deadline-subtle};
    --date-event:             ${date-event};
    --date-holiday:           ${date-holiday};
    --date-now:               ${date-now};
    --date-range:             ${date-range};
    --date-scheduled:         ${date-scheduled};
    --date-scheduled-subtle:  ${date-scheduled-subtle};
    --date-weekday:           ${date-weekday};
    --date-weekend:           ${date-weekend};
    --prose-code:             ${prose-code};
    --prose-done:             ${prose-done};
    --prose-macro:            ${prose-macro};
    --prose-metadata:         ${prose-metadata};
    --prose-metadata-value:   ${prose-metadata-value};
    --prose-table:            ${prose-table};
    --prose-table-formula:    ${prose-table-formula};
    --prose-tag:              ${prose-tag};
    --prose-todo:             ${prose-todo};
    --prose-verbatim:         ${prose-verbatim};
    --mail-cite-0:            ${mail-cite-0};
    --mail-cite-1:            ${mail-cite-1};
    --mail-cite-2:            ${mail-cite-2};
    --mail-cite-3:            ${mail-cite-3};
    --mail-part:              ${mail-part};
    --mail-recipient:         ${mail-recipient};
    --mail-subject:           ${mail-subject};
    --mail-other:             ${mail-other};
    --bg-search-match:        ${bg-search-match};
    --bg-search-current:      ${bg-search-current};
    --bg-search-lazy:         ${bg-search-lazy};
    --bg-search-replace:      ${bg-search-replace};
    --bg-search-rx-group-0:   ${bg-search-rx-group-0};
    --bg-search-rx-group-1:   ${bg-search-rx-group-1};
    --bg-search-rx-group-2:   ${bg-search-rx-group-2};
    --bg-search-rx-group-3:   ${bg-search-rx-group-3};
    --bg-space:               ${bg-space};
    --fg-space:               ${fg-space};
    --bg-space-err:           ${bg-space-err};
    --bg-tab-bar:             ${bg-tab-bar};
    --bg-tab-current:         ${bg-tab-current};
    --bg-tab-other:           ${bg-tab-other};
    --bg-term-black:          ${bg-term-black};
    --fg-term-black:          ${fg-term-black};
    --bg-term-black-bright:   ${bg-term-black-bright};
    --fg-term-black-bright:   ${fg-term-black-bright};
    --bg-term-red:            ${bg-term-red};
    --fg-term-red:            ${fg-term-red};
    --bg-term-red-bright:     ${bg-term-red-bright};
    --fg-term-red-bright:     ${fg-term-red-bright};
    --bg-term-green:          ${bg-term-green};
    --fg-term-green:          ${fg-term-green};
    --bg-term-green-bright:   ${bg-term-green-bright};
    --fg-term-green-bright:   ${fg-term-green-bright};
    --bg-term-yellow:         ${bg-term-yellow};
    --fg-term-yellow:         ${fg-term-yellow};
    --bg-term-yellow-bright:  ${bg-term-yellow-bright};
    --fg-term-yellow-bright:  ${fg-term-yellow-bright};
    --bg-term-blue:           ${bg-term-blue};
    --fg-term-blue:           ${fg-term-blue};
    --bg-term-blue-bright:    ${bg-term-blue-bright};
    --fg-term-blue-bright:    ${fg-term-blue-bright};
    --bg-term-magenta:        ${bg-term-magenta};
    --fg-term-magenta:        ${fg-term-magenta};
    --bg-term-magenta-bright: ${bg-term-magenta-bright};
    --fg-term-magenta-bright: ${fg-term-magenta-bright};
    --bg-term-cyan:           ${bg-term-cyan};
    --fg-term-cyan:           ${fg-term-cyan};
    --bg-term-cyan-bright:    ${bg-term-cyan-bright};
    --fg-term-cyan-bright:    ${fg-term-cyan-bright};
    --bg-term-white:          ${bg-term-white};
    --fg-term-white:          ${fg-term-white};
    --bg-term-white-bright:   ${bg-term-white-bright};
    --fg-term-white-bright:   ${fg-term-white-bright};
    --rainbow-0:              ${rainbow-0};
    --rainbow-1:              ${rainbow-1};
    --rainbow-2:              ${rainbow-2};
    --rainbow-3:              ${rainbow-3};
    --rainbow-4:              ${rainbow-4};
    --rainbow-5:              ${rainbow-5};
    --rainbow-6:              ${rainbow-6};
    --rainbow-7:              ${rainbow-7};
    --rainbow-8:              ${rainbow-8};
}
"""

def sub_template(name, colors, style) -> str:
    """
    Substitutes the template with the appropiate characters

    Args:
        name (str): Name of the theme
        colors (Dict[str, str]): Hashmap of name, hex pairs

    Returns:
        str: The substituted template
    """
    def sub_fn(v):
        match = v.group(1)
        if match == "_name":
            return name
        if match == "_style":
            return style

        assert(match in colors)
        return colors[match]

    return re.sub(r'\${(.*?)}', sub_fn, template)

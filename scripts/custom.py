from theme import EfTheme

ef_tint = EfTheme("", "ef-tint", "dark")

ef_tint_colors = {
  "bg-main": "#0d0e1c",
  "fg-main": "#ffffff",
  "bg-dim": "#1d2235",
  "fg-dim": "#989898",
  "bg-alt": "#242e39",
  "fg-alt": "#c6daff",
  "bg-active": "#4a4f69",
  "bg-inactive": "#2b3045",
  "red": "#ff5f59",
  "red-warmer": "#ff6b55",
  "red-cooler": "#ff7f86",
  "red-faint": "#ff8f80",
  "green": "#44bc44",
  "green-warmer": "#70b900",
  "green-cooler": "#00c06f",
  "green-faint": "#88ca9f",
  "yellow": "#d0bc00",
  "yellow-warmer": "#fec43f",
  "yellow-cooler": "#dfaf7a",
  "yellow-faint": "#d2b580",
  "blue": "#2fafff",
  "blue-warmer": "#79a8ff",
  "blue-cooler": "#00bcff",
  "blue-faint": "#82b0ec",
  "magenta": "#feacd0",
  "magenta-warmer": "#f78fe7",
  "magenta-cooler": "#b6a0ff",
  "magenta-faint": "#caa6df",
  "cyan": "#00d3d0",
  "cyan-warmer": "#4ae2f0",
  "cyan-cooler": "#6ae4b9",
  "cyan-faint": "#9ac8e0",
  "bg-red-intense": "#9d1f1f",
  "bg-green-intense": "#2f822f",
  "bg-yellow-intense": "#7a6100",
  "bg-blue-intense": "#1640b0",
  "bg-magenta-intense": "#7030af",
  "bg-cyan-intense": "#2277ae",
  "bg-red-subtle": "#620f2a",
  "bg-green-subtle": "#00422a",
  "bg-yellow-subtle": "#4a4000",
  "bg-blue-subtle": "#242679",
  "bg-magenta-subtle": "#552f5f",
  "bg-cyan-subtle": "#005065",
  "bg-added": "#004a2f",
  "bg-added-faint": "#002922",
  "bg-added-refine": "#035542",
  "fg-added": "#a0e0a0",
  "bg-changed": "#363300",
  "bg-changed-faint": "#2a1f00",
  "bg-changed-refine": "#4a4a00",
  "fg-changed": "#efef80",
  "bg-removed": "#4f1127",
  "bg-removed-faint": "#380a19",
  "bg-removed-refine": "#641426",
  "fg-removed": "#ffbfbf",
  "bg-graph-red-0": "#b52c2c",
  "bg-graph-red-1": "#702020",
  "bg-graph-green-0": "#0fed00",
  "bg-graph-green-1": "#007800",
  "bg-graph-yellow-0": "#f1e00a",
  "bg-graph-yellow-1": "#b08940",
  "bg-graph-blue-0": "#2fafef",
  "bg-graph-blue-1": "#1f2f8f",
  "bg-graph-magenta-0": "#bf94fe",
  "bg-graph-magenta-1": "#5f509f",
  "bg-graph-cyan-0": "#47dfea",
  "bg-graph-cyan-1": "#00808f",
  "bg-mode-line": "#484d67",
  "fg-mode-line": "#ffffff",
  "bg-completion": "#483d8a",
  "bg-hover": "#45605e",
  "bg-hover-secondary": "#654a39",
  "bg-hl-line": "#303a6f",
  "bg-paren": "#5f789f",
  "bg-err": "#471014",
  "bg-warning": "#3b2f04",
  "bg-info": "#103512",
  "border": "#61647a",
  "cursor": "#ff66ff",
  "fg-intense": "#ffffff",
  "modeline-err": "#ffa8bf",
  "modeline-warning": "#dfcf43",
  "modeline-info": "#9fefff",
  "underline-err": "red",
  "underline-warning": "yellow",
  "underline-info": "cyan",
  "bg-char-0": "#0050af",
  "bg-char-1": "#7f1f7f",
  "bg-char-2": "#625a00",
  "bg-fringe": "unspecified",
  "fg-fringe": "unspecified",
  "err": "red",
  "warning": "yellow-warmer",
  "info": "green-cooler",
  "link": "blue-warmer",
  "link-alt": "magenta",
  "name": "magenta",
  "keybind": "magenta-cooler",
  "identifier": "yellow-faint",
  "prompt": "cyan-cooler",
  "bg-region": "#555a66",
  "fg-region": "NONE",
  "builtin": "magenta-warmer",
  "comment": "red-faint",
  "constant": "blue-cooler",
  "fnname": "magenta",
  "keyword": "magenta-cooler",
  "preprocessor": "red-cooler",
  "docstring": "cyan-faint",
  "string": "blue-warmer",
  "type": "cyan-cooler",
  "variable": "cyan",
  "rx-escape": "magenta",
  "rx-construct": "green-cooler",
  "accent-0": "blue-cooler",
  "accent-1": "magenta-warmer",
  "accent-2": "cyan-cooler",
  "accent-3": "red-cooler",
  "date-common": "cyan",
  "date-deadline": "red",
  "date-deadline-subtle": "red-faint",
  "date-event": "fg-alt",
  "date-holiday": "magenta-warmer",
  "date-now": "fg-main",
  "date-range": "fg-alt",
  "date-scheduled": "yellow",
  "date-scheduled-subtle": "yellow-faint",
  "date-weekday": "cyan",
  "date-weekend": "red-faint",
  "prose-code": "cyan-cooler",
  "prose-done": "green",
  "prose-macro": "magenta-cooler",
  "prose-metadata": "fg-dim",
  "prose-metadata-value": "fg-alt",
  "prose-table": "fg-alt",
  "prose-table-formula": "magenta-warmer",
  "prose-tag": "fg-alt",
  "prose-todo": "red",
  "prose-verbatim": "magenta-warmer",
  "mail-cite-0": "blue",
  "mail-cite-1": "magenta-warmer",
  "mail-cite-2": "green-cooler",
  "mail-cite-3": "yellow-cooler",
  "mail-part": "cyan",
  "mail-recipient": "blue-warmer",
  "mail-subject": "cyan-cooler",
  "mail-other": "cyan-warmer",
  "bg-search-match": "bg-warning",
  "bg-search-current": "bg-yellow-intense",
  "bg-search-lazy": "bg-cyan-intense",
  "bg-search-replace": "bg-red-intense",
  "bg-search-rx-group-0": "bg-blue-intense",
  "bg-search-rx-group-1": "bg-cyan-intense",
  "bg-search-rx-group-2": "bg-red-subtle",
  "bg-search-rx-group-3": "bg-magenta-subtle",
  "bg-space": "unspecified",
  "fg-space": "border",
  "bg-space-err": "bg-red-intense",
  "bg-tab-bar": "#2c3045",
  "bg-tab-current": "#0d0e1c",
  "bg-tab-other": "#4a4f6a",
  "bg-term-black": "black",
  "fg-term-black": "black",
  "bg-term-black-bright": "gray35",
  "fg-term-black-bright": "gray35",
  "bg-term-red": "red",
  "fg-term-red": "red",
  "bg-term-red-bright": "red-warmer",
  "fg-term-red-bright": "red-warmer",
  "bg-term-green": "green",
  "fg-term-green": "green",
  "bg-term-green-bright": "green-warmer",
  "fg-term-green-bright": "green-warmer",
  "bg-term-yellow": "yellow",
  "fg-term-yellow": "yellow",
  "bg-term-yellow-bright": "yellow-warmer",
  "fg-term-yellow-bright": "yellow-warmer",
  "bg-term-blue": "blue",
  "fg-term-blue": "blue",
  "bg-term-blue-bright": "blue-warmer",
  "fg-term-blue-bright": "blue-warmer",
  "bg-term-magenta": "magenta",
  "fg-term-magenta": "magenta",
  "bg-term-magenta-bright": "magenta-cooler",
  "fg-term-magenta-bright": "magenta-cooler",
  "bg-term-cyan": "cyan",
  "fg-term-cyan": "cyan",
  "bg-term-cyan-bright": "cyan-cooler",
  "fg-term-cyan-bright": "cyan-cooler",
  "bg-term-white": "#a6a6a6",
  "fg-term-white": "#a6a6a6",
  "bg-term-white-bright": "#ffffff",
  "fg-term-white-bright": "#ffffff",
  "rainbow-0": "fg-main",
  "rainbow-1": "magenta",
  "rainbow-2": "cyan",
  "rainbow-3": "red-warmer",
  "rainbow-4": "yellow",
  "rainbow-5": "magenta-cooler",
  "rainbow-6": "green",
  "rainbow-7": "blue-warmer",
  "rainbow-8": "magenta-warmer"
}

ef_tint.set_colors(ef_tint_colors)


ef_false = EfTheme("", "ef-false", "dark")

ef_false_colors = ef_tint_colors.copy()

ef_false_colors['bg-main'] = "#292d3e"            
ef_false_colors['bg_active'] = "bg-main"             
                                               
ef_false_colors['fg-main'] = "#eeffff"            
                                               
ef_false_colors['fg-intense'] =  "bg-main"
ef_false_colors['fg-dim'] = "gray50"                 
                                               
ef_false_colors['fg-mode-line'] = "#ffffff"       
ef_false_colors['bg-mode-line'] = "#232635"       
                                               
ef_false_colors['bg-tab-other'] = "#242837"       
ef_false_colors['bg-tab-current'] = "bg-main"        
ef_false_colors['bg-tab-other'] = "#242837"       
ef_false_colors['prompt'] = "#c792ea"             
ef_false_colors['bg-hover-secondary'] = "#676e95" 
ef_false_colors['bg-completion'] = "#2f447f"      
ef_false_colors['bg-region'] = "#3c435e"          
                                               
ef_false_colors['accent-1'] = "#79a8ff"           
                                               
ef_false_colors['keyword'] = "#89ddff"            
ef_false_colors['builtin'] = "#82aaff"            
ef_false_colors['comment'] = "#676e95"            
ef_false_colors['string'] = "#c3e88d"             
ef_false_colors['fnname'] = "#82aaff"             
ef_false_colors['type'] = "#c792ea"               
ef_false_colors['variable'] = "#ffcb6b"           
ef_false_colors['docstring'] = "#8d92af"          
ef_false_colors['constant'] = "#f78c6c"           

ef_false.set_colors(ef_false_colors)



# Themes to be returned
themes = [ef_tint, ef_false]

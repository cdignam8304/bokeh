# -*- coding: utf-8 -*-

#%% Dropdown list example tab

def ddownexample_tab():
    
    from bokeh.models.widgets import Dropdown
    from bokeh.layouts import widgetbox
    from bokeh.layouts import layout
    from bokeh.models.widgets import Panel

    # menu = [(x, x) for x in df["opp_type"].unique()]
    menu = [("chris","Chris"),
            ("marie","Marie"),
            ("david","David"),
            ("michael","Michael")]
    
    # button_type: default, primary, success, warning, danger, link
    dropdown = Dropdown(label="Select sibling",
                        button_type="success",
                        menu=menu)
    
    def printddval(attr, old, new):
        print(dropdown.value)

    dropdown.on_change('value', printddval)
    
    mylayout = [widgetbox(dropdown)]
    tab = Panel(child=layout([mylayout]),
                 title="Dropdown example")
    

    
    
    return tab
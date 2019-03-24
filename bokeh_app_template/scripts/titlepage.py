# -*- coding: utf-8 -*-

#%% Title page tab


def titlepage_tab():
    
    from bokeh.models.widgets import Div
    from bokeh.layouts import widgetbox
    from bokeh.layouts import layout
    from bokeh.models.widgets import Panel
    
    width = 800
    height = 400
    text = """
<center><h1>Example bokeh application</h1></center>
<center><h2>with bokeh server</h2></center>
<p>This is a template for a bokeh application.</p>
<p>It implements the following functionality:</p>
<ul>
    <li>bokeh server, which allows callbacks on widgets.</li>
    <li>Tab interface.</li>
    <li>Examples of text and dropdown list widgets.</li>
</ul>
<p>To run the application, go to the folder that contains the application
folder, then type "bokeh serve --show [app folder]"</p>
"""

    div = Div(text=text, width=width, height=height)
    mylayout = [widgetbox(div)]
    tab = Panel(child=layout([mylayout]),
                 title="DOF Home")
    
    return tab
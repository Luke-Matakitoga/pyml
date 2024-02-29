<h1>PYML</h1>
<h4>PYML (<strong>PY</strong>thon & ht<strong>ML</strong>) is a module to extend Tkinter and allow for HTML-style markup to be translated directly into a Tkinter layout, whilst adding support for inline Python code & bindings.</h4>

<h2>How the H*CK do I use it???</h2>

<p>Do not worry, son I WILL SHOW YOU.</p>

```py
# import pyml (which includes tkinter)
from pyml import *

# open your .pyml file
with open("index.pyml") as file:
    page = file.read()

# render page
pyml(page)
```

<p>It's almost too easy...</p>

<h2>How do I write a .pyml file?????</h2>

<p>Frig**n easy:</p>

<ul>
    <li>Create a file.. ```index.pyml``` maybe?</li>
    <li>Then shove a meta tag at the top, this tells the pyml interpreter about your page</li>
    ```html
        <meta
        doctype="pyml-1"
        title="Wowee!"
        window-x="600"
        window-y="450"
    ></meta>
    ```
    
</ul>


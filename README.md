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
    <li>Create a file.. <code>index.pyml</code> maybe?</li>
    <li>Then shove a meta tag at the top, this tells the pyml interpreter about your page</li>
</ul>

```html
<meta
    doctype="pyml-1"
    title="Homepage"
    window-x="600"
    window-y="450">
</meta>
```
    
<ul>
    <li>Now you can launch your project... and see nothing?</li>
    <li>Of course there is nothing, you forgot to add any content 🤬</li>
    <li>Add some text!!!!</li>
</ul>

```html
<p>Hello World!</p>
```

<ul>
    <li>I promise you, there WILL be some python soon...</li>
    <li>In fact, let's add some now!</li>
    <li>At the end of your file, begin the Python Block by inserting <code>@py</code></li>
</ul>

```py
@py # anything after this point is Python

myName = "Luke" # put your own name here you silly man/woman

```

<ul>
    <li>HANG ON! I don't want to put Python code in there same file!</li>
    <li>If you're weird like that, you can just put everything in an external file.</li>
    <li>E.g. if I created a file called <code>extra_code.py</code>, I can add it to the top of the pyml page like so:</li>
</ul>

```html
<script href="extra_code"></script> <!-- Remember, this is the MODULE name, there's no need for the .py file extension -->
```

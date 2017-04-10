# painless [![Build Status](https://travis-ci.org/gusg21/painless.svg?branch=master)](https://travis-ci.org/gusg21/painless)
A feather-weight static site generator like [hyde][1] written in Python

*************************

painless is a static site generator that feels a lot like [hyde][1], except less sophisticated and pretty easy to use (in my opinion).

## Getting started

### Downloading

To get set up, clone the repo to your site's directory like so:

    git clone http://github.com/gusg21/painless/ super-cool-site

Or you can click the download button and rename the downloaded folder. Your choice.

### Folder Layout

The folder structure is like so:

```
painless
│
│   generate.py
│   painless.bat
│   painless.py
│   serve.py
│
├───pages
│       index.md
│
├───serve
│       index.html
│
└───templates
        bottom.html
        top.html
```

The `pages` folder is where all of the markdown for each page of your website goes. For instance, the default index.md, when compiled, results in the index.html of the `serve` folder.

The `serve` folder is the fully functional html output. This is where you should point your webserver.

The `templates` folder is the reusable HTML code. This code can be referenced in the markdown for easy use.

### Syntax

The syntax for the input files (in the `pages` folder) are the same as your run-of-the-mill markdown (see [mistune][3]). The additions are:

- Template Reference `~template`
- Comments `$ blah blah blah`
- Static Values `[[ time ]]` (see the wiki)
- Divs:

```
.foo
I'm a div!
.
  ```

  Result:

  ```
<div class="foo">
<p>I'm a div!</p>
</div>
  ```
- Spans:

```
..foo
I'm a span!
..
  ```

  Results:

  ```
<span class="foo">
<p>I'm a span!</p>
</span>
  ```

**pages/index.md:**
```markdown
~header

I'm markdown content! _Yay_!
```

**templates/header.html:**
```HTML
<h1>Site Name<h1>
<div class="nav">
  <a href="about">About</a>
</div>
```

And the resulting index.html would be:
```HTML
<h1>Site Name<h1>
<div class="nav">
  <a href="about">About</a>
</div>

<p>I'm markdown content! <i>Yay</i>!</p>
```

A cool Jinja-like feature implemented in painless is argument passing. You can do this:

```markdown
~import:header arg=value
```

Template header.html:
```HTML
<p>{{ arg }}</p>
```

Result:
```HTML
<p>value</p>
```

### Testing your site

To test and serve your site, navigate to the folder with `painless.py` in it and type:

    python painless.py gen

Then type:

    python painless.py serve

And visit <http://localhost:8000/> in your browser of choice.

_**Note**: If you're running Windows, instead of typing "python painless.py" you can type "painless", and it will run painless.bat instead._

## License

See [LICENSE][2].

[1]: http://hyde.github.io/
[2]: https://github.com/gusg21/painless/blob/master/LICENSE
[3]: http://github.com/lepture/mistune

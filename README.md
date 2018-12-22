# python-packaging-test-bed
Test bed to play around with Python packaging over the holiday.

Steps:

Copying a documentation template and changing all the configuration is too much trouble, so use ~/anaconda3/envs/python37env/bin/sphinx-quickstart

/home/dahanna/python-packaging-test-bed$ ~/anaconda3/envs/python37env/bin/sphinx-quickstart doc
Welcome to the Sphinx 1.8.2 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: doc

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]: 

The project name will occur in several places in the built documentation.
> Project name: python-packaging-test-bed
> Author name(s): David Hannasch
> Project release []: 

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: 

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]: 

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]: 
Indicate which of the following Sphinx extensions should be enabled:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: 
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]: 
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: 

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]: 
> Create Windows command file? (y/n) [y]: 

Creating file doc/source/conf.py.
Creating file doc/source/index.rst.
Creating file doc/Makefile.
Creating file doc/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file doc/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.


Add this to .git/config:
[user]
	email = David.A.Hannasch@gmail.com
	name = David A. Hannasch
or git config user.name "David A. Hannasch" and git config user.email David.A.Hannasch@gmail.com



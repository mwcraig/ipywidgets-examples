# Jupyter widget example

This is intended as a straightforward example of how to build a pure-python widget that uses a Model-View-Controller design. It works with `ipywidgets 5+` and `traitlets 4.1+`. This is not currently packaged for installation via pypi. Instead, download it as a zip from github, or, even better, clone it and improve it!

The widget is a simple password generator.

The file `model.py` contains the data model: a class that has as properties the parameters that go into generating the password and a method for doing the generation based on the parameters. The `observe` decorator indicates which method gets called when properties of the widgets change because the user has adjusted them; this is one piece of the controller.

The file `gui.py` does two things: set up the actual widgets (the view) and link properties of the widget elements to traits in the model (one piece of the controller).

from __future__ import print_function, division

from ipywidgets import Box, Layout, IntSlider, RadioButtons, Label, Checkbox, VBox, ToggleButtons, HBox
from traitlets import link

from model import PassGen, SPECIAL_GROUPS


class PassGenGUI(Box):
    """
    Class to encapsulate the interface for a simply polynomial
    graphing tool.

    """
    def __init__(self):
        super(PassGenGUI, self).__init__(description='Graph container')
        self.model = PassGen()
        self.layout.width = '100%'
        self._length = IntSlider(min=8, max=20, description='Password Length')
        link((self._length, 'value'), (self.model, 'password_length'))

        self._special = self._special_char_box()

        self._numbers = self._number_box()


        self._top_label = Label(value='Generated password:')

        self._password_text = Label(' ')
        self._password_text.layout.margin = '0 0 0 20px'
        link((self._password_text, 'value'), (self.model, 'password'))

        self.children = [self._top_label,
                         self._password_text,
                         self._length, self._special,
                         self._numbers]

    def _special_char_box(self):
        """
        The amount of space provided as a description in a ToggleButtons
        or a RadioButton. This makes a compound widget that has a longer
        description over some buttons.

        Note that the linking to the model is handled here so that the calling
        code, __init__ does not need to know about the details of this widget.
        """
        explanation = Label('Select one of the groups of special characters '
                            'below. From 1 to 3 special characters will be included.')
        special = ToggleButtons(options=SPECIAL_GROUPS)
        special.layout.margin = '0 0 0 20px'
        link((special, 'value'),
             (self.model, 'special_character_groups'))

        container = VBox(description='Special character',
                         children=[explanation, special])
        return container

    def _number_box(self):
        """
        See comments for the special character box above.
        """
        explanation = Label('Check box to include 1 to 3 numbers '
                            'in the password:')
        check = Checkbox()
        link((check, 'value'), (self.model, 'include_numbers'))
        container = HBox(description='Number checkbox',
                         children=[explanation, check])
        return container

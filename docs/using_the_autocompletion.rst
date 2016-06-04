************************
Using the Autocompletion
************************

To enable the autocompletion feature for the current session just click on the
**Start** button.

  .. image:: images/default_panels_finished_setup.png

As soon as you start typing a context box will popup that gives you suggestions.

  .. image:: images/default_context_box.png

Normally the context box opens and closes automatically but you can also do this
manually:

    - **Open:** *shift ESC*
    - **Close:** *ESC* or clicking somewhere else in the text editor

Navigation through the context box:

    - *Arrow Up/Down:* Move the selected index in the arrow-direction.
    - *Page Up/Down:* Same as arrow keys but skips a fixed a few items.
    - *Home/End:* Jump to the first or last element.
    - *Wheel Up/Down:* Move the selected index in the rotation direction.
      This only works when the mouse is on top of the context box.

Inserting a suggestion:

    - Use *TAB/ENTER* to insert the currently selected suggestion.
    - Left click on a suggestion will insert it too.


The Jedi library is not always fast. Particularly when it scans a new module
it can take a second. After that it should be faster again. If you don't want these
slow downs you can turn Jedi of by disabling the **Use Jedi Completion** property.
Fortunally, the Jedi library is not the only *Completion Provider* in this addon.
You will still be able to autocomplete words that already exist as well as the
*bpy.ops* operators.

# soundboard

This is a sound board app written in python. It uses 2 types of buttons:
    1. buttons that can be pressed multiple times
    2. buttons that, when ctrl-keyed, stop (recommended for very long sound effects/music)
In linux, the numpad buttons are the keybinds. The buttons are layed out to match, visually, the 10-key numpad.
Windows may have keybind issues. The file paths may also need to be a different format.
It is easy to get sound samples from http://bbcsfx.acropolis.org.uk/
(for personal use)

# requirements
You will need to have sound files on your computer, and change the file paths for each button press to match.
You will want to re-name the buttons so that you know what each one does.
For the keybinds to work, the window will have to have focus. It is recommended you pull it in front of your DAW if recording so you can monitor if the recording is continuing.

You will also need to have the tkinter, pygame, and os libraries available in your python environment.

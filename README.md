# Oasis_infobyte_taskno_5
A Random Password generator using Python and Tkinter containing GUI.
In this project a Python Graphical User Interface is created which takes in the user's input criteria of password length and character set preferences.
We import Tkinter for executing python GUI Interface and from that we can create the interactive interface for the project.
From random we import randint which is used to import random inetgers within the ascii values that are provided.
First we initialize a Tkinter window titled "PASSWORD GENERATOR" with a specified background color and size with the window having a root geometry of 800x600.
We add two entry panels. One entry panel named: 'How many characters do you want for your password?', asks the user for a numeric input for the number of characters that the password should have. The sccond entry panel is a display panel whcih displays the password that is generated.
There are four checkboxes present in the GUI Window which present the options for character sets that the user wants to present in the password. They are Uppercase, lowercase, symbols and digits. The user can tick the character sets that they want to be included in the password. 
The first function present is the 'generate_password' which is linked to the 'GENERATE STRONG PASSWORD' button. On clicking the button it executes the function and generates the password.
The next function is the 'clip' fuction which is connected to the 'Copy to Clipboard' button, on pressing which it will copy the generated password to the clipboard which the user can paste to the destination that he/she likes.

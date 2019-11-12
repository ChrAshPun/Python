#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard 

import pyperclip, re

# (''') to create a multiline string
# re.VERBOSE to enable comments
phoneRegex = re.compile(r'''(

# ()? means its optional
(\d{3} | \(\d{3}\))?

)''', re.VERBOSE)
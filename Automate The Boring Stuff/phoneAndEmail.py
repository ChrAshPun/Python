#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard 

# Pyperclip is a cross-platform Python module to copy and paste strings.
# pip install pyperclip

import pyperclip, re

# triple-quote syntax to create a multiline string
# ? makes the group that precedes it as optional
# re.VERBOSE as a second argument to enable comments
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # area code \d\d\d or (\d\d\d)
    (\s|-|\.)?                   # separator ' ' or - or .
    (\d{3})                      # first 3 digits \d\d\d
    (\s|-|\.)                    # separator ' ' or - or .
    (\d{4})                      # last four digits \d\d\d\d
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension space (ext or x or ext) space 2-5 digits
)''', re.VERBOSE)

# + means concatenation
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+            # username
    @                            # @ symbol
    [a-zA-Z0-9.-]+               # domain name
    (\.[a-zA-Z]{2,4})            # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text.
# use paste() function to get a string value of the text on the clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    if groups[1] != '': 
        # join the area code, first 3 digits, & last 4 digits with '-'
        phoneNum = '-'.join([groups[1],groups[3],groups[5]])
        # add the phoneNum to the matches list
        matches.append(phoneNum)
    else:
        # if there is no area code, join first 3 digits & last 4 digits with '-'
        phoneNum = '-'.join([groups[3],groups[5]])
        # add the phoneNum to the matches list
        matches.append(phoneNum)   
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
# if any matches were found
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
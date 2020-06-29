#! python3
import sys
import pyperclip

TEXT = {
    'greetings': "Hello! Welcome to KASH. Thanks for choosing to save with us,\
        you are now part of a decentralized financial community. Learn more \
            about KASH here.",
    'update': "Dear user, We like to inform you that the version of the \
        application you're using is an outdated please update the application \
            from the AppStore",
    'personal_greeting': 'Hi, \n How are you doing and how\'s your day going?',
    'meeting': "Sorry I'm in a meeting. I'll call you later if it's not an \
        emergency"
}


if len(sys.argv) < 2:
    print("Usage: python clip.py [keyword] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")

else:
    print(f"There is no text for {keyphrase}")

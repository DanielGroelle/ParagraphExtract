## Paragraph Extraction Tool

# About

This Paragraph Extraction Tool was primarily written to automate adding paragraphs to [TypingJerboa](https://github.com/DanielGroelle/TypingJerboa). Simply drag in pieces of text, and run the script in order to get paragraphs that can be automatically imported into TypingJerboa for the purpose of testing a users typing skills.

# Setup

Create a folder /texts and place all texts you wish to extract from inside. The names of each file should follow the form of Author - Title.txt

# Usage

Within the paragraphextract.py are a couple variables to be configured. ``LINE_CHARACTER_MIN`` specifies the minimum length a line can be in order to be a paragraph. ``LINE_CHARACTER_MAX`` specifies the maximum a line can be. If a line goes beyond this maximum, it will be split at punctuation to fit within these bounds.

Once the desired values are set, run ``py paragraphextract.py`` from within the root directory of the project. A folder should be created called "/processed". Within will be csv files containing extracted paragraphs.
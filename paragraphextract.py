import csv
from os.path import exists
from os import makedirs
from os import scandir

if not exists("./texts"):
  makedirs("./texts")

texts = scandir("./texts")
for text in texts:
  if text.is_file():
    print(text.name)
    title = text.name.split(" - ")[0]
    author = text.name.split(" - ")[1].split(".txt")[0]
    print(title)
    print(author)
    
    file = open("./texts/" + text.name, encoding="utf-8")
    print(file.readlines()[0:2])

    outputfile = open("./texts/" + author + " - " + title + ".csv", "w", encoding="utf-8", newline='')
    writer = csv.writer(outputfile)
    file.close()

texts.close()
import csv
import regex as re
from os.path import exists
from os import makedirs
from os import scandir

LINE_CHARACTER_MIN = 70
LINE_CHARACTER_MAX = 360

if not exists("./texts/processed"):
  makedirs("./texts/processed")

texts = scandir("./texts")
for text in texts:
  if text.is_file():
    author = text.name.split(" - ")[0]
    title = text.name.split(" - ")[1].split(".txt")[0]
    print(author + " - " + title)

    outputfile = open("./texts/processed/" + author + " - " + title + ".csv", "w", encoding="utf-8", newline='')
    writer = csv.writer(outputfile)

    file = open("./texts/" + text.name, encoding="utf-8")

    lines = file.readlines()
    for line in lines:
      # filter out newlines, replace emdashes with regular dashes, and replace alternate quotations with straight digital quotations
      line = line.replace("\n", "").replace("—", "-").replace("–", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
      line = line.strip()

      # make sure line is longer than the minimum, and starts on a valid uppercase character
      if re.compile(r'^\P{Ll}*').match(line) != None:
        if len(line) >= LINE_CHARACTER_MIN and line[0] != " ":
          if len(line) >= LINE_CHARACTER_MAX:
            # split on punctuation while preserving the punctuation
            splitlines = re.split("([?!.])", line)
            for splitline in splitlines:
              if len(splitline) >= LINE_CHARACTER_MIN and len(splitline) <= LINE_CHARACTER_MAX:
                splitline = splitline.strip()
                writer.writerow([splitline])
          else:
            writer.writerow([line])

    outputfile.close()
    file.close()

texts.close()
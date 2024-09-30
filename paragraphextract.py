import csv
import regex as re
from os.path import exists
from os import makedirs
from os import scandir

LINE_CHARACTER_MIN = 70
LINE_CHARACTER_MAX = 360

def read_file(text):
  author = text.name.split(" - ")[0]
  title = text.name.split(" - ")[1].split(".txt")[0]
  print(author + " - " + title)

  output_file = open("./texts/processed/" + author + " - " + title + ".csv", "w", encoding="utf-8", newline='')
  writer = csv.writer(output_file)
  writer.writerow([author, title])

  file = open("./texts/" + text.name, encoding="utf-8")
  lines = file.readlines()
  for line in lines:
    # filter out newlines, replace emdashes with regular dashes, replace alternate quotations with straight digital quotations, and expand single character ellipses
    line = line.replace("\n", "").replace("—", "-").replace("–", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"').replace("„", '"').replace("…", "...")
    line = line.strip()

    # make sure line starts on a valid uppercase character
    if re.compile(r'^\P{Ll}*').match(line) != None:
      # make sure line is longer than minimum
      if len(line) >= LINE_CHARACTER_MIN:
        if len(line) >= LINE_CHARACTER_MAX:
          long_line = split_long_lines(line)
          if (len(long_line)):
            writer.writerow([long_line])
        else:
          writer.writerow([line])

  output_file.close()
  file.close()

def split_long_lines(line: str):
  # split on punctuation while preserving the punctuation
  punctuation_separators = re.compile("((?<!Mr)(?<!Mrs)(?<!Ms)(?<!Jr)(?<!Sr)[\.!?]\"?)")
  split_lines = re.split(punctuation_separators, line)

  # find punctuation in split_lines, and concat with the previous sentence
  new_split_lines = []
  for concat_line in range(0, len(split_lines)):
    if (punctuation_separators.match(split_lines[concat_line])):
      new_split_lines[len(new_split_lines)-1] = new_split_lines[len(new_split_lines)-1] + split_lines[concat_line]
    else:
      new_split_lines.append(split_lines[concat_line])
  split_lines: list[str] = new_split_lines
  
  # accumulate on line_to_write until max length is reached and return result
  line_to_write = ""
  for split_line in split_lines:
    new_length = len(line_to_write + split_line)
    if new_length >= LINE_CHARACTER_MIN and new_length <= LINE_CHARACTER_MAX:
      line_to_write += split_line
    else:
      return line_to_write

def main():
  if not exists("./texts/processed"):
    makedirs("./texts/processed")

  texts = scandir("./texts")
  for text in texts:
    if text.is_file():
      read_file(text)

  texts.close()

main()
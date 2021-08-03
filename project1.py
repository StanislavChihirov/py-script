import requests
import bs4
from gensim.summarization import keywords

output_file = "output.txt"
output_file2 = "output2.txt"

res = requests.get(f"http://en.wikipedia.org/wiki/Special:Random")
res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text, "html.parser")

with open(output_file, "w", encoding="utf-8") as f:
    for i in wiki.select("p"):
        # write each paragraph to the file
        f.write(i.getText())

with open(output_file2, "w", encoding="utf-8") as f:
    for i in wiki.select("p"):
        # write each paragraph to the file
        f.write(keywords(i.getText()))

new = []
with open(output_file2, "r") as f:
    for line in f:
        stripped = line.strip("\n")
        new.append(stripped)

new.sort()  # sorts by letter
with open(output_file2, "w") as file:
    for k in new:
        file.write(k + "\n")

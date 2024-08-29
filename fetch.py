import requests
import json
from bs4 import BeautifulSoup

if __name__ == "__main__":

    r = requests.get("https://www.cs.columbia.edu/~hgs/audio/harvard.html")

    soup = BeautifulSoup(r.content, "html.parser")

    lists = []

    for elem in soup.find_all("ol"):

        lists.append([item.text.strip() for item in elem.find_all("li")])

    with open("src/lists.js", "w") as f:
        f.write("export const LISTS=")
        f.write(json.dumps(lists, indent=2))


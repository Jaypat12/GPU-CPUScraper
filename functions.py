from bs4 import BeautifulSoup
import requests
import re


def find_graphics_card(search_term):
    items_found = []
    search_term2 = search_term.replace(" ", "+")
    # Loads and parses the html file
    url = f"https://www.newegg.com/p/pl?N=4131%204814&d{search_term2}&Order=1"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(string=re.compile(search_term))
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent["href"]
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong
        if price == None:
            continue
        else:
            items_found.append({"Name": item, "Price": price.string, "Link": link})
    return items_found


def find_cpu_card(search_term):
    items_found = []
    search_term2 = search_term.replace(" ", "+")
    url = f"https://www.newegg.com/p/pl?N=100007671%204131%204814&d={search_term2}&isdeptsrh=1&Order=1"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(string=re.compile(search_term))
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent["href"]
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong.string
        items_found.append({"Name": item, "Price": price, "Link": link})
    return items_found




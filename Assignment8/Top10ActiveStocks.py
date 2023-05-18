import time
import requests
from bs4 import BeautifulSoup

starter_file = "starterfile.txt"
active_stocks_file = "active_stocks.txt"
base_url = "https://finance.yahoo.com/most-active"

def retrieve_top_10_active_stocks():
    # Send a GET request to the Yahoo Finance page
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the stock symbols
    table = soup.find("table", class_="W(100%)")

    # Find all rows in the table
    rows = table.find_all("tr")

    # Extract the stock symbols from each row
    stock_symbols = []
    for row in rows[1:11]:  # Skip the header row and get the top 10 symbols
        symbol = row.find("a")
        if symbol is not None:
            stock_symbols.append(symbol.text)

    return stock_symbols

def fill_active_stocks_file():
    top_10_stocks = retrieve_top_10_active_stocks()
    with open(active_stocks_file, "w") as file:
        for stock in top_10_stocks:
            file.write(stock + "\n")

def check_starter_file():
    while True:
        if "go" in open(starter_file).read():
            fill_active_stocks_file()
            print("active_stocks.txt has been filled.")

            # Remove "go" from the starter file
            with open(starter_file, "r+") as file:
                content = file.read().replace("go", "")
                file.seek(0)
                file.write(content)
                file.truncate()

        time.sleep(1)

check_starter_file()

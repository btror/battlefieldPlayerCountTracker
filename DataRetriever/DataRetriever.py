import requests
from bs4 import BeautifulSoup


class SteamDataRetriever:
    def __init__(self, url):
        self.HEADERS = ({"User-Agent":
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/90.0.4430.212 Safari/537.36",
                         "Accept-Language": "en-US, en;q=0.5"})
        self.url = url

    def get_soup(self):
        html = requests.get(self.url, headers=self.HEADERS).text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def get_data(self):
        soup = self.get_soup()
        table = soup.find("table", {"class": "common-table"})

        table_body = table.find("tbody")
        data = []
        rows = table_body.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        title = self.get_title()
        return data, title

    def get_title(self):
        soup = self.get_soup()
        title = soup.find("h1", {"id": "app-title"})
        title = title.find("a").text
        return title

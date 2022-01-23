import requests
from bs4 import BeautifulSoup


class DataRetriever:
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
        table_2042 = soup.find("table", {"class", "common-table"})

        table_body = table_2042.find("tbody")
        data = []
        rows = table_body.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        return data

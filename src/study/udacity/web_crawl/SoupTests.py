import unittest
import requests
import bs4


class SoupTests(unittest.TestCase):
    def before_test(self):
        print("\nstart\n")

    resp: requests.Response = requests.get("https://en.wikipedia.org/wiki/Dead_Parrot_sketch")
    doc: str = resp.text

    def test_request(self):
        resp: requests.Response = requests.get("https://en.wikipedia.org/wiki/Dead_Parrot_sketch")
        print(type(resp.text))
        print(resp.text)

    def test_select_all_anchor(self):
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self.doc, "html.parser")
        for link in soup.find_all('a'):
            print(type(link), link)

    def test_select_all_anchors_in_first_paragraph(self):
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self.doc, "html.parser")
        for link in soup.p.find_all("a"):
            print(type(link), link)

    def test_select_by_id(self):
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self.doc, "html.parser")
        div:bs4.Tag = soup.find(id="mw-content-text")
        print(type(div), div.attrs)

    def test_first_link(self):
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self.doc, "html.parser")
        content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
        for element in content_div.find_all("p", recursive=False):
            if element.a:
                first_relative_link = element.a.get('href')
                print(first_relative_link)
                break


if __name__ == '__main__':
    unittest.main()

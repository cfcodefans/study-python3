import unittest
import requests
import bs4


class SoupTests(unittest.TestCase):
    def before_test(self):
        print("\nstart\n")

    doc: str = ""

    def __init__(self):
        super(SoupTests, self).__init__(self, methodName='runTest')
        resp: requests.Response = requests.get("https://en.wikipedia.org/wiki/Dead_Parrot_sketch")
        doc = resp.text

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
        div = soup.find(id="mw-content-text")
        print(type(div), div)


if __name__ == '__main__':
    unittest.main()

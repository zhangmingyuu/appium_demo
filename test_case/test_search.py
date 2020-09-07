import pytest

from page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("key,stock_type,price",[
        ("ALIBABA","BABA",200),
        ("JD","JD",20)
    ])
    def test_search_data(self,key,stock_type,price):
        assert self.main.goto_search_page().search(key).get_price(stock_type)>price


    def test_search(self):
        assert self.main.goto_search_page().search("阿里巴巴").get_price("BABA")>200


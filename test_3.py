from contacts import ContactPage
import pytest

@pytest.mark.usefixtures('browser')
class TestTask3:
    '''В данном классе описаны тесты первого задания'''

    def setup_method(self):
        self.mainpage = ContactPage(self.driver)
        self.mainpage.go_to_mainsite()


    def test_download(self):
        assert self.mainpage.download(), 'скачал не то'

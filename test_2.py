from contacts import ContactPage
import pytest

@pytest.mark.usefixtures('browser')
class TestTask2:
    '''В данном классе описаны тесты первого задания'''

    def setup_method(self):
        self.mainpage = ContactPage(self.driver)
        self.mainpage.go_to_mainsite()


    def test_go_kontacts(self):
        self.mainpage.go_to_contacts()
        assert 'contacts' in self.mainpage.get_link(), 'не та кнопка'

    def test_area(self):
        self.mainpage.go_to_contacts()
        infoHMAO = self.mainpage.get_area()
        assert infoHMAO[0] == 'Ханты-Мансийский АО-Югра' and len(infoHMAO[1]) > 1, 'Что-то не так'

    def test_change_region(self):
        self.mainpage.go_to_contacts()
        infoHMAO = self.mainpage.get_area()
        self.mainpage.change_region()
        infoKK = self.mainpage.get_area()
        requirements=[infoHMAO[1] != infoKK[1], infoKK[0] == 'Камчатский край',
                      '41-kamchatskij-kraj' in self.mainpage.get_link(), 'Камчатский край' in self.mainpage.get_title()]
        assert all(requirements), 'Требования не выполнены'

from pages.contacts import ContactPage
import pytest


@pytest.mark.usefixtures('browser')
class TestTask1:
    '''В данном классе описаны тесты первого задания'''

    def setup_method(self):
        self.mainpage = ContactPage(self.driver)
        self.mainpage.go_to_mainsite()


    def teardown_method(self):
        '''Закрывает вторую вкладку браузера'''
        if len(self.mainpage.driver.window_handles)>1:
            self.mainpage.go_to_window(handle_num=1)
            self.mainpage.driver.close()
            self.mainpage.go_to_window(handle_num=0)


    def test_go_kontacts(self):
        self.mainpage.go_to_contacts()
        assert 'contacts' in self.mainpage.get_link(), 'не та кнопка'



    def test_go_tenzor(self):
        self.mainpage.go_to_contacts()
        self.mainpage.click_banner()
        self.mainpage.go_to_window(1)
        assert self.mainpage.get_link() == 'https://tensor.ru/', 'не та ссылка'


    def test_check_people(self):
        self.mainpage.go_to_contacts()
        self.mainpage.click_banner()
        self.mainpage.go_to_window(1)
        people_block = self.mainpage.check_findpeople()
        assert people_block and 'Сила в людях' in people_block.text, 'нет блока'

    def test_check_detail(self):
        self.mainpage.go_to_contacts()
        self.mainpage.click_banner()
        self.mainpage.go_to_window(1)
        people_block = self.mainpage.check_findpeople()
        self.mainpage.go_details()
        assert self.mainpage.get_link() == 'https://tensor.ru/about', 'не та ссылка'


    def test_photo(self):
        self.mainpage.go_to_contacts()
        self.mainpage.click_banner()
        self.mainpage.go_to_window(1)
        people_block = self.mainpage.check_findpeople()
        self.mainpage.go_details()
        assert self.mainpage.check_photo(), 'размеры не равны'

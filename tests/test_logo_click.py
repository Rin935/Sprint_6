import allure
from conftest import driver
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLogo:
    @allure.title('Провекра перехода на главную страницу сервиса при клике на лого "Самокат" в шапке')
    def test_logo_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        main_page.wait_for_page_to_load()
        assert main_page.get_page_title() == 'Дзен — платформа для просмотра и создания контента. Вы всегда найдёте здесь то, что подходит именно вам: сотни тысяч авторов ежедневно делятся постами, статьями, видео и короткими роликами'

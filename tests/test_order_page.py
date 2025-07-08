import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from conftest import driver
from locators.order_page_locators import OrderPageLocators
from data import *


class TestOrderPageOrder:
    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Тестирование функциональности оформления заказа из двух точек входа')
    @pytest.mark.parametrize('button, test_data', [
        (MainPageLocators.order_button_in_header, TestData.test_data_user1),
        (MainPageLocators.order_button_in_main, TestData.test_data_user2)
    ])
    def test_a_1(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_displaying_of_button_check_status_of_order()
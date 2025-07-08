import pytest
import allure
from conftest import driver
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import TestData


class TestMainPageFaq:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления нужного текста при нажатии на определенную иконку развертывания в разделе')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answers)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_number)
        main_page.click_on_faq_items(question_number)
        main_page.wait_visibility_of_faq_answers(question_number)
        assert main_page.get_displayed_text_from_faq_answers(question_number) == expected_answer
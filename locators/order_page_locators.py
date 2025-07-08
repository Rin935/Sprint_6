from selenium.webdriver.common.by import By


class OrderPageLocators:
    title_page_personal = (By.XPATH, ".//div[text()='Для кого самокат' and contains (@class, 'Order_Header')]")
    name = (By.XPATH, ".//input[@placeholder='* Имя']")
    lastname = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    address = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    select_item_in_dropdown_metro = (By.XPATH, ".//li[@class='select-search__row']")
    phone = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, ".//button[text()='Далее']")
    title_page_rent = (By.XPATH, ".//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, ".//div[@class='react-datepicker-popper']")
    calendar_items = (By.XPATH, ".//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    field_rental_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    dropdown_item_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    checkbox_grey_color_scooter = (By.XPATH, ".//input[@id='grey']")
    comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    button_make_order = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    button_yes_confirm_order = (By.XPATH, ".//button[text()='Да']")
    button_check_status_of_order = (By.XPATH, ".//[text()='Посмотреть статус']")

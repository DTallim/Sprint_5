from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestUrl,TEST_USER
from locators import TestLocators
from conftest import driver

#Тестирование выхода из учетной записи
class TestLogout:
    def test_logout(self,driver):
        driver.get(TestUrl.MAIN_URL_TEST)

    #Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

    #Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
    )

    #Найти поле "Email" и заполнить его
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(TEST_USER['email'])
    #найти поле "Пароль" и заполнить его
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(TEST_USER['password'])
    #Найти кнопку "Войти" и нажать
        driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

    #Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
    )

    #Переход в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_LOGOUT)
    )

    #Найти кнопку "выйти" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
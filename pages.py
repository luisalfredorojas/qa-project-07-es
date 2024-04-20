import Helpers
import data
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    type_picker = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown')

    # Numero de telfono
    number_open_modal = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    number_modal = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]')
    # Darle clikc a este para poder poner el numero de telefono
    number_input_click = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/label')
    number_input = (By.ID, 'phone')
    number_code_input = (By.ID, 'code')
    number_input_label = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[1]/div[1]')
    number_modal_next = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    number_modal_code_next = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    code_modal = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active')

    # Metodo de pago
    payment_method = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    payment_method_modal = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]')
    add_card_modal = (By.CSS_SELECTOR, '.pp-plus-container')
    add_card_modal_inputs = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]')
    add_card_number_input = (By.ID, 'number')
    add_card_CVV_name = (By.NAME, 'code')
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_payment_method_modal = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    payment_method_value = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
    click_out_of_focus = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div')

    # Mensaje para el conductor
    message_driver_click = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div')
    message_driver_input = (By.ID, 'comment')

    # Requisitos para el pedido
    requirements = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[1]')
    requirements_ice_cream_mantle_options = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[2]/div')
    requirements_switch = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
    requirements_plus_iceCream = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

    #Modal para pedir taxi
    call_a_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]')
    call_a_taxi_button_header = (By.CSS_SELECTOR, '.smart-button-main')
    searching_taxi_button_header = (By.CSS_SELECTOR, '.order-header-title')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    def to_and_get_address_to_be_visible(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, 'from')))
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, 'to')))

    # Pedir un taxi
    def ask_taxi_click(self):
        self.driver.find_element(*self.ask_taxi).click()

    def ask_taxi_button_to_be_visible(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ask_taxi))

    def type_picker_section(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.type_picker))

    # Pedir tarifa comfort
    def click_comfort(self):
        self.driver.find_element(*self.comfort_button).click()

    # Agregar numero de telefono
    def open_modal_phone_number(self):
        self.driver.find_element(*self.number_open_modal).click()

    def click_label_phone_number(self):
        self.driver.find_element(*self.number_input_click).click()

    def set_phone_number(self):
        self.driver.find_element(*self.number_input).send_keys(data.PHONE_NUMBER)

    def get_phone_number(self):
        return self.driver.find_element(*self.number_open_modal).text

    def click_next_phone_number(self):
        self.driver.find_element(*self.number_modal_next).click()

    def click_label_code(self):
        self.driver.find_element(*self.number_input_label).click()

    def set_code(self):
        self.driver.find_element(*self.number_code_input).send_keys(Helpers.retrieve_phone_code(self.driver))

    def click_next_phone_number_code(self):
        self.driver.find_element(*self.number_modal_code_next).click()

    def to_be_visible_phone_number_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.number_modal))

    def to_be_visible_phone_number_code_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.code_modal))

    # Payment Method

    def click_open_modal_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_card_inside_modal(self):
        self.driver.find_element(*self.add_card_modal).click()

    def to_be_visible_add_card_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.add_card_modal))

    def set_payment_method_card_number(self):
        self.driver.find_element(*self.add_card_number_input).send_keys(data.CARD_NUMBER)
        self.driver.find_element(*self.add_card_number_input).send_keys(Keys.TAB)

    def set_cvv(self):
        self.driver.find_element(*self.add_card_CVV_name).send_keys(data.CARD_CODE)
        self.driver.find_element(*self.add_card_CVV_name).send_keys(Keys.TAB)

    def click_next_payment_method(self):
        self.driver.find_element(*self.add_card_button).click()

    def close_payment_method_click(self):
        self.driver.find_element(*self.close_payment_method_modal).click()

    def to_be_visible_close_payment_method_click(self):
        WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable(self.close_payment_method_modal))

    def get_payment_method_value(self):
        return self.driver.find_element(*self.payment_method_value).text

    def to_be_visible_card_code_inputs(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.add_card_modal_inputs))


    def to_be_clickable_card_code_add(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.add_card_button))

# Mensaje al conductor

    def click_label_message_driver(self):
        self.driver.find_element(*self.message_driver_click).click()

    def to_be_clickable_message_driver(self):
        WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable(self.message_driver_click))

    def set_message_to_driver(self):
        self.driver.find_element(*self.message_driver_input).send_keys(data.MESSAGE_FOR_DRIVER)

    def get_message_value(self):
        return self.driver.find_element(*self.message_driver_input).get_attribute("value")

    # requisitos de manta y helado


    def click_requirements_ice_cream_option(self):
        self.driver.find_element(*self.requirements_ice_cream_mantle_options).click()

    def set_requirements_mantle(self):
        self.driver.find_element(*self.requirements_switch).click()

    def set_requirements_ice_cream(self):
        self.driver.find_element(*self.requirements_plus_iceCream).click()
        self.driver.find_element(*self.requirements_plus_iceCream).click()

    def to_be_clickable_requirements_ice_cream_mantle(self):
        WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable(self.requirements_ice_cream_mantle_options))

    def to_be_clickable_requirements_mantle(self):
        WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable(self.requirements_switch))

    def to_be_clickable_requirements_ice_cream(self):
        WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable(self.requirements_plus_iceCream))

    #call a taxi modal
    def to_be_visible_call_a_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.call_a_taxi_button))

    def click_call_a_taxi_button(self):
        self.driver.find_element(*self.call_a_taxi_button).click()

    def get_call_a_taxi_button_value(self):
        return self.driver.find_element(*self.call_a_taxi_button_header).text

    def to_be_visible_searching_taxi_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.searching_taxi_button_header))

    def get_searching_taxi_header(self):
        return self.driver.find_element(*self.searching_taxi_button_header).text










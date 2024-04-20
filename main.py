import data
import time
import pages
from selenium import webdriver


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        import time
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.to_and_get_address_to_be_visible()
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # prueba para agregar el tipo de tarifa
    def test_set_comfort_type(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.ask_taxi_button_to_be_visible()
        routes_page.ask_taxi_click()
        routes_page.type_picker_section()
        routes_page.click_comfort()
        assert routes_page.type_picker_section

    # Prueba para agregar numero de telefono
    def test_set_phone_number(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.open_modal_phone_number()
        routes_page.to_be_visible_phone_number_modal()
        routes_page.click_label_phone_number()
        routes_page.set_phone_number()
        routes_page.click_next_phone_number()
        routes_page.to_be_visible_phone_number_code_modal()
        routes_page.click_label_code()
        routes_page.set_code()
        routes_page.click_next_phone_number_code()
        assert routes_page.get_phone_number() == data.PHONE_NUMBER

    # Prueba para agregar metodo de pago
    def test_set_payment_method(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_open_modal_payment_method()
        routes_page.to_be_visible_add_card_modal()
        routes_page.click_add_card_inside_modal()
        routes_page.to_be_visible_card_code_inputs()
        routes_page.set_payment_method_card_number()
        routes_page.to_be_visible_card_code_inputs()
        routes_page.set_cvv()
        routes_page.to_be_clickable_card_code_add()
        routes_page.click_next_payment_method()
        routes_page.to_be_visible_close_payment_method_click()
        routes_page.close_payment_method_click()
        assert routes_page.get_payment_method_value() == 'Card'

    # Prueba para mensaje al conductor
    def test_set_message_to_driver(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.to_be_clickable_message_driver()
        routes_page.click_label_message_driver()
        routes_page.set_message_to_driver()
        time.sleep(3)
        assert routes_page.get_message_value() == data.MESSAGE_FOR_DRIVER

    # Prueba para poner los requisitos
    def test_set_mantle_and_ice_cream(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.to_be_clickable_requirements_ice_cream_mantle()
        routes_page.click_requirements_ice_cream_option()
        routes_page.to_be_clickable_requirements_mantle()
        routes_page.set_requirements_mantle()
        routes_page.to_be_clickable_requirements_ice_cream()
        routes_page.set_requirements_ice_cream()

    def test_call_a_taxi_button(self):
        routes_pages = pages.UrbanRoutesPage(self.driver)
        routes_pages.to_be_visible_call_a_taxi_button()
        assert routes_pages.get_call_a_taxi_button_value() == 'Call a taxi'
        routes_pages.click_call_a_taxi_button()
        routes_pages.to_be_visible_searching_taxi_header()
        assert routes_pages.get_searching_taxi_header() == 'Car search'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

import data
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar!
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    type_picker = (By.CSS_SELECTOR, '.type-picker shown')


#Numero de telfono
    number_open_modal = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    number_modal = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]')
    #Darle clikc a este para poder poner el numero de telefono
    number_input_click = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/label')
    number_input = (By.ID, 'phone')
    number_input_label = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[1]/div[1]')
    number_modal_next = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    number_modal_code_next = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

#Metodo de pago
    payment_method = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    payment_method_modal = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]')
    add_card_modal = (By.CSS_SELECTOR, '.pp-plus-container')
    add_card_modal_inputs = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]')
    add_card_number_input = (By.ID, 'number')
    add_card_CVV = (By.ID, 'code')
    add_card_CVV_XPATH = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]')
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_payment_method_modal = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    payment_method_value = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
    click_out_of_focus = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div')

#Mensaje para el conductor
    message_driver_click = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div')
    message_driver_input = (By.ID, 'comment')

#Requisitos para el pedido
    requirements = (By.CSS_SELECTOR, 'reqs-header')
    requirements_ice_cream_mantle_options = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[2]/div')
    requirements_switch = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
    requirements_plus_iceCream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')


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

    def get_personal(self):
        return self.driver.find_element(*self.to_field)

#Pedir un taxi
    def ask_taxi_click(self):
        self.driver.find_element(*self.ask_taxi).click()

    def type_picker_section(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.type_picker))


#Pedir tarifa comfort
    def click_comfort(self):
        self.driver.find_element(*self.comfort_button).click()

#Agregar numero de telefono
    def open_modal_phone_number(self):
        self.driver.find_element(*self.number_open_modal).click()

    #esta funcion sirve para habilitar el input y poder escribir. (poner await para poder empezar a escrbiir)
    def click_label_phone_number(self):
        self.driver.find_element(*self.number_input_click).click()

    def set_phone_number(self):
        self.driver.find_element(*self.number_input).send_keys(data.phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.number_open_modal).text

    def click_next_phone_number(self):
        self.driver.find_element(*self.number_modal_next).click()

    def click_label_code(self):
        self.driver.find_element(*self.number_input_label).click()

    def set_code(self):
        self.driver.find_element(*self.add_card_CVV).send_keys(retrieve_phone_code(self.driver))

    def click_next_phone_number_code(self):
        self.driver.find_element(*self.number_modal_code_next).click()

#Payment Method

    def click_open_modal_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def click_label_card_number(self):
        self.driver.find_element(*self.add_card_number_input).click()

    def click_add_card_inside_modal(self):
        self.driver.find_element(*self.add_card_modal).click()

    def set_payment_method_card_number(self):
        self.driver.find_element(*self.add_card_number_input).send_keys(data.card_number)
        self.driver.find_element(*self.add_card_number_input).send_keys(Keys.TAB)

    def click_label_cvv(self):
        self.driver.find_element(*self.add_card_CVV_XPATH).click()

    def set_cvv(self):
        self.driver.find_element(*self.add_card_CVV).send_keys(data.card_code)

    def click_next_payment_method(self):
        self.driver.find_element(*self.add_card_button).click()

    def close_payment_method_click(self):
        self.driver.find_element(*self.close_payment_method_modal).click()

    def get_payment_method_value(self):
        return self.driver.find_element(*self.payment_method_value).text

    def click_out_of_focus_header(self):
        self.driver.find_element(*self.click_out_of_focus).click()


 #Mensaje al conductor

    def click_label_message_driver(self):
        self.driver.find_element(*self.message_driver_click).click()

    def set_message_to_driver(self):
        self.driver.find_element(*self.message_driver_input).send_keys(data.message_for_driver)

#requisitos de manta y helado

    def set_requirements(self):
        self.driver.find_element(*self.requirements).click()

    def click_requirements_ice_cream_option(self):
        self.driver.find_element(*self.requirements_ice_cream_mantle_options).click()

    def set_requirements_mantle(self):
        self.driver.find_element(*self.requirements_switch).click()

    def set_requirements_ice_cream(self):
        self.driver.find_element(*self.requirements_plus_iceCream).click()
        self.driver.find_element(*self.requirements_plus_iceCream).click()



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
        time.sleep(5)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(5)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        #routes_page.set_route(address_from, address_to)
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
#prueba para agregar el tipo de tarifa
    def test_set_comfort_type(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(3)
        routes_page.ask_taxi_click()
        time.sleep(3)
        routes_page.click_comfort()
        assert routes_page.type_picker_section
#Prueba para agregar numero de telefono
    def test_set_phone_number(self):

        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(3)
        routes_page.open_modal_phone_number()
        time.sleep(2)
        routes_page.click_label_phone_number()
        time.sleep(1)
        routes_page.set_phone_number()
        time.sleep(2)
        routes_page.click_next_phone_number()
        time.sleep(1)
        routes_page.click_label_code()
        time.sleep(1)
        routes_page.set_code()
        time.sleep(1)
        routes_page.click_next_phone_number_code()
        time.sleep(3)
        assert routes_page.get_phone_number() == data.phone_number
#Prueba para agregar metodo de pago
    def test_set_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        routes_page.click_open_modal_payment_method()
        time.sleep(2)
        routes_page.click_add_card_inside_modal()

        #time.sleep(2)
        #routes_page.click_label_cvv()
        time.sleep(2)
        routes_page.set_payment_method_card_number()
        time.sleep(6)
        routes_page.set_cvv()

        time.sleep(6)

        routes_page.click_next_payment_method()
        time.sleep(2)
        routes_page.close_payment_method_click()
        time.sleep(2)
        assert routes_page.get_payment_method_value() == 'Tarjeta'
#Prueba para mensaje al conductor
    def test_set_message_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_label_message_driver()
        time.sleep(2)
        routes_page.set_message_to_driver()
        assert routes_page.message_driver_input == data.message_for_driver
#Prueba para poner los requisitos
    def test_set_mantle_and_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_requirements()
        time.sleep(2)
        routes_page.click_requirements_ice_cream_option()
        time.sleep(2)
        routes_page.set_requirements_mantle()
        time.sleep(2)
        routes_page.set_requirements_ice_cream()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

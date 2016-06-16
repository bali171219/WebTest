from selenium import webdriver
from src.WebTestSample.WebTestResources import ObjectRepository


class CommonFlows:
    def __init__(self):
        print('Initialize common functions')
        self.driver = None

    def get_or_create_web_driver(self):
        print('Called get_or_create_web_driver')
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1440, 850)
        self.driver.set_window_position(0, 0)
        self.driver.implicitly_wait(1)
        return self.driver

    def get_xpath(self,array):
        tag_type = array[0]
        tag_attribute = array[1]
        attribute_value = array[2]
        if len(array) > 3:
            parent_tag_attribute = array[3]
            parent_attribute_value = array[4]
            xpath = str("// *[ " + parent_tag_attribute + "= '" + parent_attribute_value + "'] " + "//" + tag_type + "[" + tag_attribute + "='" + attribute_value + "']")
        else:
            xpath = str("//" + tag_type + "[" + tag_attribute + "='" + attribute_value + "']")
        print('xpath = ' + xpath)
        return xpath

    def element(self, element):
        print('Get ' + element)
        element_array = ObjectRepository.WebElements[element]
        xpath = self.get_xpath(element_array)
        element_location = self.driver.find_element_by_xpath(xpath)
        return element_location

    def google_search(self, search_term):
        print('Google ' + search_term)
        self.driver.get('https://www.google.com')
        if 'Google' not in self.driver.title:
            print('Did not make it to Google')
        self.element('google_search_box').send_keys(search_term)
        self.element('google_search_button').click()
        self.element('More').click()

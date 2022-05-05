from Locators.Locators import Locators
from selenium.webdriver.common.by import By


class TextBoxPage():
    def __init__(self, driver):
        self.driver = driver

    def enter_Full_Name(self, Full_Name):
        self.driver.find_element(By.ID, Locators.Full_Name_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.Full_Name_textbox_id).send_keys(Full_Name)

    def enter_Email(self, Email):
        self.driver.find_element(By.ID, Locators.Email_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.Email_textbox_id).send_keys(Email)

    def enter_Current_Address(self, Current_Address):
        self.driver.find_element(By.ID, Locators.Current_Address_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.Current_Address_textbox_id).send_keys(Current_Address)

    def enter_Permanent_Address(self, Permanent_Address):
        self.driver.find_element(By.ID, Locators.Permanent_Address_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.Permanent_Address_textbox_id).send_keys(Permanent_Address)

    def click_Submit_button(self):
        self.driver.find_element(By.ID, Locators.Submit_button_id).click()

    def reg_name_text(self):  #After submiting
        return self.driver.find_element(By.ID, Locators.reg_name_id).text

    def reg_email_text(self):  #After submitting
        return self.driver.find_element(By.ID, Locators.reg_email_id).text

    def reg_Permananet_Address_text(self):  #After submitting
        return self.driver.find_element(By.XPATH, Locators.reg_Permananet_Address_xpath).text

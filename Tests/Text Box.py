from selenium import webdriver
import unittest
from Pages.TextBoxPage import TextBoxPage
from selenium.webdriver.common.by import By

PATH = "C:/Users/User/PycharmProjects/TesvanHomework/Drivers/chromedriverwin32.exe"
driver = webdriver.Chrome(PATH)


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_submit_valid(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        title_of_web_page = driver.title
        self.assertEqual("ToolsQA", title_of_web_page, "Webpages titles are not same")
        page_name = driver.find_element(by=By.CLASS_NAME, value="main-header").text
        assert 'Text Box' in page_name  # Check that page is opened
        submit = TextBoxPage(driver)
        submit.enter_Full_Name("TesvanTest")  # Fill in all fields on the page
        submit.enter_Email("Tesvan@mail.ru")
        submit.enter_Current_Address("Andraniki154")
        submit.enter_Permanent_Address("Andraniki 90")
        submit.click_Submit_button()

        assert "Name:TesvanTest" in submit.reg_name_text()  # Check a new item is added with correct information
        assert "Email:Tesvan@mail.ru" in submit.reg_email_text()
        assert "Permananet Address :Andraniki 90" in submit.reg_Permananet_Address_text()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

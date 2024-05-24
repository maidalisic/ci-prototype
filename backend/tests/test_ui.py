import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_calculator_ui(self):
        driver = self.driver
        driver.get("http://localhost:3000")  # Passe die URL an, falls nötig

        try:
            # Warte, bis das Eingabefeld sichtbar ist
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Type an expression"]'))
            )
            submit_button = driver.find_element(By.XPATH, '//button[text()="Calculate"]')

            # Gebe einen Ausdruck ein und klicke auf den Button
            input_field.send_keys("1+3*3*(3+4*2)")
            submit_button.click()
            
            # Warte auf das Ergebnis
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Result:")]'))
            ).text

            # Überprüfe das Ergebnis
            self.assertIn("Result: 100", result)
        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()

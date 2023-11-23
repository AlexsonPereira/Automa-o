from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

with open("usernames.txt", "r") as my_file:
    for i in my_file.readlines():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        driver.get("https://095bet.com")

        wait = WebDriverWait(driver, timeout=20)
        wait.until(
            lambda d: driver.find_element(
                By.CLASS_NAME, "ant-modal-body"
            ).is_displayed()
        )

        x_path_btn_login = "/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div[2]/div[4]/div/div[2]/button"
        print(driver.find_element(By.XPATH, x_path_btn_login))

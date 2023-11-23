import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://095bet.com")

wait = WebDriverWait(driver, timeout=20)
wait.until(
    lambda d: driver.find_element(By.CLASS_NAME, "ant-modal-body").is_displayed()
)

inputs = driver.find_elements(By.TAG_NAME, "input")

for i in inputs:
    value = i.get_attribute("placeholder")
    match value:
        case "Nome de Usuário":
            username = ""
            for x in range(16):
                username += chr(random.randint(ord("a"), ord("z")))
            i.send_keys(username)
            with open("usernames.txt", "a") as my_file:
                my_file.write(f"{username}\n")
        case "Senha":
            i.send_keys("alexson1203")
        case "Confirme a senha":
            i.send_keys("alexson1203")
        case "Nome completo":
            i.send_keys("Alexson Pereira")

button_register = driver.find_element(By.CLASS_NAME, "ant-btn-block")
button_register.click()

wait.until(
    lambda d: driver.find_element(
        By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div"
    ).is_displayed()
)

driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/button").click()

wait.until(
    lambda d: driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div"
    ).is_displayed()
)
driver.find_element(
    By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div"
).click()

wait.until(
    lambda d: driver.find_element(
        By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/button"
    ).is_displayed()
)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/button").click()


driver.get("https://095bet.com/home/event")

wait.until(
    lambda d: driver.find_element(
        By.XPATH,
        '/*[@id="home-scroll-box"]/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/section/div[2]/div/ul/div[5]/div/div/li/div/div',
    ).is_displayed()
)
driver.find_element(
    By.XPATH,
    '/*[@id="home-scroll-box"]/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/section/div[2]/div/ul/div[5]/div/div/li/div/div',
).click()

driver.find_element(
    By.XPATH,
    "/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/span/input",
).send_keys("09555")


driver.find_element(
    By.XPATH,
    "/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/button",
).click()


# btn_modal_close = driver.find_element(By.CLASS_NAME, "ant-modal-close-x")
# btn_modal_close.click()

# btn_modal2_close = driver.find_element(By.CLASS_NAME, "_EzcaSyM6xzUnvRuU5nv")
# btn_modal2_close.click()

# btn_modal_close = driver.find_element(By.CLASS_NAME, "ant-modal-close-x")
# btn_modal_close.click()


# xpath register sucess = /html/body/div[7]/div/div[2]/div/div[2]/div
# xpath register sucess btn close  = /html/body/div[7]/div/div[2]/div/div[2]/button
# xpath conivide btn close = /html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div
# deposito = /html/body/div[6]/div/div[2]/div/div[2]/button
# Eventos = //*[@id="app"]/div[1]/section/section/aside/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div[1]
# codigo = //*[@id="home-scroll-box"]/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/section/div[2]/div/ul/div[5]/div/div/li/div/div
# codigo input = /html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/span/input
# btn reeinvidicar = /html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/button

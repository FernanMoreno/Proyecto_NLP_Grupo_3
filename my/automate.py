# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# import pandas as pd

# options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
# options.add_argument('--disable-extensions')

# driver_path = 'C:\\Users\\maikol\\Downloads\\chromedriver_win64\\chromedriver.exe'

# # Configura el controlador con la ruta del ejecutable del controlador
# driver = webdriver.Chrome(driver_path, chrome_options=options)

# driver.set_window_position(2000, 0)
# driver.maximize_window()
# time.sleep(1)

# driver.get('https://www.ejemplo.com')





# url = 'https://www.facebook.com'

# driver = webdriver.Chrome()
# driver.get(url)
# source = driver.page_source









from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# Abre el sitio web de YouTube
url = 'https://www.youtube.com'
driver.get(url)


wait = WebDriverWait(driver, 20)
cookie_banner = wait.until(EC.presence_of_element_located((By.ID, "dialog")))  # Reemplaza "cookie-banner" con el ID real del banner

# # Encuentra y hace clic en el botón de aceptar cookies (puedes ajustar el atributo según sea necesario)
accept_button = cookie_banner.find_element(By.CLASS_NAME, "yt-spec-button-shape-next--filled")  # Reemplaza "accept-cookies-button" con el ID real del botón
accept_button.click()

# Forzar una recarga de la página
driver.refresh()


search_box = driver.find_element_by_id("search")

# Borra cualquier texto existente en el campo de búsqueda
search_box.clear()

# Escribe el término de búsqueda que desees, por ejemplo, "Los Simpson"
search_box.send_keys("Los Simpson")

# driver.refresh()

# Espera hasta que el campo de búsqueda sea interactable
wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.visibility_of_element_located((By.NAME, "search_query")))
# search_box.clear()
# search_box.send_keys("Los Simpson")
# search_box.send_keys(Keys.RETURN)

# # Borra cualquier texto existente en el campo de búsqueda
# search_box.clear()

# search_box.send_keys("Los Simpson")  # Cambia "Los Simpson" por el término de búsqueda que desees
# search_box.send_keys(Keys.RETURN)

# # Espera a que se carguen los resultados de búsqueda
# wait.until(EC.presence_of_element_located((By.ID, "contents")))


# Espera la entrada del usuario antes de cerrar la ventana
input("Presiona Enter para cerrar la ventana del navegador...")

# Cierra el navegador
driver.quit()


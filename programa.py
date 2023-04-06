#Librerias
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os
from datetime import datetime

class MyTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")

    def test_titulo(self):
            self.assertEqual(self.driver.title, "Example Domain")
            self.driver.save_screenshot("screenshots/screenshot1.png")
            self.assertTrue(os.path.isfile("screenshots/screenshot2.png"))


    def test_link(self):
        link = self.driver.find_element_by_tag_name("a")
        self.assertEqual(link.get_attribute("href"), "https://www.iana.org/domains/example")


    def test_capturas(self):
            self.assertEqual(self.driver.title, "Example Domain")
            self.assertTrue(os.path.isfile("screenshots/screenshot1.png"))
            self.assertTrue(os.path.isfile("screenshots/screenshot2.png")) 
            self.assertTrue(os.path.isfile("screenshots/screenshot3.png")) 
            self.assertTrue(os.path.isfile("screenshots/screenshot4.png")) 
            self.assertTrue(os.path.isfile("screenshots/screenshot5.png"))   

    def test_descarga(self):
        self.driver.find_element_by_link_text("Download").click()
        downloaded_file = os.path.join("C:\\Users\\Dell\\Downloads", "icalexport.ics")
        self.assertTrue(os.path.isfile(downloaded_file))

    def test_calificacion(self):
            self.assertEqual(self.driver.title, "Example Domain")
            self.assertTrue(os.path.isfile("calificaciones.png"))

    def tearDown(self):
        self.driver.quit()




#Carpeta y nombres de las capturas de pantalla
folder = 'screenshots'
filename1 = f'screenshot1.png'
filename2 = f'screenshot2.png'
filename3 = f'screenshot3.png'
filename4 = f'screenshot4.png'
filename5 = f'screenshot5.png'
calificaciones = f'calificaciones.png'

#Opciones para la navegación
options = webdriver.ChromeOptions()
options.add_argument('--start--maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Dell\\Desktop\\tarea4\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

#Iniciar navegador
driver.get('https://plataformavirtual.itla.edu.do/login/index.php')

#Pantalla completa
driver.maximize_window()

#Iniciar sesion correctamente
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
login = driver.find_element_by_id("loginbtn")
username.send_keys("202010320")
password.send_keys("Eldestructor1#")
login.click()

#Tomar captura
filepath1 = os.path.join(folder, filename1)
driver.get_screenshot_as_file(filepath1)
time.sleep(3)


#Informe de notas
nota = driver.find_element_by_xpath("/html/body/div[2]/nav/div[1]/button/i")
nota.click()
time.sleep(1)
nota1 = driver.find_element_by_xpath("/html/body/div[2]/div[4]/nav/ul/li[10]/a/div/div/span[2]")
nota1.click()
time.sleep(2)
nota2 = driver.find_element_by_xpath("/html/body/div[2]/div[4]/nav[1]/ul/li[5]/a/div/div/span[2]")
nota2.click()
time.sleep(2)
nota3 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div/section/div/div/ul/li[1]/a")
nota3.click()
driver.execute_script("window.scrollBy(0, 300);")

#Tomar captura
cali = os.path.join(folder, calificaciones)
driver.get_screenshot_as_file(calificaciones)

area_personal = driver.find_element_by_xpath("/html/body/div[1]/nav/a/span[1]/img")
area_personal.click()
time.sleep(2)


#Ingresar al Calendario
barra = driver.find_element_by_xpath("/html/body/div[2]/nav/div[1]/button/i")
barra.click()
time.sleep(1)
calendario = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/section[1]/div[1]/div/div/div/div[1]/div/div/div[2]/a")
calendario.click()

#captura de pantalla
filepath2 = os.path.join(folder, filename2)
driver.get_screenshot_as_file(filepath2)

#Presionar boton de Exportar
time.sleep(2)
exportar = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/section[1]/div/div/div[2]/div[1]/form/button")
exportar.click()

#Seleccionar casillas y exportar el calendario
time.sleep(2)
boton1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/section[1]/div/div/form/div[2]/div[2]/fieldset/div/label[3]/input")
boton1.click()
boton2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/section[1]/div/div/form/div[3]/div[2]/fieldset/div/label[1]/input")
boton2.click()
exportar_todo = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/section[1]/div/div/form/div[4]/div[2]/fieldset/div/div[2]/span/input")
exportar_todo.click()

#Tomar captura
filepath3 = os.path.join(folder, filename3)
driver.get_screenshot_as_file(filepath3)


#Cerrar sesion
time.sleep(2)
cerrar = driver.find_element_by_xpath("/html/body/div[2]/nav/ul[2]/li[2]/div/div/div/div/div/a/span/span[2]/span/img")
cerrar.click()
time.sleep(2)

#Tomar captura
filepath4 = os.path.join(folder, filename4)
driver.get_screenshot_as_file(filepath4)

#Cerrar sesion
cerrar1 = driver.find_element_by_xpath("/html/body/div[2]/nav/ul[2]/li[2]/div/div/div/div/div/div/a[7]/span")
cerrar1.click()
time.sleep(1)

#Tomar captura
filepath5 = os.path.join(folder, filename5)
driver.get_screenshot_as_file(filepath5)

time.sleep(3)
driver.close()


unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
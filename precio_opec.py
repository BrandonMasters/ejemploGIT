#Programa que obtiene datos de la página datosmacroexpansion:
#Importando librerías:
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


#Instalando ChromeDriverManager, si ya está instalado sólo crea la variable driver:
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Se almacena la direccion de la web en la variable url:
url = "https://www.opec.org/basket/basketDayArchives.xml"

#Fecha actual:
fecha_archivo = datetime.now().date().strftime('%Y_%m_%d')

#Con driver se realiza la petición get():
driver.get(url)
html = driver.page_source

#Listas para almacenar las fechas, los precios por barril y los valores del documento html:
fechas = []
precios = []
valores = []
lista_nueva = []

#Se crea una variable de la clase Beautifulsoup y se le pasa como argumento el str del html y se le indica que es html
soup = BeautifulSoup(html, 'html.parser')

#Mediante soup busca el div con clase "opened", este contiene todas las fechas y precios:
cuerpo_html = soup.find(class_ = "opened")

#Con un ciclo for busca elemento por elemento hasta encontrar aquellos con el atributo "html-attribute-value" para almacenarlos en
#la lista valores:
for e in cuerpo_html.find_all(class_ = "html-attribute-value"):
    valores.append(e.text)

#Luego itera desde el elemento 0 hasta el ultimo y verifica si cada indice del elemento es impar o par. Esto se realiza para
#almacenar los valores impares en fechas y los pares en precios:
for i in range(len(valores)):
    if (i+1) % 2 != 0:
        fechas.append(valores[i])
    else:
        precios.append(valores[i])

#Se crea un dataframe con las listas obtenidas:

df = pd.DataFrame(
    {
        "Fechas" : fechas,
        "Precio petróleo ($USD/Bl)" : precios
    }
)

df.to_csv(f"C:\\Users\\regg6\\OneDrive - regulus.com.mx\\Documentos\\Archivos_regulus\\Cenace\\Web scraping\\Precio petroleo OPEP\\Precio_petroleo.csv")






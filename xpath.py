import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# Varianta veche de instantiere a driver-ului:
# chrome = webdriver.Chrome("cale_catre_webdriver_descarcat_local")

# Varianta de instantiere a driver-ului dupa selenium 4.0
chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Varianta de instantiere a driver-ului dupa selenium 4.6
# chrome = webdriver.Chrome()

# chrome.get("https://the-internet.herokuapp.com/login")

"""
XPATH = o adresa in codul HTML la care putem sa identificam un anumit element
/html/body/div[2]/div/div/form/div[1]/div/input - XPATH Absolut -> Care porneste de la inceputul paginii web
//*[@id="last-name"] - XPATH Relativ -> Care porneste de la un anumit element unic identificabil pe pagina
La Xpath filtrarea pe baza de atribut = valoare se face prin plasarea caracterului @ in fata atributului
"""

# 1.Cautare dupa atribut = valoare pentru un tag specific
"""
Modalitati de identificare a userului pe baza de atribut = valoare
//input[@type="text"]
//input[@name="username"]
//input[@id="username"]
"""
#
# chrome.find_element(By.XPATH,'//input[@type="text"]').send_keys("tomsmith")
#
# # 2.Cautare dupa atribut = //*[@type="text"]valoare indiferent de tag
# chrome.find_element(By.XPATH,'//*[@type="text"]').send_keys("tomsmith")
#
# # 3. Cautare dupa copil prin navigare in jos
# """
# Cautarea dupa copil se face prin plasarea caracterului "/" intre parinte si copil
# """
#
# chrome.find_element(By.XPATH,'//form/div/div/input[@type="text"]').send_keys("tomsmith")
# chrome.find_element(By.XPATH,'//form/div[@class="row"][2]/div[@class="large-6 small-12 columns"]')

chrome.get("https://formy-project.herokuapp.com/form")
# 4. Cautare cu OR - Ambele conditii sunt adevarate
# chrome.find_element(By.XPATH,"//input[@placeholder='Enter first name'] | //*[@placeholder='Enter last name']").send_keys("Cautare cu OR")
# time.sleep(3)

time.sleep(3)
# 5. Cautare cu OR - Doar a doua conditie este adevarata
# chrome.find_element(By.XPATH,"//input[@placeholder='Enter first names'] | //*[@placeholder='Enter last name']").send_keys("Cautare cu OR")
# time.sleep(3)

# 6. Cautare cu OR - Nicio conditie nu este adevarata
# chrome.find_element(By.XPATH,"//input[@placeholder='Enter first names'] | //*[@placeholder='Enter last names']").send_keys("Cautare cu OR")


# 7. Tratare dropdown
"""
Atunci cand avem de un dropdown, primul lucru pe care il facem este sa verificam daca a fost creat cu clasa Select
Pentru a interactiona cu un dropdown, atunci vom instantia un obiect din clasa Select, care clasa va primi ca argument
				pentru constructor rezultatul metodei find_element 

Prin intermediul obiectului vom avea acces la toate metodele si atributele din clasa Select, inclusiv la metoda select_by_visible_text
"""
# years_of_experience = Select(chrome.find_element(By.ID,"select-menu"))
# time.sleep(2)
# years_of_experience.select_by_visible_text("5-9")
# time.sleep(2)
# years_of_experience.select_by_visible_text("0-1")
# time.sleep(2)

chrome.find_element(By.ID, 'radio-button-1').click()

time.sleep(3)
# """
# x y axis navigation
# 1. Navigare din parinte in copil se face cu caracterul /
# 2. Navigare catre un urmas care nu e urmas direct se face cu caracterul //
# 3. Navigarea in sus catre parent se poate face cu "/parent::tag"
# 4. Putem sa navigam la urmatorul frate cu "/following-sibling::tag"
# 5. Putem as navigam la fratele anterior cu "/preceding-sibling::tag"
# //a[@class="forgot-password"]/preceding-sibling::div[1]/div/button
# //a[@class="btn btn-primary btn-block"]/preceding-sibling::ul/li/following-sibling::li[3]
# //ul[@class="search-suggest-results"]/preceding-sibling::button/following-sibling::div
"""
Structura unei pagini web ete definita pe baza unui limbaj de programare numit HTML
Aspectul si stilizarea unei pagini este definita pe baza unui limbaj numit CSS

HTML = Hyper Text Markup Language -> un limbaj de programare frontend care este
                        utilizat pentru a defini functionalitatea unui site web
                        - structura
                        - ce meniuri are site-ul
                        - daca are mai multe pagini din care este compus
                        - daca paginile sunt legate intre ele
                        - daca exista necesitatea inputului de la tastatura
                        - daca trebuie apasate butoane
Pentru a accesa codul HTML al unui site web trebuie sa dam click dreapta pe pagina si sa dam inspect.
Daca ne intereseaza codul HTML al unui element specific (de exemplu buton),
vom da click si inspect pornind de la acel element.

Exemple de elemente:
- buton
- input
- p (paragraph)
- a (anchor -> legatura catre alta pagina)
- span ( de regula defineste un text peste un alt element( de ex: textul "login" peste buton))
            sau proprietati ale elementelor care sunt comune cu cele de la alte elemente

CSS = Cascading Style Sheets -> este un limbaj de programare de tip frotend care
            definete felul in care este stilizat site-ul.

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


"""
ID-ul in general este cea mai simpla si sigura metoda de a indentifica un element in interfata
In general reprezinta un identificator unic pentru un element specific
            dar di unele situatii, desi extrem de rare in care pot sa fie doua elemente cu acelasi id.
            In cazul acesta trebuie sa gasim alta metoda de identificare a eementului in codul HTML
            
"""
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
                                    # am insttalat un obiect al clasei Chrome din libraria Webdriver
                                    # prin intermediul acestui obiect vom avea aces la toate metodele
                                    #si atributele din clasa Chrome
                                    # inclusiv la metoda webdriver-manager



time.sleep(3) # instruim sistemul sa astepte trei secunde inainte sa execute urmatoarea insctructiune

"""
sleep = metoda prin care punem pauza in cod timp de o perioada de o perioada bine definita care va fi 
        respetata ad-literam de catre sistem.
        
implicitly_wait() = metoda prin care sistemul va cauta un element timp de o perioada determinata:
                    - daca elemetul este gasit mai devreme, atunci executa urmatoarea instructiune
                    - daca elementul nu este gasit pana cand tipul alocat expira, atunci sistemul va 
                    returna eroare.
                    Este util in conceptul de RANDARE al paginii - uneori paginile web se pot incarca
                    mai greu ceea ce inseamna ca unele elemente nu vor fi vizibile imediat
                    Implicit wait este global si va acoperi orice element scris in fisierul curent
                    
                    
explicit_wait() = metoda prin care sistemul va cauta un element timp de o perioada determinata
                - daca elementul este gasit mai devreme, atunci va executa urmatoarea instructiune fara
                 sa mai astepte
                - daca ementul nu este gasit pana timpul alocat expira, atunci sitemul va returna eroare
                Este util in conceptul de RANDARE al paginii - uneori paginile web se pot incarca mai greu
                ceea ce inseamna ca unele elemente nu vor fi vizibile imediat
                Explicit wait NU este global si va acopri doar elementul pentru care este scris
                
                
Expemplu:
Vrem sa cautam un element cu id-ul username pe site-ul herokkuapp.com
Sistemul va cauta acel element, si daca il va gasi va trece instant la instructiunea urmatoare
Daaca nu il va gasi, sistemul va returna eroare in felul urmator:
a) Implicit wait
Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in implicit wait dupa care 
va da eroare
Daca nu am avea acel implicit wait, ar returna eroare instant
b)Sleep
b.1. Daca avem sleep inainte de element, atunci sistemul va astepta 5 secunde inainte sa caute elementul, 
apoi il va cauta si va returna eroare instant
b.2. Daca avem sleep inainte de element, atunci sistemul va returna eroare instant pentru ca nu va mai ajunge 
sa execute instructiunea de sleep
c) Explicit wait
Daca avem explicit wait pe elementul cautat, atunci se va astepta numarul de secunde definit in explicit wait 
dupa care va da eroare
Daca avem explicit wait pe un alt element decat elementul cautat, atunci sistemul va returna eroare instant
d) Implicit waint + explicit wait
Sistemul va tine cont de timpul definit in implicit wait care are prioritate fata de explicit wait, dupa care va 
returna eroare
                
"""

driver.maximize_window() # se foloseste pentru a maximiza fereastra astfel incat sa ne asiguram ca elementele sunt
                                                                                                            # vizibile
driver.get("https://formy-project.herokuapp.com/form") # putem deschide un site

"""
Pentru a cauta un elemnt, dam click dreapta si inspect pornind de la acel elemnt si se va abastru codul care 
identifica acel element
In momentul in care il gasim el va fi format din urmatoarele componente:
1. tag de inceput (<input>, <button>, <span>, <div>, <p>, <a>) -> tag = eticheta -> reprezinta o modalitate prin care
putem sa marcam un element ca fiind deun anumit tip
div = divide -> reprezinta o modaliate prin care putem sa impartim continutul site-ului in functie de enumite elemente
comune
Exemplu: putem sa punem toate elementele care apartin de un meniu intr-un div. Documentatie :
                                                                            https://www.w3schools.com/tags/tag_div.ASP
 2. perechi de tipul atribut = valoare care defineste diverse proprietati ale elementului
 Exemple:
 type = "text" (type = atribut, text = valoare)
 class = "form-control" (class = atribut, form-control = valoare)
 id = "first-name" (id = atribut, first-name = valoare)
 placeholder = "Enter first name" ( placeholder = atribut, Enter first name = valoare)
 
 
Atunci cand vrem sa facem cautare dupa perechi de tipul atribut = valoare trebuie sa le incadram intre paranteze patrare
 exemplu de cautare: [type="text"]

"""
driver.find_element(By.ID, "first-name"). send_keys("Marian")
"""
find_element este o metoda din clasa Chrome care primente doua argumente:
-metoda de cautare (Ex. By.ID)

- valoarea pentru aceametoda de cautare (Ex. first-name)


Dupa ce accesam functia find_element ni se returneaza un WebElement cu care se poate interactiona
Una din metodele cu care putem sa interactionam cu acel WebElement este metoda send_keys care este folosita
pentru a trimite text intr-un element de tip input. Metoda send_keys accepta un singur parametru care reprezinta
valoarea ce va fi scrisa in campul de tip input

"""

driver.find_element(By.ID, "last-name").send_keys("Gheoghisor")
time.sleep(3)
driver.quit() # inchide toata instanta browserului
#driver.close() -> inchide un singur tab (cel activ) din instanta de browser
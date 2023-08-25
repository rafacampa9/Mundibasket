from selenium.webdriver.support.ui import WebDriverWait


#para condiciones en selenium
from selenium.webdriver.support import expected_conditions as ec

#excepción de timeout en selenium
from selenium.common.exceptions import TimeoutException

#para definir que tipo de búsqueda voy a definir para el elemento
from selenium.webdriver.common.by import By



from iniciar_chrome.iniciar_chrome import iniciar_chrome












# ENTRAMOS A LA WEB DE UEFA ########################################################################
def fiba(year):
    print(year[0])
    driver = iniciar_chrome()
    wait = WebDriverWait(driver, 30)
    
        
    driver.get(
            f'https://www.los-deportes.info/baloncesto-campeonato-mundial-masculino-{year[0]}-epr{year[1]}.html'
            )
            
            
    
    print('Aceptando cookies...')     
    try:
        wait.until(
            ec.element_to_be_clickable(
                    (By.XPATH,
                    '//*[@id="sd-cmp"]/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/button[2]')
                    )
            ).click()
        print('COOKIES aceptadas.')
    except TimeoutException:
        print('ERROR: Botón COOKIES no encontrado')
                
        
        
    matches = []

    print('Buscando información.')
    try:
        elemento = wait.until(
            ec.visibility_of_any_elements_located(
                (By.CSS_SELECTOR,
                "table[class='table-style-2']"
                )
            )               
        )
        print('Info encontrada.')
    except TimeoutException:
        print('ERROR: Partidos no encontrados')

    matches = driver.find_elements(
            By.CSS_SELECTOR, 
            "table[class='table-style-2']"
                )
        
    partidos = []
                
                
    for match in matches:
        partidos.append(match.text)

    
    driver.quit()
    juego = []
    for partido in partidos:
        juego.append(partido.split('\n'))

    return juego



    
    
        


            

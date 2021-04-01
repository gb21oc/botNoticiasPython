#Criado por: Gabriel Jose
#No dia: 01/04/2021

import sys
import win32api  #pip install pywin32
import requests  # pip install requests
import schedule  #pip install schedule
from time import sleep
from line_txt import lineText
from bs4 import BeautifulSoup  # pip install beautifulsoup4
from selenium import webdriver  #Pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def remove_duplicates(list):
    l = []
    for i in list:
        if i not in l:
            l.append(i)
    return l


def noticesNow():
    global driver
    user_name = win32api.GetUserName()
    try:
        print("Iniciando processo...")
        page = requests.get(
            "https://www.google.com/search?safe=active&sa=X&hl=pt-PT&sxsrf=ALeKk03af9oDJDL8H6TMHQ-Q2h9BOwW_OA:1617280293510&q=noticias+hoje&tbm=nws&source=univ&tbo=u&ved=2ahUKEwiXhpbLht3vAhXeZzABHR6EBPUQt8YBKAJ6BAgFEAM&biw=1009&bih=625")
        soup = BeautifulSoup(page.content, 'html.parser')
        notices = soup.find_all(class_="BNeawe vvjwJb AP7Wnd")
        subNotices = soup.find_all(class_="BNeawe s3v9rd AP7Wnd")
        subNoticesText = []
        noticesText = []
        linkNotices = []
        dictionary = {}
        contatos = "nome_do_grupo"

        for notice in notices:
            noticesText.append(notice.text)

        for subNotice in subNotices:
            subNoticesText.append(subNotice.text)

        for link in soup.find_all('a'):
            linkNotices.append(link.get('href'))

        del linkNotices[0:18]
        for i in range(3):
            del linkNotices[-1]

        replaceLinks = []
        for replaceLink in linkNotices:
            replace = replaceLink.replace("/url?q=", "")
            replaceLinks.append(replace)

        indiceDel = [2, 2, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for i in indiceDel:
            del replaceLinks[i]

        subNoticesText = remove_duplicates(subNoticesText)
        noticesText = remove_duplicates(noticesText)
        lenNotices = len(noticesText)

        for i in range(lenNotices):
            dictionary[noticesText[i]] = f"*SUBTITULO*: {subNoticesText[i]} -> *LINK*: {replaceLinks[i]}\n"

        print("Guardando noticias...")
        with open(f'C:\\Users\\{user_name}\\Documents\\noticias.txt', 'a') as path:
            for key, value in dictionary.items():
                path.write(f"*TITULO*: {key} -> {value}\n")
            path.close()

        listText = lineText()
        print("Iniciando o chorme...")
        chorme_driver = f"C:\\tempPython\\chromedriver.exe"
        chrome_options = Options()
        #chrome_options.add_argument("headless")
        chrome_options.add_argument('--user-data-dir=./User_Data')
        driver = webdriver.Chrome(executable_path=chorme_driver, options=chrome_options)
        driver.get('https://web.whatsapp.com/')
        print("Só um momento...")
        sleep(10)

        print("No wpp web quase enviando as noticias do dia...")
        x = driver.find_element_by_xpath(
            f"//span[@title='{contatos}']")  # Achando o contato com o nome selecionado
        sleep(3)
        x.click()
        input = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]")
        sleep(3)
        print("Digitando as noticias....")
        input.click()
        input.send_keys(listText)
        sleep(1)
        btn = driver.find_element_by_xpath("//span[@data-testid='send']")
        sleep(3)
        btn.click()
        sleep(5)
        open(f'C:\\Users\\{user_name}\\Documents\\noticias.txt', 'w').close()
        driver.close()
        sys.exit()
    except NoSuchElementException:
        open(f'C:\\Users\\{user_name}\\Documents\\noticias.txt', 'w').close()
        driver.close()
        sys.exit()
    except IndexError:
        print("Ocorreu um erro desconhecido")
        open(f'C:\\Users\\{user_name}\\Documents\\noticias.txt', 'w').close()
        driver.close()
        sys.exit()


schedule.every().day.at("09:00").do(noticesNow)

while True:
    schedule.run_pending()


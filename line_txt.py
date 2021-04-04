import win32api
from datetime import datetime

def lineText():
    user_name = win32api.GetUserName()
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M")
    path = open(f'C:\\Users\\{user_name}\\Documents\\noticias.txt', 'r')
    first_line = path.readline()
    second_line = path.readline()
    third_line = path.readline()
    bedroom_line = path.readline()
    fifth_line = path.readline()
    sixth_line = path.readline()
    seventh_line = path.readline()
    eighth_line = path.readline()
    ninth_line = path.readline()
    tenth_line = path.readline()


    msg = f"\
          *--------------NOTICIAS DO DIA: {dateNow}----------*\n\
          {first_line}\n\
          {second_line}\n\
          {third_line}\n\
          {bedroom_line}\n\
          {fifth_line}\n\
          {sixth_line}\n\
          {seventh_line}\n\
          {eighth_line}\n\
          {ninth_line}\n\
          {tenth_line}"

    return msg

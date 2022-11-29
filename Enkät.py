
import datetime
from openpyxl import Workbook, load_workbook

tid_nu = datetime.datetime.now()
t_stamp = str(tid_nu.strftime(" '%y.%m.%d @ %H:%M:%S "))


#######om nya frågor ska läggas till, lägg int frågor först, o ändra i for-loopen ner
preguntas =  "Av 10 hur många?\n","Ålder?\n", "Ursprung?\n", "Vinnare?\n", "Feminin/Maskulin?\n"
doc = 'Undersökning.xlsx'
respuestas = []
usr = []
tabell = []


############################
def ny_data(delt, docu):

    wb = load_workbook(docu)
    ws = wb.active

    for i in range(len(delt)-1):
        ws.append(delt[i])
        
    ws.append(delt[-1])
    wb.save(docu)


############################
def enkät():
    while True:
        try:
            antal =int(input("Antal tillfrågade?\n"))
        except ValueError:
            print('Siffra tack!')
            continue


    ################### int loop 
        for i in range(2):
            for ii in range(antal):
                while True:
                    try:
                        c = int(input(preguntas[i]))
                        respuestas.append(c)
                        break
                    except ValueError:
                        print('Måste vara siffra!')
                        continue


    ################### str loop
        for i in range(2,len(preguntas)):
            for ii in range(antal):
                o = input(preguntas[i]) 
                respuestas.append(o)


    ################### varje deltagare blir lista
        for i in range(antal):
            temp = []

            for ii in range(0, len(respuestas),antal):
                temp.append(respuestas[i+ii])
            tabell.append(temp)

        tabell.append([t_stamp])


    ###################
        print(tabell)
        ny_data(tabell, doc)
        break


enkät()


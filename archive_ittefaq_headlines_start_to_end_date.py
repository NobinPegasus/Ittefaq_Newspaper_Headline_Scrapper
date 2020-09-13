import io

from bs4 import BeautifulSoup
import requests

id = 1
gap = ' '*10

f_name = 'info212.txt'

def old_news(year, month, date):    
    global id
    global gap
    base_url = 'https://www.ittefaq.com.bd/archive/online-edition'
    if(month <10 and date < 10):
        final_url5 = base_url + '/' + str(year) + '/0' + str(month) +'/0' + str(date)
        print(final_url5)
    elif(month < 10):
        final_url5 = base_url + '/' + str(year) + '/0' + str(month) +'/' + str(date)
        print(final_url5)
    elif(date < 10):
        final_url5 = base_url + '/' + str(year) + '/' + str(month) +'/0' + str(date)
        print(final_url5)


    source3 = requests.get(final_url5).text

    
    soup_3 = BeautifulSoup(source3, 'lxml')

    with io.open(f_name, "a", encoding="utf-8") as f:
            f.write('##########' +'     ' + final_url5[50:60] +'     ' +'##########')
            f.write('\n')
            f.write('\n')
    
    for artice in soup_3.find_all('li'):
        
        hu = artice.find('i',class_='fa fa-square-o')
        # print(hu)
        if(hu is not None):
            boo = artice.find('a')
            koo = boo.text
            with io.open(f_name, "a", encoding="utf-8") as f:
                f.writelines(str(id) + gap +koo)
                f.write('\n')
                id += 1
        
            
            print(koo)
    with io.open(f_name, "a", encoding="utf-8") as f:
            f.write('\n')

   

def date_from_to(fro, too):
    year_final = int(too[0:4])
    month_final = int(too[5:7])
    date_final = int(too[8:10])

    year_current = int(fro[0:4])
    # print(year_current , type(year_current))
    month_current = int(fro[5:7])
    # print(month_current , type(month_current))
    date_current = int(fro[8:10])

 

    while(year_current != year_final or month_current != month_final or date_final != date_current):
        
        old_news(year_current,month_current,date_current)

        date_current += 1
        if(date_current == 32):
            date_current = 31
            month_current += 1
            date_current = 1
            if(month_current == 13):
                month_current =12
                year_current += 1
                month_current = 1

        # print(year_current, 'year', month_current, 'month', date_current, 'date')

date_from_to('2020/02/15', '2020/02/25')

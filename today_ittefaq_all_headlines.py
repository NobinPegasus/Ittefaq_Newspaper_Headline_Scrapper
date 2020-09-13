from datetime import datetime
import io

from bs4 import BeautifulSoup
import requests

f_name = 'info1001.txt'

ui  = datetime.today().strftime('%Y/%m/%d')
with io.open(f_name, "a", encoding="utf-8") as f:
        f.write('##########' +'     ' + str(ui) +'     ' +'##########')
        
        f.write('\n')
        f.write('\n')

my_url = 'https://www.ittefaq.com.bd'

slash = '/'




sections = ['projonmo', 'national','politics','capital','worldnews','sports', 'entertainment','court','wholecountry','economy','education','scienceandtechnology','lifestyle','abroad','culture','budget','covid19-update','opinion','samoyiki','projonmo']
for i in range(len(sections)):


    with io.open(f_name, "a", encoding="utf-8") as f:
        f.write('---------' +'     ' + sections[i].upper() +'     ' + '---------')
        
        f.write('\n')
        f.write('\n')
    m_final_url = my_url + slash + sections[i]

    print(m_final_url)


    source = requests.get(m_final_url).text





    soup = BeautifulSoup(source, 'lxml')

    # print(soup)

 

    for artice in soup.find_all(['h4','h5']):
        hu = artice.text
        with io.open(f_name, "a", encoding="utf-8") as f:
            f.writelines(hu)
            f.write('\n')
        # fic =  open('info.txt', 'a')
        # fic.write(hu)
        print(artice.text)

    with io.open(f_name, "a", encoding="utf-8") as f:
            f.write('\n')
    # fic.close()
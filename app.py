import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://www.pandinthong.com/price/"  # Source URL
driver = webdriver.PhantomJS()
driver.get(url)
wait = WebDriverWait(driver, 3)
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'txt-loading')))

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()

price_list_json = []
price_data = ''
price_points = []


def date_to_millis(date):
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date + " 00:00:00", pattern)))
    return epoch


for tr in soup.find_all("li", class_="table-data-row"):
    tds = tr.find_all("span", class_="txt")
    if tds[0].text.isnumeric():
        print "Order: %s, ProvinceTH: %s, ProvinceEN: %s, Market: %s, TypeTH	: %s, TypeEN	: %s, Price (Baht): %s, unitTH	: %s, Change	: %s, DateTH	: %s ,DateEN	: %s, Source	: %s, epoch	: %s" % \
              (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text, tds[11].text, str(date_to_millis(tds[10].text)))
        data_row = 'product_th="' + tds[4].text \
                + '",product_en="' + tds[5].text \
                + '",province_th="' + tds[1].text \
                + '",province_en="' + tds[2].text \
                + '",market="' + tds[3].text \
                + '",price=' + (tds[6].text).replace(",","") \
                + ',unit="' + tds[7].text \
                + '",change="' + tds[8].text \
                + '",date_th="' + tds[9].text \
                + '",date_en="' + tds[10].text \
                + '",source="' + tds[11].text \
                + '",market_update="' + str(date_to_millis(tds[10].text)) + "000000000" \
                + '",value=' + (tds[6].text).replace(",","") \
                + ' ' + str(int(round(time.time()))) + "000000000\n"
        #print data_row
        json_data = {"oid": tds[0].text, "province_th": tds[1].text, "province_en": tds[2].text,
                     "market": tds[3].text, "product_th": tds[4].text, "product_en": tds[5].text, "price": tds[6].text,
                     "unit": tds[7].text, "change": tds[8].text, "date_th": tds[9].text, "date_en": tds[10].text,
                     "source": tds[11].text, "timestamp": date_to_millis(tds[10].text)}
        price_list_json.append(json_data)


# Printing price list in JSON format
print price_list_json

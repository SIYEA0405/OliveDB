import requests, re
from bs4 import BeautifulSoup
import categoryNo as category_numbers

def remove_brackets_reg_exp(pdname):
  return re.sub(r'\[.*?\]', '', pdname).strip()

# 각 카테고리별로 상품저장
def get_products_data(catNo, pageIdx=1):
    url = f'https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo={catNo}&fltDispCatNo=&prdSort=01&pageIdx={pageIdx}&rowsPerPage=48&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&trackingCd=Cat100000100010008_Small'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    large_ctg = soup.find('a', {'class': 'cate_y'}).text
    small_ctg = soup.find_all('h1')[1].text

    all_products_data = soup.find_all("div", {'class': 'prd_info'})
    for product_data in all_products_data:
      product_info_data = product_data.find("div", {"class": "prd_name"})
      product_price_data = product_data.find("p", {"class": "prd_price"}).find_all(class_='tx_num')

      name = product_info_data.find("p", {"class":"tx_name"}).text
      name = remove_brackets_reg_exp(name)
      brand =product_info_data.find("span", {"class":"tx_brand"}).text
      
      product_number = product_data.find("a").get("data-ref-goodsno")
      
      original_price = None
      current_price = None

      if len(product_price_data) == 1 :
        original_price = product_price_data[0].text.replace(",", "")
        current_price =original_price
      else:
        original_price = product_price_data[0].text.replace(",", "")
        current_price =product_price_data[1].text.replace(",", "")
       
      print(f"상품명: {name}, 브랜드: {brand}, 상품번호: {product_number}, 정가: {original_price}, 최저가: {current_price}")
      # lowest_recorded_price =product_data.find("")"5000"
      # last_sale =product_data.find("")"2023-01-02"
    
    categories = []
    return categories

get_products_data("100000100010008")
import requests, re
from bs4 import BeautifulSoup
import categoryNo as category_numbers


def remove_brackets_reg_exp(pdname):
    return re.sub(r"\[.*?\]", "", pdname).strip()


# 각 카테고리별로 상품저장(초기데이터 구축)
def get_products_data(catNo, pageIdx=1):
    url = f"https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo={catNo}&fltDispCatNo=&prdSort=01&pageIdx={pageIdx}&rowsPerPage=48&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&trackingCd=Cat100000100010008_Small"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    if soup.select_one("p.cate_info_tx span").text.strip() == "0":
        print(f'\033[31m{pageIdx}페이지가 없습니다')
        return

    large_ctg = soup.find("a", {"class": "cate_y"}).text
    small_ctg = soup.find_all("h1")[1].text

    all_products_data = soup.find_all("div", {"class": "prd_info"})

    products_collection = []
    date_collection = []

    for product_data in all_products_data:
        try:
            product_info_data = product_data.find("div", {"class": "prd_name"})
            product_price_data = product_data.find(
                "p", {"class": "prd_price"}
            ).find_all(class_="tx_num")

            name = product_info_data.find("p", {"class": "tx_name"}).text
            re_name = remove_brackets_reg_exp(name)
            brand = product_info_data.find("span", {"class": "tx_brand"}).text

            product_number = product_data.find("a").get("data-ref-goodsno")

            original_price = None
            current_price = None

            if len(product_price_data) == 1:
                original_price = product_price_data[0].text.replace(",", "")
                current_price = original_price
            else:
                original_price = product_price_data[0].text.replace(",", "")
                current_price = product_price_data[1].text.replace(",", "")
            products_collection.append(
                {
                    "_id": product_number,
                    "name": re_name,
                    "brand": brand,
                    "price": {
                        "original": original_price,
                        "current": current_price,
                        # 초기버전이기 때문에 업데이트시 수정할 것
                        "lowest": current_price,
                    },
                    "large_ctg": large_ctg,
                    "small_ctg": small_ctg,
                }
            )
        except Exception as e:
            print("데이터를 받아오는 동안 예외가 발생했습니다:", str(e))

    print(f"\033[92m{pageIdx}\033[95m페이지\033[93m{len(products_collection)}\033[95m개 완료")
    return products_collection


# 여기서 pageIdx가 있는지부터 확인
get_products_data("100000100010008")

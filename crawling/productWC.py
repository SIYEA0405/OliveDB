import requests, re
from bs4 import BeautifulSoup
from datetime import datetime


def remove_brackets_reg_exp(pdname):
    return re.sub(r"\[.*?\]", "", pdname).strip()


def get_products_data(catNo, pageIdx):
    url = f"https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo={catNo}&fltDispCatNo=&prdSort=01&pageIdx={pageIdx}&rowsPerPage=48&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&trackingCd=Cat100000100010008_Small"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    if soup.select_one("p.cate_info_tx span").text.strip() == "0":
        print(f"\033[31m{pageIdx}페이지가 없습니다\033[0m")
        return None

    large_ctg = soup.find("a", {"class": "cate_y"}).text
    small_ctg = soup.find_all("h1")[1].text

    all_products_data = soup.find_all("div", {"class": "prd_info"})

    products_data = []
    dates_data = []
    now = datetime.now()

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
            products_data.append(
                {
                    "_id": product_number,
                    "name": re_name,
                    "brand": brand,
                    "price": {
                        "original": int(original_price),
                        "current": int(current_price),
                        "lowest": int(current_price),
                    },
                    "large_ctg": large_ctg,
                    "small_ctg": [small_ctg],
                }
            )

            dates_data.append(
                {
                    "_id": product_number,
                    "dates": [
                        {
                            "date": now.strftime("%Y-%m-%d"),
                            "price": int(current_price),
                        }
                    ],
                }
            )
        except Exception as error:
            print("데이터를 받아오는 동안 예외가 발생했습니다:", str(error))

    print(f"\033[92m{pageIdx}\033[95m페이지\033[93m{len(products_data)}\033[95m개 완료")
    return {
        "products_data": products_data,
        "dates_data": dates_data,
    }


def crawlProducts(category_num):
    page_index = 1
    data_list = {
        "products_data": [],
        "dates_data": [],
    }
    while True:
        result = get_products_data(category_num, page_index)
        if result is None:
            return data_list
        data_list["products_data"].extend(result["products_data"])
        data_list["dates_data"].extend(result["dates_data"])
        page_index += 1

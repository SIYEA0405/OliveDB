import requests
from bs4 import BeautifulSoup

category_number = [
  { "skin_care": ["100000100010008", "100000100010009", "100000100010010"] },

  {
    "masks": [
      "100000100090001",
      "100000100090004",
      "100000100090002",
      "100000100090003"
    ]
  },

  { "cleansing": ["100000100100001", "100000100100002", "100000100100003"] },

  { "suncare": ["100000100110001", "100000100110002"] },

  {
    "dermo_cosmetics": [
      "100000100080013",
      "100000100080006",
      "100000100080005",
      "100000100080011",
      "100000100080004"
    ]
  },

  { "makeup": ["100000100020006", "100000100020001", "100000100020007"] },

  {
    "nail": [
      "100000100120007",
      "100000100120006",
      "100000100120005",
      "100000100120004"
    ]
  },

  {
    "bath_body": [
      "100000100030005",
      "100000100030014",
      "100000100030019",
      "100000100030016",
      "100000100030008",
      "100000100030015",
      "100000100030012",
      "100000100030020",
      "100000100030017",
      "100000100030018"
    ]
  },

  {
    "hair": [
      "100000100040008",
      "100000100040007",
      "100000100040013",
      "100000100040010",
      "100000100040004",
      "100000100040011",
      "100000100040009"
    ]
  },

  {
    "perfume": [
      "100000100050003",
      "100000100050004",
      "100000100050008",
      "100000100050009"
    ]
  },
  {
    "tools": [
      "100000100060001",
      "100000100060006",
      "100000100060007",
      "100000100060002",
      "100000100060003",
      "100000100060004",
      "100000100060005"
    ]
  },

  {
    "man": [
      "100000100070007",
      "100000100070009",
      "100000100070010",
      "100000100070017",
      "100000100070008",
      "100000100070011"
    ]
  }
]

# 각 카테고리별로 상품저장
def get_products_data(catNo):
    pageIdx = 1
    url = f'$https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo={catNo}&fltDispCatNo=&prdSort=01&pageIdx={pageIdx}&rowsPerPage=48&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&trackingCd=Cat100000100010008_Small'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    large_category_list = soup.find('ul', class_='all_menu_wrap')
    large_ctg_names = large_category_list.find_all('h2')
    large_categories = []
    for large_ctg_name in large_ctg_names:
        large_ctg = large_ctg_name.text0
        large_categories.append({'large_ctg': large_ctg})
    return large_categories


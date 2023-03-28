"""
Get csv directly from the "import/export" goodreads page
"""


import requests
# from bs4 import BeautifulSoup
# from lxml import html
import csv
import io




# cookies = {
#     'srb_8': '0_ar',
#     'ccsid': '847-0781147-3836519',
#     'logged_out_browsing_page_count': '2',
#     '__qca': 'P0-773872044-1675298241149',
#     'p': 'CmEVU4Hs1Jw0CNX7H8seJ91q0JMKi-8NAlvScDjXiazhGh_D',
#     'likely_has_account': 'true',
#     'allow_behavioral_targeting': 'true',
#     'session-id': '132-7723043-7117532',
#     'session-id-time': '2307193819l',
#     'lc-main': 'en_US',
#     'ubid-main': '135-0605047-8001544',
#     'u': 'fFd8Hcz_P6GrCEHbVDE5J4fVTGva4E5rWyytmVX22sDJkVtT',
#     'csm-sid': '924-5754924-3973708',
#     'locale': 'en',
#     '_session_id2': 'f8b35bcd3f4e0ca56c6cef3bc08a63ba',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'X-CSRF-Token': '5x4O6MstPcx+o/vRj1qnc3dY2AniBTNAPwvtyiFcuwbDyO/Rgxa6coe9I1VGKX1r5+fim3qdrtqzPlyRHkc8xA==',
#     'Related-Request-Id': '5VBZ1DTDX0AGKHH96GJT',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.goodreads.com/review/import',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     # 'If-None-Match': 'W/"7e88ddfabf5d9da1f08526faafb4ea75"',
# }

# # load cookies, TODO: may not need this
# # requests.get("https://www.goodreads.com/")

# response = requests.head(
#     'https://www.goodreads.com/review_porter/export/61429830/goodreads_export.csv',
#     cookies=cookies,
#     headers=headers,
# )


session = requests.Session()
homepage_response = session.get('https://www.goodreads.com')
# session.get('https://www.goodreads.com/review/import')

cookies = {
    'srb_8': '0_ar',
    'ccsid': '847-0781147-3836519',
    'logged_out_browsing_page_count': '2',
    '__qca': 'P0-773872044-1675298241149',
    'p': 'CmEVU4Hs1Jw0CNX7H8seJ91q0JMKi-8NAlvScDjXiazhGh_D',
    'likely_has_account': 'true',
    'allow_behavioral_targeting': 'true',
    'session-id': '132-7723043-7117532',
    'session-id-time': '2307193819l',
    'lc-main': 'en_US',
    'ubid-main': '135-0605047-8001544',
    'u': 'fFd8Hcz_P6GrCEHbVDE5J4fVTGva4E5rWyytmVX22sDJkVtT',
    'csm-sid': '924-5754924-3973708',
    'locale': 'en',
    '_session_id2': '76990736ec0a28b25a2547dbd1eb54ae',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.goodreads.com/review/import',
    # 'Cookie': 'srb_8=0_ar; ccsid=847-0781147-3836519; logged_out_browsing_page_count=2; __qca=P0-773872044-1675298241149; p=CmEVU4Hs1Jw0CNX7H8seJ91q0JMKi-8NAlvScDjXiazhGh_D; likely_has_account=true; allow_behavioral_targeting=true; session-id=132-7723043-7117532; session-id-time=2307193819l; lc-main=en_US; ubid-main=135-0605047-8001544; u=fFd8Hcz_P6GrCEHbVDE5J4fVTGva4E5rWyytmVX22sDJkVtT; csm-sid=924-5754924-3973708; locale=en; _session_id2=76990736ec0a28b25a2547dbd1eb54ae',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

# session.headers.update(homepage_response.headers)
# session.cookies.update(homepage_response.cookies)
cookies_test = {
    'srb_8': '0_ar',
    'ccsid': '847-0781147-3836519',
    'logged_out_browsing_page_count': '2',
    '__qca': 'P0-773872044-1675298241149', # store and track audience reach
    'p': 'CmEVU4Hs1Jw0CNX7H8seJ91q0JMKi-8NAlvScDjXiazhGh_D',
    'likely_has_account': 'true',
    'allow_behavioral_targeting': 'true',
    'session-id': '132-7723043-7117532',
    'session-id-time': '2307193819l',
    'lc-main': 'en_US',
    'ubid-main': '135-0605047-8001544',
    'u': 'fFd8Hcz_P6GrCEHbVDE5J4fVTGva4E5rWyytmVX22sDJkVtT',
    'csm-sid': '924-5754924-3973708',
    'locale': 'en',
    '_session_id2': '76990736ec0a28b25a2547dbd1eb54ae',
}

response_test = session.get(
    'https://www.goodreads.com/review_porter/export/61429830/goodreads_export.csv',
    headers=headers,
    cookies=homepage_response.cookies
)
response_test.request._cookies.get_dict()


response_curl = session.get(
    'https://www.goodreads.com/review_porter/export/61429830/goodreads_export.csv',
    cookies=cookies,
    headers=headers,
)
response_curl.request._cookies.get_dict()



reader = csv.DictReader(io.StringIO(response.text))

# Previous attempt to scrape from "my list" on goodreads
# -----

# url = "https://www.goodreads.com/review/list/61429830-taniya?ref=nav_mybooks&shelf=read"
# url_export_books = "https://www.goodreads.com/review/import"

# response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")

# htmlparser = etree.HTMLParser()
# tree = etree.parse(response.content, htmlparser)

# html_element = html.fromstring(response.text)
# book_list = "//tr[@class='bookalike review']"
# -----

# cookies = {
#     'srb_8': '0_ar',
#     'ccsid': '847-0781147-3836519',
#     'logged_out_browsing_page_count': '2',
#     '__qca': 'P0-773872044-1675298241149',
#     'p': 'CmEVU4Hs1Jw0CNX7H8seJ91q0JMKi-8NAlvScDjXiazhGh_D',
#     'likely_has_account': 'true',
#     'allow_behavioral_targeting': 'true',
#     'session-id': '132-7723043-7117532',
#     'session-id-time': '2307193819l',
#     'lc-main': 'en_US',
#     'ubid-main': '135-0605047-8001544',
#     'u': 'fFd8Hcz_P6GrCEHbVDE5J4fVTGva4E5rWyytmVX22sDJkVtT',
#     'csm-sid': '924-5754924-3973708',
#     'locale': 'en',
#     '_session_id2': '76990736ec0a28b25a2547dbd1eb54ae',
# }
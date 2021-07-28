from selenium import webdriver

driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")


driver.get("https://web-staging-sbux.starbucks.com.cn/help/legal/2020-double-eleven-r-b-stores/")
driver.maximize_window()

table = driver.find_elements_by_css_selector('section#content>section>table>tbody>tr')
list=[]
for tr in table:
    td = tr.find_elements_by_tag_name('td')
    list.append(td[1].text)

print(list)
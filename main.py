from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

NB_CHAPITRES = 4
driver = webdriver.Chrome()
driver.get("https://bonpatron.com/")
full_text = ""
text_chunk = ""
for i in range(1,NB_CHAPITRES):
    with open("D:\Stage bentley 2019\chapitre{}.tex".format(i), encoding='utf-8') as file:
        text_chunk = ""
        for line in file:
            full_text = full_text + line
text_itr = 0
split = full_text.replace('\\', '').replace('\n', '').replace('section*', ' ').replace('{', ' ').replace('}', ' ').replace('citet', '').replace('citep', '').rsplit('.')
split_index = 0
while(True):
    """ if text_itr+2000-int(len(text_chunk)) >= len(full_text):
        split = full_text[text_itr:].replace('\\', '').replace('\n', '').replace('section*', '').replace('{', ' ').replace('}', ' ').replace('citet', '').replace('citep', '').rsplit('.')
    else:
        split = full_text[text_itr:text_itr+2000-int(len(text_chunk))].replace('\\', '').replace('\n', '').replace('section*', ' ').replace('{', ' ').replace('}', ' ').replace('citet', '').replace('citep', '').rsplit('.')
 """
    text_chunk = ""
    for chunk in split[split_index:]:
        if len(text_chunk + '.' + chunk) >= 2000:
            break
        text_chunk += '.' + chunk
        split_index += 1
    driver.switch_to.frame('typedText_ifr')
    elem = driver.find_element_by_tag_name('p')
    driver.execute_script("arguments[0].textContent = arguments[1];", elem, text_chunk)
    driver.switch_to.default_content()
    correct_text_button = driver.find_element_by_class_name('mainbutton')
    window_before = driver.window_handles[-1]
    correct_text_button.click()

    driver.execute_script("window.open('');")
    window_after = driver.window_handles[-1]
    driver.switch_to_window(window_after)
    driver.get("https://bonpatron.com/")

    
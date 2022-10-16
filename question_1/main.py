from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import urllib.request

browser = webdriver.Chrome(executable_path=r"C:\Users\Batur\Desktop\Reality Defender\question_1\chromedriver.exe")
url = r"https://this-person-does-not-exist.com/en"

browser.get(url)
time.sleep(5)
reload_btn = browser.find_element(By.ID, "reload-button")
time.sleep(15)
reload_btn.click()
for i in range(70):
    reload_btn = browser.find_element(By.ID, "reload-button")
    time.sleep(3)
    reload_btn.click()
    # time.sleep(5)

    img = browser.find_element(By.ID, "avatar")
    src = img.get_attribute("src")

    urllib.request.urlretrieve(src, f"data_collection/image{i}.jpg")

browser.get(r"https://www.istockphoto.com/en/search/2/image?mediatype=photography&phrase=real+headshot&utm_source=pixabay&utm_medium=affiliate&utm_campaign=SRP_photo_sponsored&utm_content=http%3A%2F%2Fpixabay.com%2Fphotos%2Fsearch%2Freal%2520headshot%2F%3Fmanual_search%3D1&utm_term=real+headshot")

images = browser.find_elements(By.CLASS_NAME, "MosaicAsset-module__thumb___klD9E")

for idx, image in enumerate(images):
    src = image.get_attribute("src")
    urllib.request.urlretrieve(src,f"data_collection2/image{idx}.jpg")
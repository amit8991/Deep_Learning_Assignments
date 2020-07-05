
from selenium import webdriver
from save_images import make_directory,save_images,save_data_to_csv
from scrap_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = 'E:\\Softwares\\chromedriver.exe'

driver = webdriver.Chrome(executable_path = DRIVER_PATH)
current_page_url = driver.get('https://www.amazon.in/s?i=apparel&bbn=1968024031&rh=n%3A1571271031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_72%3A1318476031%2Cp_36%3A50000-150000&dc&pf_rd_i=1968093031&pf_rd_p=9663a251-0b2d-5815-92b1-80abd77c0c0b&pf_rd_r=MQ6WNPP00X5F06P7R8QR&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&qid=1593714636&rnid=1968024031&ref=sr_nr_n_1')

DIRNAME = "men_tshirts"
make_directory(DIRNAME)

start_page =1
total_pages = 4

for page in range(start_page,total_pages+1):
    try:
        product_details = scrap_image_url(driver=driver)
        print("Scrapping Page {0} of {1} pages".format(page,total_pages))

        page_value = driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The current page scrapped is {}".format(page_value))

        save_images(data=product_details, dirname=DIRNAME, page=page)
        print("Scraping of page{0} done ".format(page))

        save_data_to_csv(data=product_details, filename='men_tshirts.csv')

        print("Moving to the next page")
        button_type = driver.find_element_by_xpath("//li[@class='a-last']").get_attribute('innerHTML')

        if button_type == 'Next':
            driver.find_element_by_xpath("//li[@class='a-last']").click()
        else:
            driver.find_element_by_xpath("//li[@class='a-normal'][1]").click()

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='a-section aok-relative s-image-tall-aspect']//following::img[@class='s-image']")))
        new_page = driver.find_element_by_tag_name('li').text
        print("The new page is {}".format(new_page))

    except StaleElementReferenceException as Exception:

        print("We are facing an exception")

        exp_page = driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']").text()
        print("The page value at the time of exception is {}".format(exp_page))

        value = driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']")
        link=value.get_attribute('href')
        driver.get(link)

        product_details = scarp_image_url(driver=driver)
        print("Scrapping Page {0} of {1} pages".format(page,total_pages))

        page_value = driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']").text
        print("The current page scrapped is {}".format(page_value))

        save_images(data=product_details,dirname=DIRNAME,page=page)
        print("Scraping of page{0} done ".format(page))

        save_data_to_csv(data=product_details,filename='men_ethnic.csv')

        print("Moving to the next page")
        button_type = driver.find_element_by_xpath("//div[@class='_2zg3yZ']//a[@class='_3fVaIS']//span").get_attribute('innerHTML')

        if button_type == 'Next':
            driver.find_element_by_xpath("//a[@class='_3fVaIS']").click()
        else:
            driver.find_element_by_xpath("//a[@class='_3fVaIS'][2]").click()

        new_page = driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']").text
        print("The new page is {}".format(new_page))
















        

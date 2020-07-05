#scrapping images urls using selenium

def scrap_image_url(driver):
    images=driver.find_elements_by_xpath("//div[@class='a-section aok-relative s-image-tall-aspect']//following::img[@class='s-image']")
    brands=driver.find_elements_by_xpath("//h5[@class='s-line-clamp-1']")

    print(len(images),len(brands))
    
    product_data={}
    product_data['image_urls']=[]
    product_data['brands']=[]

    for image in images:
        source = image.get_attribute('src')
        product_data['image_urls'].append(source)

    for brand in brands:
        product_data['brands'].append(brand.text)


    print("Returning scrapped data")

    return product_data
        

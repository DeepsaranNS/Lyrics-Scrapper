from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, executable_path=r"C:\\Users\\deeps\\Downloads\\chromedriver_win32\\chromedriver.exe")
search="https://www.musixmatch.com/search/{q}"
query=input("Provide the song Name: ")

try:
    driver.get(search.format(q=query))
    driver.find_element_by_class_name("track-card").click() 
    ans1=driver.find_element_by_xpath('//*[@id="site"]/div/div/div/main/div/div/div[3]/div[1]/div/div/div/div[2]/div[1]/span/p/span').text
    ans2=driver.find_element_by_xpath('//*[@id="site"]/div/div/div/main/div/div/div[3]/div[1]/div/div/div/div[2]/div[1]/span/div/p/span').text
    print("\n\n")
    print(ans1+ans2)
except:
    print("The lyrics is not found for this song!! \n Please provide other song :)")
finally:
    driver.close()
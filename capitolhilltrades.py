#A serverless script that scrapes data from https://app.capitoltrades.com/trades
#DISCLAIMER: The use of this script may be against the iQ2 Terms of Service. 
#As such, by using this script you accept that there is a risk of service outage or legal repercussions
#The author of this script assumes no liability for such risk, and this software is provided 'as-is' 

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#Requirements beyond imports: Selenium + compatible Chrome (or preferred) webdriver

#Initiate a headless Selenium instance
options = Options()
options.headless = True

#n=473 is the current amount of pages in the capitolhill trades website, dating back to 27 Jan 2019
olddata=pd.DataFrame()
i=1

#modify the following to reflect the appropriate paths 
webdriver_path=''
csv_output_path=''

#MAINLOOP
#n=473 is the current amount of pages in the capitolhill trades website, dating back to 27 Jan 2019
for n in range(473):
    urlstr="https://app.capitoltrades.com/trades?page="+str(i)+"&pageSize=100"
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
    driver.get(urlstr)
    time.sleep(2) # Optional sleep to reduce risk of off-targets; can reduce with fast internet/disk space
    html_source = driver.page_source
    driver.close() #This website (or selenium) seems to interrupt multiple queries by a given selenium driver, so the driver must be reinstantiated (don't quote me on this)
    newdata = pd.read_html(html_source)[0]
    olddata=pd.concat([olddata,newdata])
    olddata.to_csv(path_or_buf=csv_output_path) 
    time.sleep(2) # Optional sleep to reduce risk of off-targets; can reduce with fast internet/disk space
    print(olddata)
    i=i+1

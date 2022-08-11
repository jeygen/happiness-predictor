from webbrowser import get
from bs4 import BeautifulSoup
import requests
import time

def get_hl():
    nyt_html_text = requests.get('https://www.nytimes.com/').text
    soup = BeautifulSoup(nyt_html_text, 'lxml')
    
    hl_string = ''
    try:
        for headline in soup.find_all('div',  class_ = 'css-xdandi'):
            hl_string = hl_string + headline.text + ' '
    except Exception as e:
        print("Unable to scrape NYT.")

    return hl_string

def get_poem():
    poem_html_text = requests.get('https://www.youngwriterssociety.com/poem_random.php').text
    soup_p = BeautifulSoup(poem_html_text, 'lxml')

    p_string = ''
    try:
        for poem in soup_p.find_all(id = 'random'):
            p_string = p_string + poem.text + ' '
            print(poem.text)
            return poem.text
    except Exception as e:
        print("Unable to scrape random poem.")

    return p_string
          
print(get_hl())
print(get_poem())

'''
    # for job in jobs:
    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','') # cleanup white space
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        with open(f'posts/{index}.txt', 'w') as f: # b/c fancy enum loop name files 1,2,3..
            # because span in span
            f.write(f"Company Name: {company_name.strip()} \n") #strip for whitespace
            f.write(f"Required Skills: {skills.strip()}\n") 
            f.write(f"Required Skills: {more_info.strip()}\n") 
        print("File saved")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 360
        print(f"Waiting {time_wait / 60} minutes...")
        time.sleep(time_wait)
'''
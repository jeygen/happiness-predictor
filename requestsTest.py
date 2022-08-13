import requests

# unfinished

def rtest(r):
    try:
        poem_html_text = requests.get('https://www.youngwriterssociety.com/poem_random.php', timeout=3)
        poem_html_text.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Oops: Something Else",err)
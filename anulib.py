# ANU Library room booker network module
# Paul Apelt u5568225
import requests
from lxml import html
def login(login):
    # anulib url
    url = 'https://anulib.anu.edu.au/'\
            'using-the-library/book-a-library-group-study-room/index.html'
    # convert login to POST dict
    login = {'inp_uid':login[0],'inp_passwd':login[1]}
    r = requests.post(url,data = login)
    # check for errors
    return not html.fromstring(r.text).xpath("//div[@class='msg-error']")



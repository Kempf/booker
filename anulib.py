# ANU Library room booker network module
# Paul Apelt u5568225
import requests
from lxml import html
def success(r):
    """Checks for errors and status code"""
    return not html.fromstring(r.text).xpath("//div[@class='msg-error']")\
            and r.status_code == requests.codes.ok
def login(login):
    """POST logn data to anulib and check for errors"""
    url = 'https://anulib.anu.edu.au/'\
            'using-the-library/book-a-library-group-study-room/index.html'
    login = {'inp_uid':login[0],'inp_passwd':login[1]}
    r = requests.post(url,data = login)
    return success(r)
def logout():
    """POST logout and confirm"""
    
    return success(r)
def init(date,lib):
    """Select date and library for the booking and check for errors"""
    
    return success(r)
def book(time,room)
    """Book the room at the specified time"""

    return success(r)

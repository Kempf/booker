# ANU Library room booker network module
# Paul Apelt u5568225
import requests
from lxml import html
class anulib:
    def __init__(self):
        self.url = 'https://anulib.anu.edu.au/'\
                'using-the-library/book-a-library-group-study-room/index.html'
    def success(self,r):
        """Checks for errors and status code"""
        return not html.fromstring(r.text).xpath("//div[@class='msg-error']")\
                and r.status_code == requests.codes.ok
    def login(self,login):
        """POST logn data to anulib and check for errors"""
        login = {'inp_uid':login[0],'inp_passwd':login[1]}
        r = requests.post(self.url,data = login)
        return self.success(r)
    def logout(self):
        """POST logout and confirm"""
        r = requests.post(self.url,data = 'logout')
        return self.success(r)
    def init(self,date,lib):
        """Select date and library for the booking and check for errors"""
        
        return self.success(r)
    def book(self,time,room):
        """Book the room at the specified time"""

        return self.success(r)

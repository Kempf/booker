# ANU Library room booker config module
# Paul Apelt u55628225
import datetime
import os.path
class parser:
    def __init__(self):
        self.log = self.initlog()
    def checkline(self,line):
        """Checks if the config line is not a comment"""
        if line[0] != '#' and line.strip():
            return True
        else:
            return False
    def initlog(self):
        """Initiates log"""
        log = open('log','a')
        log.write("{}: {} log.\n"\
                .format(datetime.datetime.now(),__name__))
        return log
    def fileopen(self,filename,mode):
        """Utility file open with exception catching"""
        try:
            f = open(filename,mode)
            print("Opened {} as {}\n".format(filename,mode),file = self.log)
        except FileNotFoundError:
            print("File '{}' not found!\n".format(filename),file = self.log)
            exit()
        return f
    def timetable(self,filename):
        """Parse timetable config and return it as a list"""
        timelist = []
        f = self.fileopen(filename,'r')
        for line in f:
            if self.checkline(line):
                linelist = line.strip().split(',')
                breaklist = []
                for item in linelist[1:]:
                    hourlist = item.split(':')
                    for i, hour in enumerate(hourlist):
                        try:
                            hourlist[i] = int(hour)
                        except ValueError:
                            print("Bad config format at line '{}'!\n"\
                                    .format(line.strip()),file = self.log)
                            exit()
                    breaklist.append(hourlist)
                timelist.append(breaklist)                    
        return timelist
    def bookings(self,filename):
        """Parses the bookings list and returns it as a list"""
        booklist = []
        if os.path.isfile(filename):
            f = self.fileopen(filename,'r')
            for line in f:
                if self.checkline(line):
                    linelist = line.split(',')
                    hourlist = linelist[-1].split(':')
                    try:
                        linelist[-1] = [int(hourlist[0]),int(hourlist[1])]
                    except ValueError:
                            print("Bad config format at line '{}'!\n"\
                                    .format(line.strip()),file = self.log)
                            exit()
                    booklist.append(linelist)
        return booklist
    def logins(self,filename):
        """Parses login file"""
        loginlist = []
        f = self.fileopen(filename,'r')
        for line in f:
            if self.checkline(line):
                loginlist.append(line.strip().split())
        return loginlist

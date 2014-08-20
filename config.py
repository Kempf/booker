# ANU Library room booker config module
# Paul Apelt u55628225
import datetime
import os.path
def checkline(line):
    """Checks if the config line is not a comment"""
    if line[0] != '#' and line.strip():
        return True
    else:
        return False
def initlog():
    """Initiates log"""
    log = open('log','a')
    log.write("{}: {} log.\n"\
            .format(datetime.date.today().isoformat(),__name__))
    return log
def fileopen(filename,mode):
    """Utility file open with exception catching"""
    try:
        f = open(filename,mode)
        print("Opened {} as {}\n".format(filename,mode),file = log)
    except FileNotFoundError:
        print("File '{}' not found!\n".format(filename),file = log)
        exit()
    return f
def timetable(filename):
    """Parse timetable config and return it as a list"""
    timelist = []
    f = fileopen(filename,'r')
    for line in f:
        if checkline(line):
            linelist = line.strip().split(',')
            breaklist = []
            for item in linelist[1:]:
                hourlist = item.split(':')
                for i, hour in enumerate(hourlist):
                    try:
                        hourlist[i] = int(hour)
                    except ValueError:
                        print("Bad config format at line '{}'!\n"\
                                .format(line.strip()),file = log)
                        exit()
                breaklist.append(hourlist)
            timelist.append(breaklist)                    
    return timelist
def bookings(filename):
    """Parses the bookings list and returns it as a list"""
    booklist = []
    if os.path.isfile(filename):
        f = fileopen(filename,'r')
        for line in f:
            if checkline(line):
                linelist = line.split(',')
                hourlist = linelist[-1].split(':')
                try:
                    linelist[-1] = [int(hourlist[0]),int(hourlist[1])]
                except ValueError:
                        print("Bad config format at line '{}'!\n"\
                                .format(line.strip()),file = log)
                        exit()
                booklist.append(linelist)
    return booklist
log = initlog()



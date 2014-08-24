# ANU Library room booker
# Paul Apelt, u5568225
import config
import network
parser = config.parser()
anulib = network.anulib()
print(parser.timetable('timetable.conf'))
login = parser.logins('login.conf')[0]
print(anulib.login(login))
print(anulib.logout())

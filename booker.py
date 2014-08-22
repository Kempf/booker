# ANU Library room booker
# Paul Apelt, u5568225
import config
import network
parser = config.parser()
anulib = network.anulib()
print(parser.timetable('timetable.conf'))
print(anulib.login(('u5568225','P13apauoe!')))


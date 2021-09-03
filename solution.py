import sys

#put flight info together into JSON script
def print_flight(flight):
    ret = '       "flights": [\n            {\n'
    i = 0
    for x in flight:
        if i != 7:
            ret += '                "{}": "{}",\n'.format(column_names[i], x)
        else:
            ret += '                "{}": "{}"\n'.format(column_names[i], x)
        i += 1
    ret += '            }\n'
    ret += '        ]\n'
    return ret


#read all arguments and put them into variables
if len(sys.argv)<2 or len(sys.argv)>6:
    sys.exit("wrong input (number of arguments)")
csv_file = sys.argv[1]
origin = sys.argv[2]
destination = sys.argv[3]
bags_needed = 0
flight_return = False
if len(sys.argv) > 4:
    bags_needed = int(list(sys.argv[4])[-1])
if len(sys.argv) > 5:
    flight_return = True


#read file and put its contents into list
list_of_flights = []
f= open(csv_file, "r")
i = 0
for x in f:
    if i != 0:
        x = x[:-1]
        list_of_flights.append(x.split(","))
    else:
        x = x[:-1]
        column_names = x.split(",")
    i+=1
f.close()

#check for presence of airport
origin_present = False
destination_present = False
for flight in list_of_flights:
    if destination == flight[2]:
        destination_present = True
    if origin == flight[1]:
        origin_present = True

if not origin_present or not destination_present:
    sys.exit("no suitable flights (missing airport)")

exit_file = open("returnfile.json", "w")
exit_file.write("[\n")
exit_file.write("    {\n")
#for flight in list_of_flights:
    #if flight[1] == origin and flight[2] == destination:
exit_file.write(print_flight(flight))
exit_file.write("    }\n")
exit_file.write("]\n")

#TODO dokoncit spracovanie JSON aspon pre priamy let
#TODO skusit nieco pre vyhladavanie viacerych spojeni
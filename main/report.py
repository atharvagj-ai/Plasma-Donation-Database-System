def get_event_date(event):
    return event.date
def current_users(events):
    events.sort(key = get_event_date)
    machines = {}
    for event in events:
        if (event.machine not in machines):
            machines[event.machine] = set()
        if (event.type == "login"):
            machines[event.machine].add(event.user)
        elif (event.type == "logout"):
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


class Event:
    def __init__( self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

"""        
    def print_values(self):
        print(self.date)
        print(self.type)
        print(self.machine)
        print(self.user)



def intake_event_details() :
    event_date = input("Enter date and time in format: YYYY-MM-DD HH:MM:SS\n")
    event_type = input("Enter event type: login/logout\n")
    machine_name = input("Enter machine name\n")
    user = input("Enter user's name\n")
    e = Event(event_date,event_type,machine_name,user)
    e.print_values()

intake_event_details()


# a =[] 
# Create a new Event object
# e[i] = Event(a, event_date[i],event_type[i],machine_name[i],user[i])

# n = int(input("How many events do you want to add"))
# for i in range (n):
#     e[i].intake_event_details()
#     i += 1

def intake_event_details():
    event_date = input("Enter date and time in format: YYYY-MM-DD HH:MM:SS\n")
    event_type = input("Enter event type: login/logout\n")
    machine_name = input("Enter machine name\n")
    user = input("Enter user's name\n")
"""
#events = []

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'Lase'),
    Event('2020-01-22 10:25:36', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)
generate_report(users)


from datetime import datetime

def add_datetimes_to_list(datetimes_when_occupied):
    '''Adds the date and time when the room is occupied to a
        dictionary, which is added to a list containing each dictionary.'''
    now = datetime.now()
    print(now)
    d = {}
    d['time'] = now.time()
    d['day'] = now.strftime("%A")
    d['date'] = now.strftime("%d")
    d['month'] = now.strftime("%B")
    datetimes_when_occupied.append(d)

def print_list(datetimes_when_occupied):
    '''Print the contents of each dictionary from the list.'''
    for datetimes in datetimes_when_occupied:
        print(datetimes['time'])
        print(datetimes['day'])
        print(datetimes['date'])
        print(datetimes['month'])

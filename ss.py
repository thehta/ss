import requests
import json
import mappings
import time
import sys

API_URL = "https://mhlengispeaks.com/wp-admin/admin-ajax.php"

INIT_PARAMS = {
    "location": "",
    "service": "2",
    "worker": "17",
    "date": "",
    "end_date": "",
    "start": "",
    "action": "ea_res_appointment"
}

CONFIRMATION_PARAMS = {
    "id": "",
    "bame": "",
    "student-number": "",
    "email": "",
    "phone": "0",
    "description": "",
    "action": "ea_final_appointment"
}


def find_seat(seat):
    for k in mappings.seat_mappings:
        if (mappings.seat_mappings[k] == seat):
            return k

def book(time, date, seat, SU_id, name):
    location = find_seat(seat)
    populated_init_params = {
        "location": location,
        "date": date,
        "end_date": date,
        "start": f"{time[0:2]}:00"}
    INIT_PARAMS.update(populated_init_params)

    r_init = requests.get(url=API_URL, params=INIT_PARAMS)
    book_json = json.loads(r_init.text)
    print(book_json)
    book_id = int(book_json['id'])

    populated_confirmation_params = {
        "id": book_id,
        "bame": name,
        "student-number": SU_id,
        "email": f"{SU_id}@sun.ac.za",
    }
    CONFIRMATION_PARAMS.update(populated_confirmation_params)
    r_confirm = requests.get(url=API_URL, params=CONFIRMATION_PARAMS)
    print(r_confirm.text)


def getTimes(date, time):
    seat_output = []
    i = 0
    for location in range(30, 231):
        URL = "https://mhlengispeaks.com/wp-admin/admin-ajax.php?worker=17&service=2&location={0}&action=ea_date_selected&date={1}".format(
            location, date)

        response = requests.get(URL)
        out = json.loads(response.text)
        b = ""
        sys.stdout.write('\033[2K\033[1G')
        if (i < 4):
            b = "Fetching reservations" + "." * i
            print(b, end="\0", flush=True)
            i += 1
        else:
            i = 0
        for hour in out:
            if ((hour['count'] == 1) and (hour['value'] == time)):
                seat_output.append(mappings.seat_mappings[str(location)])
    seat_output.sort()
    print(time, seat_output)


if __name__ == "__main__":
    try:
        if (sys.argv[1] == 'get'):
            date = sys.argv[2]
            time = sys.argv[3]
            getTimes(date, time)
        elif (sys.argv[1] == 'book'):
            date = sys.argv[2]
            time = sys.argv[3]
            seat = sys.argv[4]
            id = '20700601'
            name = 'Thomas'
            if (sys.argv[5] and sys.argv[6]):
                id = sys.argv[4]
                name = sys.argv[5]
            book(time, date, seat, id, name)
        else:
            raise ValueError('')

    except:
        print(f"Usage:\n\
            {sys.argv[0]} get 'YYYY-MM-DD' 'HH:00'\n\
            {sys.argv[0]} book 'YYYY-MM-DD' 'HH:00' 'D1-<seat_no>' 'SU_id' 'name'\n\
            \nExamples:\
            \nGet all available seats for 9 am on October 30th:\n\
            {sys.argv[0]} get '2021-10-30' '09:00'\n\
            \nBook seat D53 at 9 am on October 30th for Thomas:\n\
            {sys.argv[0]} book '2021-10-30' '09:00' 'D1-53' '20700601' 'Thomas'\n")
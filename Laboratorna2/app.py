import requests
import ntplib
from datetime import datetime
import time

def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date


def check_time(d):
    if "time" in d.keys():
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError


def main(url=''):
    if not url:
        print("No URL passed to function")
        return False

    try:
        r = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        raise ConnectionError

    if r:
        check_time(r.json())
    else:
        check_time(get_time_if_url_not_work())
    return True


def home_work(url=''):
    if url=='' or url:
        my_time = time.strftime('%H', time.localtime())
        if int(my_time) >= 12:
            h = "ДоБрОї НоЧі"
        elif int(my_time) < 12:
            h = "ДоБрОгО ДнЯ"
    else:
        r = requests.get(url=url)
        for l in r.json()['time']:
            if l =='P':
                h = "ДоБрОї НоЧі"
                break
            else:
                h = "ДоБрОгО ДнЯ"
    print(h)
    return h



if __name__ == "__main__":
    a = "="*40
    print(a + "\nРезультат без параметрів: ")
    main()
    print(a + "\nРезультат з правильною URL: ")
    main('http://date.jsontest.com/')
    print(a + "\nРезультат з правильною URL: ")
    home_work('http://date.jsontest.com/')
    print(a + "\nРезультат без параметрів: ")
    home_work()

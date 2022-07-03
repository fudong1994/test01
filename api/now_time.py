import datetime


def get_time():
    now = datetime.datetime.now()
    return now.strftime('%y%m%d')#%H%M%S


def get_time2():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')


if __name__ == '__main__':
    time = get_time()
    time2 = get_time2()
    print(time, time2)


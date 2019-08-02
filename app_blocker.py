import time
from datetime import datetime as dt

# for testing purposes
# hosts_temp = 'hosts'

# hosts file(unix e.g mac)
hosts_path = '/etc/hosts'
redirect_host = '127.0.0.1'
websites = ['www.facebook.com', 'facebook.com', 'pornhub.com', 'www.pornhub.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('working hours...')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write('%s %s \n' % (redirect_host, website))
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
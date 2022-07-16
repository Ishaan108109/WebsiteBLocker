# Administrator permission is required to run the program
# if u want to unblock then comment the code from line 11 to 19

import datetime
import time
end_time=datetime.datetime(2022,7,18)
site_block= ['docs.python.org','www.facebook.com']
host_path="C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1 "

while True:
    if datetime.datetime.now()<end_time:
        print('Start Blocking')
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect + " "+website+"\n")
    else:
        with open(host_path, "r+") as host_file:
            content = host_file.readline()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()
        time.sleep(5)
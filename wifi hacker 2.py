import csv
import datetime 
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
specific_time = datetime.datetime.now().strftime("%H-%M-%S") 
import subprocess
import re
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
wifi_list = []
if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {} 
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:           
            wifi_profile["ssid"] = name        
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)           
            if password == None:
                wifi_profile["password"] = None
            else:   
                wifi_profile["password"] = password[1]   
            wifi_list.append(wifi_profile) 
for x in wifi_list:
    print(x)

File=open(f'passwords\\{current_date}-{specific_time}.csv','w',newline='')
fw=csv.writer(File)
for x in wifi_list:
    print(x)
    fw.writerow([x['ssid'],x['password']])
print('file made')
File.close()

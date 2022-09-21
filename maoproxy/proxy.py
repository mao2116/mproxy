#usr/bin/pyton3
try:
    import os
except Exception as mao:
    print(f"[ ! ] {mao}")
try:
    import datetime
    from requests import get
except  Exception as mao:
    print(f"[ ERROR ] {mao}")
    inp=(input("Install Requirement Auto (Y/n) : ")).lower()
    if inp=="n":
        print("[ ! ] Cancel !!!")
    elif inp == "y":
        os.system("pip3 install requests")
        from requests import get
    else:
         print("[ ! ] Aborted !!!")   
def mproxy(type=None):
    try:    
        true=True
        false = False
        return_ip=""
        if str(type).lower() =="none":
            print("Must Set Requests Security Type !!!")
        elif str(type).lower() =="http":
            responses=(get(f"https://checkerproxy.net/api/archive/{datetime.date.today()}")).text
            for ips in eval(responses):
                if str(ips["type"]) == "1":
                    return_ip=return_ip+ips["addr"]+","      
                else:
                    pass
            return return_ip.split(",")
        elif str(type).lower() =="https":
            responses=(get(f"https://checkerproxy.net/api/archive/{datetime.date.today()}")).text
            for ips in eval(responses):
                if str(ips["type"]) == "2":
                    return_ip=return_ip+ips["addr"]+","      
                else:
                    pass
            return return_ip.split(",")       
        elif str(type).lower() =="socks5":
            responses=(get(f"https://checkerproxy.net/api/archive/{datetime.date.today()}")).text
            for ips in eval(responses):
                if str(ips["type"]) == "4":
                    return_ip=return_ip+ips["addr"]+","      
                else:
                    pass
            return return_ip.split(",")
        elif str(type).lower() =="all":
            responses=(get(f"https://checkerproxy.net/api/archive/{datetime.date.today()}")).text
            for ips in eval(responses):
                    return_ip=return_ip+ips["addr"]+","
            return return_ip.split(",")
        else:
            print("[ ! ] Type Not supported !!\n Code Aborted !")    
    except Exception as mao:
        print(f"[ ! ] {mao}")
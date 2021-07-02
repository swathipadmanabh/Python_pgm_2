# creating 10 different files for 10 different users

userlist = ["Shristi","Akanksha","Surabhi","Shishir","Sampath","Abhimanyu","Niveditha","Sharan"]
password = "SSSS123"
string1 = "Username is %s\n"
string2 = "Password is %s"


for name in userlist:
        with open("%sfile1.txt" %name, "w+") as file1:
            file1.write(string1 %name)
            file1.write(string2 %password)
file1.close()

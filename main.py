
file=input("enter the file name : ")
with open(file,"r") as f:
     for line in f:
        if "INFO" in line:
            print(line.strip())
        else:
                 continue


with open("test.txt","w") as f:
    f.write("""INFO 2024-07-12 10:00:00 Service started
INFO 2024-07-12 10:15:00 User logged in
INFO 2024-07-12 10:30:00 Service stopped""")
    f.close()
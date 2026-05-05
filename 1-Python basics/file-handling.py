# files - read, write, append 

# 1st method - file 

# f=open('abhinav.txt','r')  # r- read
# print(f.read())
# f.close()  # close the file after use

# f= open('abhinav.txt','w')  # w- write
# i="Arshdeep Jatin "
# f.write(i)

# f.close()

# f= open('abhinav.txt','r')  # r- read
# print(f.read())
# f.close()

# f= open('file.txt','a')  # a- append
# i=" Anshu Mehak Mansi"
# f.write(i)
# f.close()

# f=open('file.txt','r')
# print(f.read())
# f.close()

# 2nd method -

# with open('abhinav.txt','r') as f:
#     print(f.read())


# with open('abhinav.txt','r+') as f:  #\ r+ - read and write
#     print(f.read())
#     f.seek(15)
#     f.write("\n My name is Abhinav Sharma \n I am from Chandigarh")
    


# with open('abhinav.txt','w+') as f: # w+ - write and read
#     f.write("Jatin Dhuper")
#     f.seek(0)
#     print(f.read())
#     f.close()


# with open("new.txt",'x') as e: # x - create a new file and write in it
#     print(e.write("hello"))


with open("new.py",'x') as e:
    print(e.write("print(\"Hello World\")"))

# Json files read
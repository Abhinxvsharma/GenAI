# os - operating system 

import os
# check directory 
print(os.getcwd())  # getcwd - get current working directory 

os.chdir('D:\\CODER ROOTS')
print("After change",os.getcwd())  # getcwd - get current working directory 



os.makedirs('jatin') # make directories


os.chdir('jatin')
for i in range(0,100):
    os.makedirs(f'anshu{i}')

for i in range(0,100):
    os.removedirs(f'jatin{i}')

os.remove()  # remove 
import re 

# exp="[6-9]{1}\d{9}"

# st="mobile number is 8264123555 and other number is 9585837845 and one more is 4568 and 7638726 JATIN 324234 and 2589637410"

# print(re.search(pattern=exp,string=st)) # search - only one return 
# print(re.findall(pattern=exp,string=st))

mail_exp="[a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z]{2,7}"
hotexp="[a-zA-Z0-9._]+@[hotmail|gmail]+.[a-zA-Z]{2,7}"
only_gmail="[a-zA-Z0-9._]+@gmail.[a-zA-Z]{2,7}"

st1="mail id is gurminder@coderroots.com and jatin@gmail.com and coderroots001@gmail.com and arsh id is arsh.singh0@gmail.com AND mail is a@hdsbf.com and arsh12@hotmail.com "
# print(re.findall(mail_exp, st1))

# print(re.findall(hotexp, st1))

# print(re.findall(only_gmail, st1))

st1=re.sub(mail_exp,repl="",string=st1)  # replace

print(st1)
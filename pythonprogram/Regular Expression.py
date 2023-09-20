#Meta charecter : .,/,^,$,{},[],(),|,*,?,+
#spacel character:w,W,s,S,b,B,d,D
#methods:match,search,findall,split,sub,subn
import re
#match:
"""st="Now i am doing python course,my name is Alexander 67"
m1=re.match(".",st)
print(m1)
m2=re.match("^N",st)
print(m2)
m3 =re.match("[a-z A-Z]",st)
print(m3)"""


#phone
plist="+91987654374743" "+916381549406" "7868029219" "g288929289l"
res=re.findall("\+91[6-9]{1}[0-9]{9}",plist)
print(res)

#--------------------------------------------------------------------------------

#URL
#for single url
import re
pattern =r'^(http|https)://www[.][a-z 0-9]+[.]com$'
str=input("Enter the URL : ")
out=re.match(pattern,str)
print(out)
print(out.group())
"""
#for string of url

--------------------------------------------------------------------------------
# Email Id
#for single mail id
import re
pattern='^[a-z 0-9]+[@]\w+[.]\w{2,3}'
str=input("Enter the email Id:")
print("the mail valid") if re.match(pattern,str) else print("the mail is invalid")"""

#for string of mail id

"""import re
pattern=r'\w+@\w+[.]\w{2,3}'
coll='alexander938@gmail.com,adc@adc.com,asd@asd.com,mervin007@gmail.com vimal@@gmil.in,kdjsakdfk.dksfjkk,dklfja@dkfa..deu'
out=re.findall(pattern,coll)
print(out)
print(type(out))"""
    
    





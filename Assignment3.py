dicti={}
def most_frequent(s):
    for i in s:
        if i not in dicti:
            dicti[i]=1
        else:
            dicti[i]+=1
    return dicti

stri=input("Enter a string: ")
res=most_frequent(stri)
for keys in sorted(res,key = res.get,reverse=True):
  print(keys,"=",res[keys])

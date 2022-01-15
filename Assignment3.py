dicti={}
def most_frequent(s):
    for i in s:
        if i not in dicti:
            dicti[i]=1
        else:
            dicti[i]+=1
    return dicti

res=most_frequent('Mississippi')
print(sorted(res.keys()))
print(sorted(res.values()))


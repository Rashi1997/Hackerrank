# Complete the solve function below.
def solve(s):
    s1=""
    c=0
    for i in range(0,len(s)):
        if(i==0 or s[i]==" " or c==1):  
            if(i==0):
                s1+="".join(s[i].upper())
            elif(s[i]==" "):
                s1+="".join(s[i])
                c=1
            elif(c==1):
                s1+="".join(s[i].upper())
                c=0
        else:
            s1+="".join(s[i])
    return s1

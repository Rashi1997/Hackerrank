# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d=dict()
for i in range(0,n):
    inp=list(input().split(" "))
    d.update({inp[0]:inp[1]})
#print(d)
try:
    while True:
        query = input()
        try:
                print(query + "=" + d[query])
        except:
            print("Not found")
except EOFError:
    pass

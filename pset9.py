#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

x = input("Enter message:")

print(x.upper())

l = x.split()
char = ''

for i in range(len(l)):
    char += l[i][0:1]

print(char)
    




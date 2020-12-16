#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

x = input("Message:")
char = ''

for i in x:
    offset = ord(i) + 13
    if (offset > 90):
        offset -= 26
        
    char += chr(offset)

print(char)
    

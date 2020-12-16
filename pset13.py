#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

x = input("Enter list of names here:")

listnames= x.split("; ")
counter = 0

for i in listnames:
    note = i.split(", ")
    listnames[counter] = note[1][0] + ". " + note[0]
    counter += 1


for i, j in enumerate(listnames):
    print(j)

    


            
    
    





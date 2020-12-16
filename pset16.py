#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

x = int(input("Enter time in seconds:"))

hours = x // 3600
minutes = (x - (hours * 3600)) // 60
seconds = (x - (hours * 3600) - (minutes * 60))

print(str(hours) + "h: " + str(minutes) + "m: " + str(seconds) + "s")

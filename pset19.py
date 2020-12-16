#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

x = int(input("Enter # of cents:"))

remaining = 0

Quarters = x // 25
remaining = x % 25

Dimes = remaining // 10
remaining = remaining % 10

Nickel = (remaining // 5)
remaining = remaining % 5


print("Quarters:" + str(Quarters))
print("Dimes:" + str(Dimes))
print("Nickels:" + str(Nickel))
print("Cents" + str(remaining))

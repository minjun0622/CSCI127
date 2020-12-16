#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

def backup(n):
    return(n * 1.0875)

def main():
    price = float(input("Enter the price of item:"))
    counter = 0
    while price > 0:
        counter += backup(price)
        price = float(input("Enter price of item:"))

    print("Total is ", counter)

if __name__ == "__main__":
    main()

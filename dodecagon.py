import math


def main():
    # Get area length from user
    side  = float(input("Enter the side length(mm): "))

    # calculate area and perimeter
    
    area = 3 * ( 2 + math.sqrt(3) ) * math.pow(side,2) 
    perimeter = 12 * side

    # shows area and perimeter
    print("Area = {} mm^2".format(area))
    print("Perimeter = {} mm".format(perimeter))

if __name__ =="__main__":
    main()
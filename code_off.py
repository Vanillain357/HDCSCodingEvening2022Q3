from math import factorial

def main():
    test()


def pascal(n):

    # checking that n is an int
    try:
        n = int(n)
    except ValueError:
        print("Please enter a number")
        return

    # create a list with the right number of entries
    row = [1] * n 
    # for every row
    for x in range(n):
        # for every position in the row
        for y in range(x+1):
            # use x and y to calculate the row using n! = x!/(x-y)!*y!
            row[y] = (factorial(x)/(factorial(x-y)*(factorial(y))))
    # return the sum of the list
    return (round(sum(row)))


# unit tests
def test():
    try:
        assert pascal(5) == 16
        print("✔️ 5 returns 16")
    except AssertionError:
        print("❌ 5 does not return 16")

    try:
        assert pascal(8) == 128
        print("✔️ 8 returns 128")
    except AssertionError:
        print("❌ 8 does not return 128")

    try:
        assert pascal(30) == 536870912
        print("✔️ 30 returns 536870912")
    except AssertionError:
        print("❌ 30 does not return 536870912")


main()
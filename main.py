def main():
    # taking input from the user
    credit  =  input("number: ")
    # regecting non-mumaric chars
    if credit.isdigit() == False:
        main()
    s = 0
    size = len(credit)
    # begin checksum
    for i in range(size - 1, -1, -2):
        s += int(credit[i])
    for i in range (size - 2, -1, -2):
        temp = 0
        temp += int(credit[i])  * 2
        if temp > 9:
            temp -= 9
        s += temp
    # combine fistr two digits
    temp = (10 * int(credit[0]) + int(credit[1]))
    if size >= 13:
        if s % 10 == 0:
            if credit[0] == "4":
                print("VISA")
            elif temp == 34 or temp == 37:
                print("AMEX")
            elif temp == 51 or temp == 52 or temp == 53 or temp == 54 or temp == 55:
                print("MASTERCARD")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")


main()
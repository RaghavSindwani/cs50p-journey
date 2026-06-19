def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_found = False

    for c in s:

        if not c.isalnum():
            return False

        if c.isdigit():

            if not number_found and c == "0":
                return False

            number_found = True

        if number_found and c.isalpha():
            return False

    return True


main()

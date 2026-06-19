months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")


        else:
            month, rest = date.split(" ", 1)
            day, year = rest.split(", ")
            day = int(day)
            month = months.index(month) + 1
            print(f"{year}-{month:02}-{day:02}")

            break
    except ValueError:
            pass

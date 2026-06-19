import random

def get_level():
    while True:
        try:
           level = int(input("Level: "))
           if level == 1 or level == 2 or level == 3:
            return level
        except ValueError:
            pass

level = get_level()

def generate_integer(level):

       if level == 1:
          return(random.randint(0, 9))
       if level == 2:
          return(random.randint(10, 99))
       if level == 3:
          return(random.randint(100, 999))

x = generate_integer(level)
y = generate_integer(level)

answer = int(x) + int(y)

print(f"{x} + {y} = ")
score = 0
correct = False
for i in range(3):
    guess = int(input("Ans: "))

    if guess == answer:
       score += 1
       correct = True
       break
    if guess != answer:
       print("EEE")
if correct == False:
  print(f"{x} + {y} = {answer}")

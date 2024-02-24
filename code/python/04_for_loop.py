# Practice "for" loop with lists
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in myList:
  print(number)

# Alternatively:
for number in range(10):
  print(number)

for number in myList:
  if number == 8:
    print(number)
  else:
    print("number not equal 8")

# Looping with a list of strings
newList = ["Taylor Swift ", "Fearless ", "Speak Now ", "Red ", "1989 ", "Reputation ", "Lover ", "folklore ", "evermore ", "Midnights ", "The Tortured Poets Department "]
for album in newList:
  print(album)
  for letter in album:
    print(letter)

for index, album in enumerate(["Taylor Swift", "Fearless", "Speak Now", "Red", "1989", "Reputation", "Lover", "folklore", "evermore", "Midnights", "The Tortured Poets Department"]):
  print(index, album)
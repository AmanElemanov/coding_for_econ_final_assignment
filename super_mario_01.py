# Number of levels in the pyramid
number_levels = 5

# Outer loop for each level
for level in range(1, number_levels + 1):
  # Inner loop for spaces before the hashes
  for space in range(number_levels - level):
    print(" ", end="")

  # Inner loop for hashes
  for hashtag in range(level):
    print("#", end="")

  # Move to the next line after completing each level
  print()


# Using a function
def pyramid(levels):
  # Outer loop for each level
  for level in range(1, levels + 1):
    # Inner loop for spaces before the hashes
    for space in range(levels - level):
          print(" ", end="")

    # Inner loop for hashes
    for hashtag in range(level):
          print("#", end="")

    # Move to the next line after completing each level
    print()

# Example with 7 levels
pyramid(7)
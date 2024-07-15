l = [1,5,4,3,1,8,2,4,2,3,1]

occurrences = 0
occurrences_sought = 2
number_searched = 1
for i, n in enumerate(l):
  if n == number_searched:
    occurrences += 1
    if occurrences == occurrences_sought:
      break
print(f"Occurrence {occurrences_sought} of number {number_searched} is at index {i}.")

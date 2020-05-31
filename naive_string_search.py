def naive_string_search(landscape, target):
  tally = 0

  for i in range(0,len(landscape)):

    for j in range(0, len(target)):

      if target[j] != landscape[i + j]:
        break

    if j == len(target) - 1:
      tally += 1

  return tally

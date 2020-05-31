def countingValleys(n, s):
    level = 0
    level_tracker = []
    zero_tracker = [0]
    valley_count = 0

    for i in range(0,n):
        if s[i] == "D":
            level -= 1
        if s[i] == "U":
            level += 1
        level_tracker.append(level)
    print(level_tracker)

    for z in range(0,n):
      if level_tracker[z] == 0:
        zero_tracker.append(z)
    print(zero_tracker)
    
    for j in range (0, len(zero_tracker)-1):
      start = zero_tracker[j]
      end = zero_tracker[j+1]
      if sum(level_tracker[start:end])<0:
        valley_count += 1
    return valley_count


#test:
mountain_range = "DDUUDDUDUUUD"
print(countingValleys(len(mountain_range), mountain_range))
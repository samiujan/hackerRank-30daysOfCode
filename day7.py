n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
print " ".join(map(str, arr))
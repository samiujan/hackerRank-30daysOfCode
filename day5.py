T = input()
l = []
for _ in range(T):
  l.append(map(int, raw_input().split()))
for i in range(T):
  a, b, N = l[i][0], l[i][1], l[i][2]
  val = 0
  for i in range(0, N): #0, 1, 2, 3, 4
    val += (pow(2, i) * b)
    print a + val,
  print ""

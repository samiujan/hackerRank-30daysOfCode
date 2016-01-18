T = input()

l = []
for _ in range(T):
    l.append(input())

print "\n".join([str(bin(l[i]))[2:] for i in range(T)])

T = input()

p = {}
for _ in range(T):
    name = raw_input()
    number = input()
    p[name] = number

while True:
    query = raw_input()
    if len(query) == 0:
        break

    if query in p:
        print query + "=" + str(p[query])
    else:
        print "Not found"

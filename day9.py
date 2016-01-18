def gcd(a, b):
    if a == b:
        return a
    return gcd(max(a,b)-min(a,b), min(a,b))

a, b = map(int, raw_input().split())

print gcd(a, b)

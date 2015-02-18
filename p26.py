def rec(n):
    (parts, pos, seen) = (10, 1, {})
    while parts:
        parts = (parts % n) * 10
        if parts in seen: return pos - seen[parts]
        seen[parts] = pos
        pos += 1
    return 0

print(max([(rec(n), n) for n in range(2, 1000)])[1])

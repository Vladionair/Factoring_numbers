def factoring(n):
    values = []
    counter = 0
    for i in range(2, n + 1):
        while n % i == 0:
            counter += 1 
            n //= i
        if counter != 0:
            values.append((i, counter))
        counter = 0
        if n == 1:
            break
    result =  ''.join('({} ** {})'.format(i[0], i[1]) if i[1] != 1 else '({})'.format(i[0]) for i in values)
    return result

print(factoring(1234567890))
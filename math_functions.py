#Fundamental Math Functions

def is_prime(n):
    assert type(n) == int
    if n < 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0: #n has a factor
                return False
        return True

def divisor(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst

def prime_factor(x):
    fact_lst = []
    if is_prime(x) is True:
        fact_lst.append(x)
    for i in divisor(x):
        if i == 1:
            pass
        elif is_prime(i) is True:
            fact_lst.append(i)
    return fact_lst

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif a % b == 0:
        return b
    return gcd(b, a % b)

def relatively_prime(a, b):
    while a > 0 and b > 0:
        if gcd(a, b) == 1:
            return True
        else:
            return False

def common_factor(a, b):
    a_fact = divisor(a)
    b_fact = divisor(b)
    common_fact = []
    for elem in a_fact:
        if elem in b_fact:
            common_fact.append(elem)
    return common_fact

def int_to_binary(n):
    x = "{0:b}".format(n) #Bit conversion in-built
    return x

def bit_calculation(n):
    x = int_to_binary(n)
    no_of_bits = len(x)
    return no_of_bits

#Mathematical Functions used in RSA

def totient(p, q):
    return (p-1)*(q-1)

def public_key_choices(totient):
    assert type(totient) == int
    possible_keys = []
    for e in range(3, totient):
        if relatively_prime(e, totient):
            if is_prime(e):
                possible_keys.append(e)
                e += 1
            e += 1
        e += 1
    return possible_keys

def mod(a, b):
    if a < b:
        return a
    else:
        if a//b == 1:
            return a-b
        else:
            return mod(a-b, b)

def private_key(e, totient):
    assert type(e) == int
    assert type(totient) == int
    for d in range(totient):
        x = e * d
        if mod(x, totient) == 1:
            return d

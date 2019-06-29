#Conversion to Binary for additional security

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

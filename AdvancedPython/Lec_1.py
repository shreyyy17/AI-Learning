friends_last_seen ={
    'rolf':6,
    'folf':56,
    'aolf':42,
}

print(id(friends_last_seen))



primes = [2,3,5]

print(id(primes))

# prime += [7,11] it uses __iadd__function
primes= [2,3,5] + [7,11] # this uses __add__ function

print(id(primes))


## Dictionary unpacking =========>
Users = [
    {
        {'username': 'rolf', 'password': '123'},
        {'username': 'tech', 'password': 'youaretoo'},
    }
]


## now here above is the dictionary
# Here now when we need to pass the data as the named parameter
# we need to pass them as below :
# "**data" ===> what this does is that it unpackes the dictionary
# as per the named parameter like currently in the Users Dictionary
# we have 2 data and in that we have 2 key:vaule pairs
# so it passes that value as named parameters
## And if the values are in tuples like below

value = [
    ('username', 'username'),
    ('password', 'password'),
]

## then we can do [User(*data) for data in users]
# we need to add 1 astrick before the variable
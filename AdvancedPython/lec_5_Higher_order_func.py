def greet():
    print('This will ')

def before(func):
    print('Before == ')
    print(func())
    print('after == ')

before(lambda: 5)
before(greet)


movies = [
    {"name":"The Matrix","director":"Wachoski"},
    {"name":"The Matrix 4","director":"Wachoski 4"},
    {"name":"The Matrix t3","director":"Wachoski 3"},
    {"name":"The Matrix d6","director":"Wachoski 5"},
    {"name":"1966","director":"Raju"},
]

def find_movie(expected,finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie
    return None


find_by = input("What property are we searching by ? :")
looking_for= input("what are you looking for?")

movie = find_movie(looking_for,lambda movie: movie[find_by])
print(movie)
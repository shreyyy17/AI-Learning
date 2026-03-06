def add_all(*args):
    return sum(args)


def pretty_print(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}: {v}')


pretty_print(**{'username':'jose123','access_level':'admin'})

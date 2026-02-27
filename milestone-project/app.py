## Add new movie to collection
## List al movie in my collection
## find a movie by movie title

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movie ,  'f' find your movie by title, or 'q' to quit : "
movies = []



def print_movies(movie):
    print(f"Title  {movie['title']}")
    print(f"director  {movie['director']}")
    print(f"year  {movie['year']}")


def add_movie():
    title = input("enter the movie title : ")
    director = input("enter the movie director : ")
    year = input("enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })

def display_movies():
    for movie in movies:
        print_movies(movie)


def find_movie():
    searched_movie = input("enter the movie to find : ")
    for movie in movies:
        if movie['title'] == searched_movie:
            print_movies(movie)


user_options= {
    "a":add_movie,
    "l":display_movies,
    "f":find_movie,
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection in user_options:
            selected_option = user_options[selection]
            selected_option()
        else:
            print("unknown commmand, Please enter a valid option")

        selection = input(MENU_PROMPT)

menu()









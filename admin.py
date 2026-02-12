data=[
    { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
    { "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action","Adventure", "Drama"] },
    { "name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"] }
]


def input_int(prompt):
    while True:
        value=input(prompt)
        if value.isdigit() and int(value) >=1:
            return int(value)
        else:
            print("please enter the valid value >=1 ")


def input_something(prompt):
    while True:
        value=input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannnot be empty ")

print("Welcome to the movie manager")     

while True:
    print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")      
    choice=input("Enter your choice: ").lower()     

    if choice=="a":
        name=input_something("Enter the movie name:")
        year=input_int("Enter the year:")
        duration=input_int("Enter the duration in minutes: ")
        genres_input=input_something("enter the genre (comma-separated): ")
        genres=[g.strip() for g in genres_input.split(",") if g.strip()]
        
        if len(genres)==0:
            print("At least one genre is required")
        else:
            movie={
                "name":name,
                "year":year,
                "duration":duration,
                "genres":genres
            }
            data.append(movie)
            print("Movie added successfully")

    elif choice=="l":
        if len(data)==0:
            print("No movie saved")
        else:
            for index, movie in enumerate(data, start=1):
                print(f"{index} {movie['name']} {movie['year']}")

    elif choice=="s":
        if len(data)==0:
            print("no movies found")
        else:
            term=input_something("enter the search term:").lower()
            found = False        
            for index, movie in enumerate(data, start=1):
                if term in movie["name"].lower():
                    print(f"{index}) {movie['name']} ({movie['year']})")
                    found = True

    elif choice=="v":
        if len(data)==0:
            print("no movies saved")
        else:
            index = input_int("enter the movie index:") 
            if 1<=index<=len(data):
                movie=data[index-1]
                genres=",".join(movie["genres"])
                print(f"\nname: {movie['name']}")
                print(f"year: {movie['year']}")
                print(f"duration: {movie['duration']}")
                print(f"genres: {movie['genres']}")
            else:
                print("invalid index number")

    elif choice=="d":
        if len(data)==0:
            print("no movie found")
        else:
            index=input_int("enter movie index to delete")
            if 1<=index<=len(data):
                deleted=data.pop(index-1)
                print(f"{deleted['name']} deleted successfully")
            else:
                print("invalid index number")

    elif choice=="q":
        print("goodbye")

    else:
        print("invalid choice")
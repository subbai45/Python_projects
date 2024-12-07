import pandas as pd

# Sample dataset of movies with genres
data = {
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight',
              'Pulp Fiction', 'The Lord of the Rings', 'Forrest Gump', 'Inception', 'Fight Club'],
    'Genre': ['Drama', 'Crime', 'Action', 'Crime', 'Fantasy', 'Drama', 'Sci-Fi', 'Drama']
}

# Load data into a DataFrame
movies_df = pd.DataFrame(data)

# Function to display all movies
def display_movies():
    print("Available Movies:\n", movies_df)

# Function to get recommendations by genre
def recommend_movies(genre):
    recommended = movies_df[movies_df['Genre'].str.lower() == genre.lower()]
    if not recommended.empty:
        print(f"\nRecommended Movies in Genre '{genre}':")
        print(recommended[['Title']])
    else:
        print(f"No movies found in the genre '{genre}'.")

        # Add a new movie
        title_input = input("Enter a movie title to add: ")
        genre_input = input("Enter the genre of the movie: ")
        add_movie(title_input, genre_input)

        # Display updated movies
        print("\nUpdated Movie List:")
        display_movies()

# Function to add a new movie to the list
def add_movie(title, genre):
    global movies_df
    new_movie = pd.DataFrame([[title, genre]], columns=['Title', 'Genre'])
    movies_df = pd.concat([movies_df, new_movie], ignore_index=True)
    print(f"Movie '{title}' added successfully!")

# Sample interaction
display_movies()

# Recommend movies based on genre
genre_input = input("Enter a genre to get recommendations: ")
recommend_movies(genre_input)



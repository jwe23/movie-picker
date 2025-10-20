import requests
import os
import random

API_KEY = os.getenv('TMDB_API_KEY')
BASE_URL = "https://api.themoviedb.org/3"

GENRES = {
    '1': ('Action', 28),
    '2': ('Comedy', 35),
    '3': ('Drama', 18),
    '4': ('Horror', 27),
    '5': ('Romance', 10749),
    '6': ('Sci-Fi', 878),
    '7': ('Thriller', 53),
    '8': ('Animation', 16),
    '9': ('Documentary', 99),
}

MOODS = {
    '1': ('Excited', [28, 878, 12]),
    '2': ('Happy', [35, 10749, 16]),
    '3': ('Sad', [18, 10749]),
    '4': ('Scared', [27, 53]),
    '5': ('Thoughtful', [99, 18, 36])
}

def check_api_key():
    """Verify API key is configured"""
    if not API_KEY:
        print("Error: TMDB_API_KEY environment variable not set.")
        print("Configure with: export TMDB_API_KEY='your_key_here'")
        return False
    return True

def get_random_movie_by_genre(genre_id):
    """Fetch a random movie from specified genre"""
    params = {
        'api_key': API_KEY,
        'with_genres': genre_id,
        'sort_by': 'popularity.desc',
        'page': random.randint(1, 5),
        'vote_count.gte': 100
    }
    
    try:
        response = requests.get(f"{BASE_URL}/discover/movie", params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['results']:
            return random.choice(data['results'])
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie: {e}")
        return None

def get_random_movie_by_mood(genre_ids):
    """Fetch a random movie matching mood criteria"""
    genre_id = random.choice(genre_ids)
    return get_random_movie_by_genre(genre_id)

def display_movie(movie):
    """Display formatted movie information"""
    title = movie['title']
    year = movie.get('release_date', 'N/A')[:4]
    rating = movie.get('vote_average', 'N/A')
    overview = movie.get('overview', 'No description available.')
    
    print("\n" + "="*70)
    print(f"{title} ({year})")
    print("="*70)
    print(f"Rating: {rating}/10")
    print(f"\n{overview}")
    print("="*70)

def browse_by_genre():
    """Genre-based browsing interface"""
    print("\n--- Select Genre ---")
    for key, (name, _) in GENRES.items():
        print(f"{key}. {name}")
    
    choice = input("\nEnter genre number: ").strip()
    
    if choice in GENRES:
        genre_name, genre_id = GENRES[choice]
        print(f"\nSearching for {genre_name} movie...")
        
        movie = get_random_movie_by_genre(genre_id)
        if movie:
            display_movie(movie)
            return True
    else:
        print("Invalid selection.")
    
    return False

def browse_by_mood():
    """Mood-based browsing interface"""
    print("\n--- Select Mood ---")
    for key, (mood, _) in MOODS.items():
        print(f"{key}. {mood}")
    
    choice = input("\nEnter mood number: ").strip()
    
    if choice in MOODS:
        mood_name, genre_ids = MOODS[choice]
        print(f"\nSearching for {mood_name.lower()} movie...")
        
        movie = get_random_movie_by_mood(genre_ids)
        if movie:
            display_movie(movie)
            return True
    else:
        print("Invalid selection.")
    
    return False

def search_movie():
    """Search for specific movie by title"""
    query = input("\nEnter movie title: ").strip()
    
    if not query:
        print("Please enter a valid movie title.")
        return False
    
    params = {
        'api_key': API_KEY,
        'query': query
    }
    
    try:
        response = requests.get(f"{BASE_URL}/search/movie", params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['results']:
            movie = data['results'][0]
            display_movie(movie)
            return True
        else:
            print(f"No results found for '{query}'.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error searching: {e}")
    
    return False

def get_random_popular():
    """Get random popular movie from all genres"""
    params = {
        'api_key': API_KEY,
        'sort_by': 'popularity.desc',
        'page': random.randint(1, 5),
        'vote_count.gte': 500
    }
    
    try:
        response = requests.get(f"{BASE_URL}/discover/movie", params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['results']:
            return random.choice(data['results'])
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie: {e}")
        return None

def main():
    """Main application loop"""
    if not check_api_key():
        return
    
    print("Movie Recommendation CLI")
    print("Find your next movie to watch\n")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Browse by genre")
        print("2. Browse by mood")
        print("3. Search specific movie")
        print("4. Random popular movie")
        print("5. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            browse_by_genre()
        elif choice == '2':
            browse_by_mood()
        elif choice == '3':
            search_movie()
        elif choice == '4':
            print("\nSearching for random popular movie...")
            movie = get_random_popular()
            if movie:
                display_movie(movie)
        elif choice == '5':
            print("\nExiting. Enjoy your movie!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        if choice in ['1', '2', '3', '4']:
            again = input("\nGet another recommendation? (y/n): ").strip().lower()
            if again != 'y':
                print("\nExiting. Enjoy your movie!")
                break

if __name__ == "__main__":
    main()

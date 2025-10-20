# movie-picker

CLI tool for discovering movies by genre, mood, or search query using the TMDB API.

## Features

- Browse movies by genre (Action, Comedy, Drama, Horror, Romance, Sci-Fi, Thriller, Animation, Documentary)
- Get recommendations based on current mood
- Search for specific movies by title
- Discover random popular movies
- View movie ratings, release years, and descriptions

## Requirements

- Python 3.6+
- requests library
- TMDB API key (free)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jwe23/movie-picker.git
cd movie-picker
```

2. Install dependencies:
```bash
pip install requests
```

3. Get a free API key from [The Movie Database (TMDB)](https://www.themoviedb.org/settings/api)

4. Set your API key as an environment variable:
```bash
export TMDB_API_KEY='your_api_key_here'
```

For persistence, add the export command to your shell configuration file (.bashrc, .zshrc, etc.)

## Usage

Run the program:
```bash
python movie_picker.py
```

Follow the menu prompts to browse movies:
```
Movie Recommendation CLI
Find your next movie to watch

--- Main Menu ---
1. Browse by genre
2. Browse by mood
3. Search specific movie
4. Random popular movie
5. Exit

Choice: 1

--- Select Genre ---
1. Action
2. Comedy
3. Drama
4. Horror
5. Romance
6. Sci-Fi
7. Thriller
8. Animation
9. Documentary

Enter genre number: 6

Searching for Sci-Fi movie...

======================================================================
Inception (2010)
======================================================================
Rating: 8.4/10

A thief who steals corporate secrets through the use of dream-sharing 
technology is given the inverse task of planting an idea into the mind 
of a C.E.O.
======================================================================
```

## Available Options

### Browse by Genre
Select from 9 different genres to get random movie recommendations within that category.

### Browse by Mood
Choose from 5 moods that map to appropriate genres:
- Excited (Action, Sci-Fi, Adventure)
- Happy (Comedy, Romance, Animation)
- Sad (Drama, Romance)
- Scared (Horror, Thriller)
- Thoughtful (Documentary, Drama, History)

### Search Specific Movie
Search for any movie by title to view its details.

### Random Popular Movie
Get a random recommendation from highly-rated popular movies across all genres.

## Technologies

- Python 3.x
- TMDB API v3
- requests library

## API Usage

This tool uses The Movie Database (TMDB) API. Please review their [terms of use](https://www.themoviedb.org/terms-of-use) and ensure compliance with their API usage guidelines.

## Future Improvements

- Save watched movies list
- Filter by release year or rating threshold
- Display cast and crew information
- Show movie trailers
- Export recommendations to file
- Add pagination for search results

## License

MIT

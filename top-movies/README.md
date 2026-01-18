# Top 10 Movies - Flask Application

A Flask web application that allows users to manage their personal top 10 movies list. The application integrates with The Movie Database (TMDB) API to search for movies and automatically fetch movie details including posters, release dates, and descriptions.

## Features

- **Movie Search**: Search for movies using the TMDB API
- **Add Movies**: Add movies to your personal collection with automatic data fetching
- **Rate & Review**: Add personal ratings (out of 10) and reviews for each movie
- **Dynamic Ranking**: Movies are automatically ranked based on your ratings
- **Update & Delete**: Edit ratings/reviews or remove movies from your list
- **Interactive UI**: Flip card design showing movie posters and details
- **Database Persistence**: All data stored in SQLite database

## Technologies Used

- **Flask**: Web framework
- **Flask-Bootstrap**: UI styling with Bootstrap 5
- **Flask-SQLAlchemy**: Database ORM
- **Flask-WTF**: Form handling and validation
- **WTForms**: Form validation
- **Requests**: HTTP library for API calls
- **TMDB API**: Movie data source
- **SQLite**: Database
- **Python-dotenv**: Environment variable management

## Project Structure

```
top-movies/
├── main.py                 # Main Flask application
├── tmdb.py                 # TMDB API client
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore file
├── instance/
│   └── movies.db          # SQLite database
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Home page with movie list
│   ├── add.html           # Add movie form
│   ├── select.html        # Movie selection from search results
│   └── edit.html          # Edit rating and review
└── static/
    └── css/
        └── styles.css     # Custom styles
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- TMDB API Access Token

### 1. Get TMDB API Access Token

1. Create a free account at [The Movie Database (TMDB)](https://www.themoviedb.org/)
2. Go to Settings → API
3. Request an API key
4. Copy your **API Read Access Token** (Bearer token)

### 2. Installation

1. Clone or navigate to the project directory:


2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration

1. Create a `.env` file in the project root:
```bash
TMDB_ACCESS_TOKEN=your_tmdb_access_token_here
```

2. Replace `your_tmdb_access_token_here` with your actual TMDB API Read Access Token

> [!IMPORTANT]
> Never commit your `.env` file to version control. Add it to `.gitignore` to keep your API token secure.

### 4. Run the Application

```bash
python main.py
```

The application will start on `http://127.0.0.1:5000/`

## Usage

### Adding a Movie

1. Click the **"Add Movie"** button on the home page
2. Enter the movie title in the search form
3. Select the correct movie from the search results
4. Add your rating (out of 10) and review
5. Click **"Done"** to save

### Updating a Movie

1. Hover over a movie card and click **"Update"**
2. Modify the rating or review
3. Click **"Done"** to save changes

### Deleting a Movie

1. Hover over a movie card and click **"Delete"**
2. The movie will be removed from your list

### Viewing Rankings

- Movies are automatically ranked from 1-10 based on your ratings
- Higher ratings receive better rankings
- Rankings update automatically when ratings change

## Database Schema

### Movie Model

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| title | String(250) | Movie title (unique) |
| year | Integer | Release year |
| description | String(500) | Movie overview/synopsis |
| rating | Float | Your rating (out of 10) |
| ranking | Integer | Calculated ranking (1-10) |
| review | String(250) | Your personal review |
| img_url | String(250) | TMDB poster image URL |

## API Integration

The application uses the TMDB API v3 with the following endpoints:

- **Search Movies**: `/search/movie` - Search for movies by title
- **Get Movie Details**: `/movie/{movie_id}` - Fetch detailed movie information

The `TMDBClient` class in `tmdb.py` handles all API interactions with proper error handling and authentication.

## Dependencies

```
Bootstrap_Flask==2.2.0
Requests==2.31.0
WTForms==3.0.1
Flask_WTF==1.2.1
Werkzeug==3.0.0
Flask==2.3.2
flask_sqlalchemy==3.1.1
SQLAlchemy==2.0.25
python-dotenv
```

## Security Notes

- The Flask secret key in `main.py` should be changed for production use
- Store sensitive data (API tokens) in environment variables
- Never commit `.env` files to version control
- The application runs in debug mode by default - disable for production

## Troubleshooting

### "TMDB_ACCESS_TOKEN not found in environment variables"
- Ensure you've created a `.env` file with your TMDB access token
- Check that `python-dotenv` is installed

### Database errors
- Delete the `instance/movies.db` file and restart the application to recreate the database

### API errors
- Verify your TMDB access token is valid
- Check your internet connection
- Ensure you're not exceeding TMDB API rate limits

## Future Enhancements

- User authentication for multiple users
- Movie recommendations based on ratings
- Export/import movie lists
- Advanced filtering and sorting options
- Movie trailers and additional media
- Social sharing features

## License

This project is part of the Angela Yu 100 Days of Python course (Day 64).

## Acknowledgments

- Movie data provided by [The Movie Database (TMDB)](https://www.themoviedb.org/)
- Course by Angela Yu

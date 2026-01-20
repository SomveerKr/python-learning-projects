# Cafe & WiFi API

A RESTful API built with Flask and SQLAlchemy for managing cafe information, including amenities like WiFi, power sockets, and workspace suitability. This API allows users to search for cafes, add new locations, update prices, and report closures.

## Features

- **Random Cafe**: Get a random cafe from the database
- **Search Cafes**: Search for cafes by location
- **List All Cafes**: Retrieve all cafes in the database
- **Add New Cafe**: Add a new cafe with detailed information
- **Update Prices**: Update coffee prices for existing cafes
- **Report Closures**: Delete cafes that have closed (requires API key authentication)

## Technologies Used

- **Flask**: Web framework for building the API
- **Flask-SQLAlchemy**: ORM for database operations
- **SQLite**: Database for storing cafe information
- **SQLAlchemy 2.0**: Modern SQLAlchemy with declarative base and mapped columns

## Database Schema

The `Cafe` model includes the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key |
| `name` | String(250) | Cafe name (unique) |
| `map_url` | String(500) | Google Maps URL |
| `img_url` | String(500) | Cafe image URL |
| `location` | String(250) | Cafe location/area |
| `seats` | String(250) | Number of available seats |
| `has_toilet` | Boolean | Restroom availability |
| `has_wifi` | Boolean | WiFi availability |
| `has_sockets` | Boolean | Power socket availability |
| `can_take_calls` | Boolean | Suitable for phone calls |
| `coffee_price` | String(250) | Coffee price (optional) |

## API Endpoints

### 1. Get Random Cafe
```
GET /random
```
Returns a random cafe from the database.

**Response:**
```json
{
  "id": 1,
  "name": "Cafe Name",
  "map_url": "https://maps.google.com/...",
  "img_url": "https://example.com/image.jpg",
  "location": "Peckham",
  "seats": "50",
  "has_toilet": true,
  "has_wifi": true,
  "has_sockets": true,
  "can_take_calls": false,
  "coffee_price": "£2.50"
}
```

### 2. Get All Cafes
```
GET /all
```
Returns all cafes in the database.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Cafe 1",
    ...
  },
  {
    "id": 2,
    "name": "Cafe 2",
    ...
  }
]
```

### 3. Search Cafes by Location
```
GET /search?loc=<location>
```
Search for cafes in a specific location.

**Parameters:**
- `loc` (query parameter): Location to search for

**Response (Success):**
```json
{
  "cafes": [
    {
      "id": 1,
      "name": "Cafe Name",
      "location": "Peckham",
      ...
    }
  ]
}
```

**Response (Not Found):**
```json
{
  "error": {
    "Not Found": "Sorry, we don't have cafe at that location."
  }
}
```
Status Code: `404`

### 4. Add New Cafe
```
POST /add-cafe
```
Add a new cafe to the database.

**Form Data:**
- `name`: Cafe name
- `map_url`: Google Maps URL
- `img_url`: Image URL
- `location`: Location/area
- `seats`: Number of seats
- `has_toilet`: "True" or "False"
- `has_wifi`: "True" or "False"
- `has_sockets`: "True" or "False"
- `can_take_calls`: "True" or "False"
- `coffee_price`: Price (e.g., "£2.50")

**Response:**
```json
{
  "response": {
    "Success": "Cafe added successfully to the database."
  }
}
```

### 5. Update Coffee Price
```
PATCH /update-price/<cafe_id>?new_price=<price>
```
Update the coffee price for a specific cafe.

**Parameters:**
- `cafe_id` (path parameter): ID of the cafe
- `new_price` (query parameter): New coffee price

**Response (Success):**
```json
{
  "response": {
    "success": "Successfully updated the price."
  }
}
```
Status Code: `200`

**Response (Not Found):**
```json
{
  "error": {
    "Not Found": "Sorry a cafe with that id was not found in the database."
  }
}
```
Status Code: `404`

### 6. Report Cafe Closed
```
DELETE /report-closed/<cafe_id>?api_key=<your_api_key>
```
Delete a cafe from the database (requires API key authentication).

**Parameters:**
- `cafe_id` (path parameter): ID of the cafe
- `api_key` (query parameter): API key for authentication

**Response (Success):**
```json
{
  "success": "Successfully deleted the cafe."
}
```

**Response (Unauthorized):**
```json
{
  "error": "Sorry that's not allowed, make sure that you have correct API key."
}
```
Status Code: `403`

**Response (Not Found):**
```json
{
  "error": {
    "Not Found": "Sorry a cafe with that id was not found in the database."
  }
}
```
Status Code: `404`

## Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd cafe-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install flask flask-sqlalchemy
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

6. **Access the API**:
   - Home page: `http://127.0.0.1:5000/`
   - API endpoints: `http://127.0.0.1:5000/<endpoint>`

## API Documentation

For detailed API documentation with examples, visit the [Postman Documentation](https://documenter.getpostman.com/view/21604542/2sBXVhCAHV).

## Project Structure

```
cafe-api/
├── instance/
│   └── cafes.db          # SQLite database
├── templates/
│   └── index.html        # Home page template
├── main.py               # Main application file
└── README.md             # This file
```

## Security Notes

> [!WARNING]
> The API key in this project (`TopSecretAPIKey`) is hardcoded for demonstration purposes only. In a production environment, you should:
> - Store API keys in environment variables
> - Use a secure key management system
> - Implement proper authentication and authorization

## Usage Examples

### Using cURL

**Get a random cafe:**
```bash
curl http://127.0.0.1:5000/random
```

**Search for cafes:**
```bash
curl http://127.0.0.1:5000/search?loc=Peckham
```

**Add a new cafe:**
```bash
curl -X POST http://127.0.0.1:5000/add-cafe \
  -d "name=New Cafe" \
  -d "map_url=https://maps.google.com" \
  -d "img_url=https://example.com/image.jpg" \
  -d "location=Shoreditch" \
  -d "seats=30" \
  -d "has_toilet=True" \
  -d "has_wifi=True" \
  -d "has_sockets=True" \
  -d "can_take_calls=False" \
  -d "coffee_price=£3.00"
```

**Update coffee price:**
```bash
curl -X PATCH "http://127.0.0.1:5000/update-price/1?new_price=£2.75"
```

**Delete a cafe:**
```bash
curl -X DELETE "http://127.0.0.1:5000/report-closed/1?api_key=mkneu4yjedu8734uioefi893489"
```

## Learning Objectives

This project demonstrates:
- Building RESTful APIs with Flask
- CRUD operations with SQLAlchemy
- HTTP methods (GET, POST, PATCH, DELETE)
- API authentication with API keys
- Error handling and status codes
- Database modeling and relationships
- Converting database models to JSON

## Future Enhancements

- [ ] Implement user authentication with JWT tokens
- [ ] Add pagination for the `/all` endpoint
- [ ] Add filtering options (by amenities, price range, etc.)
- [ ] Implement rate limiting
- [ ] Add input validation and sanitization
- [ ] Create a frontend interface for easier interaction
- [ ] Add image upload functionality
- [ ] Implement cafe ratings and reviews

## License

This project is part of the Angela Yu 100 Days of Python course.

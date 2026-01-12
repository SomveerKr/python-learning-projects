# Blog with Contact Form - Flask Application

A Flask-based blog application that displays blog posts fetched from an external API and includes a functional contact form with email notification capabilities.

## Features

- **Dynamic Blog Posts**: Fetches and displays blog posts from an external API (npoint.io)
- **Individual Post Pages**: Each blog post has its own dedicated page with full content
- **Contact Form**: Fully functional contact form that sends email notifications
- **Email Integration**: Automated email sending using SMTP with Gmail
- **About Page**: Information about the blog author
- **Responsive Design**: Clean, modern UI with Bootstrap styling
- **Template Inheritance**: Modular design using Jinja2 templates with reusable header and footer components

## Project Structure

```
blog_contact_form_flask/
├── server.py              # Main Flask application
├── send_email.py          # Email sender class for handling SMTP operations
├── .env                   # Environment variables (not tracked in git)
├── .gitignore            # Git ignore configuration
├── templates/
│   ├── index.html        # Home page with blog post listings
│   ├── post.html         # Individual blog post page
│   ├── about.html        # About page
│   ├── contact.html      # Contact form page
│   ├── header.html       # Reusable header component
│   └── footer.html       # Reusable footer component
└── static/
    ├── assets/           # Static assets (images, etc.)
    ├── css/              # Stylesheets
    └── js/               # JavaScript files
```

## Technologies Used

- **Flask**: Web framework for Python
- **Jinja2**: Template engine for dynamic HTML rendering
- **Requests**: HTTP library for fetching blog data from external API
- **SMTP (smtplib)**: Email sending functionality
- **Python-dotenv**: Environment variable management
- **Bootstrap**: Frontend styling framework

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system
- A Gmail account for sending emails (or another SMTP server)
- Gmail App Password (if using Gmail with 2FA enabled)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   60_blog_contact_form_flask
   ```

2. **Install required dependencies**:
   ```bash
   pip install flask requests python-dotenv
   ```

3. **Create a `.env` file** in the project root with the following variables:
   ```env
   EMAIL_ID=your_email@gmail.com
   EMAIL_PASS=your_app_password
   ```

   > **Note**: For Gmail, you'll need to generate an [App Password](https://support.google.com/accounts/answer/185833) if you have 2-factor authentication enabled.

### Running the Application

1. **Start the Flask development server**:
   ```bash
   python server.py
   ```

2. **Access the application** in your web browser:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

### Viewing Blog Posts

- Navigate to the home page to see all available blog posts
- Click on any post to view its full content on a dedicated page

### Using the Contact Form

1. Navigate to the **Contact** page
2. Fill in the required fields:
   - Name
   - Email
   - Phone
   - Message
3. Submit the form
4. Upon successful submission, an email will be sent to the configured recipient email address

### API Integration

The application fetches blog posts from:
```
https://api.npoint.io/57303010b8ea0f9272e8
```

You can replace this URL with your own API endpoint by modifying the `blog_res` variable in `server.py`.

## Key Components

### EmailSender Class (`send_email.py`)

A reusable email sender class that handles:
- SMTP connection management
- Email composition and sending
- Error handling for authentication and connection issues
- Support for custom SMTP servers and ports

### Flask Routes

- `GET /` - Home page with blog post listings
- `GET /blog/<id>` - Individual blog post page
- `GET /about` - About page
- `GET /contact` - Display contact form
- `POST /contact` - Handle contact form submission and send email

## Configuration

### Email Settings

By default, the application uses Gmail's SMTP server:
- **Server**: `smtp.gmail.com`
- **Port**: `587`
- **TLS**: Enabled

To use a different email provider, modify the `EmailSender` initialization in `server.py` or update the default values in `send_email.py`.

### Recipient Email

The contact form sends emails to `work.somveerk@gmail.com` by default. Update the `recipient` variable in the `/contact` route to change this.

## Security Considerations

- **Environment Variables**: Never commit your `.env` file to version control
- **App Passwords**: Use Gmail App Passwords instead of your main account password
- **Input Validation**: Consider adding form validation to prevent spam and malicious input
- **Rate Limiting**: Implement rate limiting to prevent abuse of the contact form

## Future Enhancements

- Add form validation (client-side and server-side)
- Implement CAPTCHA to prevent spam
- Add database support for storing blog posts locally
- Create an admin panel for managing blog posts
- Add user authentication and comments functionality
- Implement rate limiting for contact form submissions

## Troubleshooting

### Email Not Sending

1. Verify your `.env` file contains correct credentials
2. Ensure you're using an App Password (not your regular Gmail password)
3. Check if "Less secure app access" is enabled (if not using App Password)
4. Review console output for specific error messages

### Blog Posts Not Loading

1. Check your internet connection
2. Verify the API endpoint is accessible
3. Check console for any error messages from the requests library

## License

This project is for educational purposes as part of Python learning projects.

## Author

Somveer Kumar

---

**Note**: This is a learning project demonstrating Flask web development, API integration, form handling, and email automation.

# File Share Project

A simple file sharing platform built with **Django** and **MySQL**, allowing users to upload and share files securely. This project includes a basic file upload system, with support for file expiration and password protection (optional).

## Features
- User authentication (login, register)
- Secure file upload and download
- Password protection for files (optional)
- Expiry settings for files (optional)
- Admin panel for file management
- Supports large file uploads (up to 2GB)

## Technologies Used
- **Backend**: Django (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS (Tailwind CSS for styling)
- **Security**: .env file for sensitive information (e.g., DB credentials)

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- MySQL server running on your local machine or remote host

### 1. Clone the Repository
Clone this project to your local machine using:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies
Install required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database
1. Create a MySQL database for the project:
   ```sql
   CREATE DATABASE fileshare_db CHARACTER SET UTF8MB4;
   ```

2. Add the database credentials to your `.env` file:

   Create a `.env` file in the root of the project and add the following content:
   ```env
   SECRET_KEY=your-very-secret-django-key
   DEBUG=False
   DB_NAME=fileshare_db
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

### 4. Run Migrations
Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)
Create an admin superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### 6. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the app.

---

## Contributing

Feel free to fork this project and submit pull requests for any improvements or features.

---

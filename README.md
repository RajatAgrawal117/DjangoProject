
# Django Form Submission Project

This project is a simple Django application that allows users to submit their names and email addresses through a form. Users can view all submitted forms on a separate submissions page.

## Features

- User-friendly form submission.
- Displays current time on the home page.
- View all submissions in a table format.
- Basic validation for form fields.
- User feedback for successful and unsuccessful submissions.

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS
- **Database:** SQLite (default)
- **Python Libraries:** Django

## UI
![image](https://github.com/user-attachments/assets/7a06bb7d-03b1-4c5b-a338-67a3527956e7)
![image](https://github.com/user-attachments/assets/376a98e0-60d6-4fd9-922e-609e09fe2523)


## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-form-submission.git
   cd django-form-submission
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install django
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional for accessing the admin panel):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- Navigate to the home page to view the form.
- Fill in the name and email fields and submit the form.
- You will receive feedback based on the submission.
- View all submissions by navigating to the submissions page.


## Author

Rajat Agrawal


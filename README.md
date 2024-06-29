# Petrol Pump Management System (Django E-Commerce Website)

![screenshot](screenshot/home.png)

# Overview

The Petrol Pump Management System is a comprehensive software solution designed for managing various aspects of a petrol pump or gas station.
It includes functionalities for administrators to oversee operations, as well as features tailored for user interactions such as sales reporting,
leave management, attendance tracking, and customer feedback.

#Key Features

# Admin Dashboard:
Provides administrators with access to manage categories, user accounts, sales reports, attendance records, and leave approvals.
# User Page:
Allows users to view their attendance status, apply for leave, submit feedback, update details, change profile picture, 
and change password.
# Category Management:
Enables administrators to add, edit, and delete product categories for inventory management.
# Sales Reporting:
Generates reports on sales transactions, providing insights into product performance and revenue.
# User Table:
Displays a list of users with relevant details such as employee information and attendance records.
# Leave Management:
Facilitates the application and approval process for employee leave requests.
# Attendance Tracking:
Tracks employee attendance to monitor punctuality and performance.
# Feedback System:
Allows users to submit feedback, suggestions, or complaints for continuous improvement.
# Password Security:
Upon successful signup, the user's username and password are securely mailed to their registered email address.
# Sweetify Integration:
Sweetify messages appear for all operations done, providing users with instant feedback and notifications.

Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Django (Python)
Database: SQLite (for development), PostgreSQL (for production)
Other Tools: Django Templates, Sweetify (for notifications), Django FileField (for file uploads), etc.

# Installation

# 1. Clone the repository:
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

# 2. Install dependencies:

pip install -r requirements.txt

# 3. Set up the database:

python manage.py migrate

# 4. Create a superuser:

python manage.py createsuperuser

# 5. Run the development server:

python manage.py runserver

# 6. Access the application:

Open your web browser and go to http://localhost:8000/

# Usage
Navigate to http://localhost:8000/ to access the website.
Admin Actions:
Log in as an admin to manage categories, user accounts, sales reports, and leave approvals.
User Interactions:
Users can access their page to view attendance, apply for leave, submit feedback, update details, change profile picture,
and change password.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

# Customization
Customize the template according to your project’s specific details, structure, and preferences. Ensure clarity and completeness so that anyone visiting your repository can understand and use your project effectively.








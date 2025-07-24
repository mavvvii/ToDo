# Application Functionality

## 📚 Contents
- [Application Description](#application-description)
- [Main Functionality](#main-functionality)
- [Page-by-Page Functionality](#page-by-page-functionality)
- [Modules](#modules)
- [Future Features](#future-features)

---

## Application Description
**ToDo Application** allows users to manage their tasks efficiently through categorized lists. Users can register, log in, and organize their to-dos across multiple boards (e.g., for work, school, or personal life). The app supports account management, dark mode, and multilingual settings.

---

## Main Functionality
- User registration and login with validation
- Email-based account confirmation and password recovery
- Task organization via categorized boards
- Ability to add, edit, delete, and archive tasks and boards
- Profile management (avatar, description, email, password)
- Dark/light mode toggle
- Multilingual interface (Polish and English)

---

## Page-by-Page Functionality

### Login Page
- Users can log in to their account using login and password
- Password reset available via email if forgotten
- Button to navigate to the registration page
- Validation messages for incorrect credentials

### Register Page
- Users can create an account using:
  - Unique username
  - Secure password (min. length, one uppercase letter, one special character)
  - Unique email address
- Validation messages for incorrect credentials
- After registration, users must confirm their email via an automatic confirmation link
- Unconfirmed users cannot log in

### Main Page (Dashboard)
- Logged-in users can create separate boards (e.g., "Work", "School")
- Boards contain individual ToDo items that can be added, edited, and deleted
- Boards can be archived and restored (within 7 days after deletion)
- Each ToDo item includes:
  - Title
  - Description
  - Creation date
  - Deadline date
- Navigation to Profile Page is available
- Users can toggle between light/dark mode
- Language can be switched (currently Polish and English)

### Profile Page
- Users can upload or change their avatar
- Edit personal description
- Change email and password

---

## Modules

### Authentication
- Secure registration with input validation
- JWT-based login authentication
- Password reset via email
- Email-based account confirmation

### User Profile
- Edit user details (email, password)
- Upload/change avatar
- Edit user description

### Settings
- Switch between light and dark modes
- Change application language (Polish / English)

---

## Future Features

- Email notifications reminding users of upcoming ToDo deadlines
- Calendar view for deadlines
- Tagging system for tasks (e.g., #urgent, #important)
- Share boards with other users (collaborative to-do lists)
- Activity history (track changes made to tasks and boards)
- Export tasks to CSV or PDF
- Integration with Google Calendar or Outlook

---

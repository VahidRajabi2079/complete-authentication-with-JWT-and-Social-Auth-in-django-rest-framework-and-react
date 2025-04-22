# 🛠 Complete Authentication with JWT & Social Auth in Django Rest Framework

This project demonstrates a complete authentication system using JWT (JSON Web Tokens) and social authentication (Google, Facebook, etc.) in Django Rest Framework (DRF). It's perfect for building secure REST APIs with token-based authentication and integration with third-party login services.

## 🚀 Features
- **JWT Authentication**: Secure login and token management.
- **Social Authentication**: Login via external platforms like Google and Facebook.
- **DRF-based API**: CRUD operations for users and authentication management.
- **Fully Customizable**: Easily extendable with more social login providers.

## 🛠 Technologies Used
- **Django**
- **Django Rest Framework (DRF)**
- **JWT (JSON Web Token)**
- **drf-yasg**: For generating API documentation (Swagger UI and Redoc).
- **Social Auth**: For third-party login integrations.

## 🏁 Setup Instructions

### Backend Setup
1. **Clone the repository**:
    ```bash
    git clone <repo-url>
    ```
2. **Install dependencies**:
    ```bash
    pipenv install
    ```
3. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```
4. **Create a superuser** (for admin panel):
    ```bash
    python manage.py createsuperuser
    ```
5. **Run the server**:
    ```bash
    python manage.py runserver
    ```

### 📝 API Documentation
Once the server is running, you can access the API documentation at the following endpoints:

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 📚 Resources
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [JWT Authentication](https://jwt.io/introduction/)
- [drf-yasg Documentation](https://drf-yasg.readthedocs.io/en/stable/)
- [Python Social Auth Documentation](https://python-social-auth.readthedocs.io/en/latest/)

## ⚖️ License
This project is licensed under the BSD License - see the [LICENSE](LICENSE) file for details.

---

## 🎯 Want to Contribute?
Feel free to fork the repository, create issues, and submit pull requests. Contributions are welcome! ✨

---

### 🔧 Badges

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-BSD-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

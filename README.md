# Session-Based Authentication Using Django REST Framework

This is a Django application implementing session-based authentication using Django REST Framework (DRF). The application provides user login functionality and utilizes Django's templating system.

## Project Structure

``` .
├── manage.py
├── requirements.txt
├── session_api
│ ├── admin.py
│ ├── apps.py
│ ├── init.py
│ ├── models.py
│ ├── serializer.py
│ ├── templates
│ │ └── registration
│ │ └── login.html
│ ├── tests.py
│ ├── urls.py
│ └── views.py
└── Session_Based_API
├── asgi.py
├── init.py
├── pycache
│ ├── init.cpython-310.pyc
│ ├── settings.cpython-310.pyc
│ ├── urls.cpython-310.pyc
│ └── wsgi.cpython-310.pyc
├── settings.py
├── urls.py
└── wsgi.py
```


### `manage.py`

- A command-line utility that lets you interact with this Django project in various ways.

### `requirements.txt`

- Lists the Python packages that your project depends on. You can install these dependencies using `pip`.

### `session_api/`

- **`admin.py`**: Registers models with the Django admin site.
- **`apps.py`**: Configuration for the `session_api` application.
- **`__init__.py`**: Marks the directory as a Python package.
- **`models.py`**: Contains the data models for the application.
- **`serializer.py`**: Defines serializers for converting complex data types, such as Django models, into JSON and vice versa.
- **`templates/registration/login.html`**: HTML template for the login page.
- **`tests.py`**: Contains test cases for the application.
- **`urls.py`**: Defines URL patterns for the `session_api` application.
- **`views.py`**: Contains view functions or class-based views that handle HTTP requests and responses.

### `Session_Based_API/`

- **`asgi.py`**: ASGI configuration for the application, used for handling asynchronous server gateway interface requests.
- **`__init__.py`**: Marks the directory as a Python package.
- **`__pycache__/`**: Contains compiled Python files.
- **`settings.py`**: Contains the settings and configuration for the Django project, including database settings and installed apps.
- **`urls.py`**: Defines URL patterns for the project.
- **`wsgi.py`**: WSGI configuration for the application, used for deploying the application in a WSGI-compatible server.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Harshyadav02/Session-Based-Authentication-Using-DRF/
    cd Session-Based-Authentication-Using-DRF
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Run the application:**

    ```sh
    python manage.py runserver
    ```

## Configuration

- **`settings.py`**: Configure your Django settings, including database, authentication, and middleware settings.
- **`urls.py`**: Define URL patterns for routing requests to the appropriate views.
- **`views.py`**: Implement view logic to handle requests and return responses.
- **`serializer.py`**: Define serializers to convert between complex data types and JSON.

## Templates

- **`login.html`**: The login page template located in `session_api/templates/registration/login.html`. This template is used for user authentication.


### Notes
    1. This application uses Django's session-based authentication system.
    2. Ensure to configure Django settings as needed for your environment.
    3. Make sure to handle sensitive data securely and follow best practices for authentication.

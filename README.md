# AI-Excel Chat with Django, MindsDB, and OpenAI

This project demonstrates how to create an AI-powered chat application using Django, MindsDB, and GEMINI, all containerized with Docker.

## Contain

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: MindsDB, SQLite, PostgreSQL

## Features

- Chat interface for user interaction
- Predictions made by MindsDB
- user id create through PostgreSQL
- Containerized setup using Docker and Docker Compose

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- django
- MindsDB or mindsdb_sdk
- Docker
- docker-compose

  
### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/rupacesigdel/Excel_using_AI.git
    cd Excel_using_AI
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **mindsdb install and start port**:
    ```sh
    pip install mindsdb
    python -m mindsdb
    ```
5. **Making sure that PostgreSQL server is running on localhost.t**:
    ```sh
    pip install mindsdb
    psql -h localhost -U rupeshsigdel -d aiexcel
    ```

6. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

8. **Open your browser and visit**:
    ```
    http://127.0.0.1:8000/
    ```

## Usage

- **chatbot**: Click on the "chatbot" button on the home page, text a messages with ai about Excel question like formulas, rules, project, feature of excel etc.



## project structure
- ├── .venv
- ├── AI_Excel
- │   ├── __init__.py
- │   ├── docker-compose.yml
- │   ├── settings.py
- │   ├── urls.py
- │   ├── wsgi.py
- ├──aiexcel
- │   ├── admin.py
- │   ├── ai_tools.py
- │   ├── mindsdb_tools.py
- │   ├── requests.py
- │   ├── templates
- │   │   └── chat.html
- │   │   └── home.html
- │   │   └── login.html
- │   │   └── signup.html
- │   ├── urls.py
- │   ├── views.py
- ├── static
- │   ├── css
- │   │   └── styles.css
- │   │   └── js
- │   │       └── script.js
- ├── db.sqlite3
- ├── .gitignore
- ├── LICENSE
- ├── manage.py
- └── README.md
- ├── MANIFEST.in
- ├── postgre.sql
- └── requirements.txt
- └── setup.py
- └── test_db_connection

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to the branch
6. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration from various online excel using AI knowledge, tutorials and projects.
- Thanks to the contributors and the open-source community.

---

Feel free to customize this `README.md` file according to your project's specific details and requirements.

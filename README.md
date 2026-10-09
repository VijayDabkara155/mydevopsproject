# DevOps Task Manager

A containerized task management application built with Flask and PostgreSQL, using Docker Compose for local development and pytest for automated testing.

## Architecture

```text
User / Browser
      |
      v
Flask Application (Port 5000)
      |
      v
PostgreSQL Database (Port 5432)
```

Docker Compose manages the application and database containers, their configuration, and persistent database storage.

## Tech Stack

- **Application:** Python, Flask
- **Database:** PostgreSQL 16
- **Containers:** Docker, Docker Compose
- **Testing:** pytest
- **Version Control:** Git, GitHub

## Project Structure

```text
mydevopsproject/
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── tests/
│   └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── .gitignore
└── README.md
```

## Prerequisites

- Docker Engine
- Docker Compose
- Git

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/VijayDabkara155/mydevopsproject.git
cd mydevopsproject
```

### 2. Configure environment variables

Create a local `.env` file in the project root. Use the same variable names expected by `docker-compose.yml`:

```dotenv
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=choose_a_strong_local_password
```

Use your own values. Never commit `.env` or real credentials to GitHub.

### 3. Start the application

```bash
docker compose up -d --build
```

Check the running containers:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f app
```

### 4. Access the application

Open the following URL in your browser:

http://localhost:5000

Health endpoint:

http://localhost:5000/health

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Displays the task manager page |
| GET | `/health` | Checks application health |
| GET | `/tasks` | Retrieves tasks |
| POST | `/tasks` | Creates a task |

Example request to create a task:

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Kubernetes"}'
```

## Testing

Run the automated test suite from the project root.

Install the Python dependencies in your active virtual environment if needed:

```bash
pip install -r app/requirements.txt
pip install pytest
```

Configure the test database connection using the appropriate local values:

```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=your_database_name
export DB_USER=your_database_user
export DB_PASSWORD=your_database_password
```

Ensure the PostgreSQL container is running and these values match your local `.env` configuration, then run:

```bash
pytest -v
```

## Data Persistence

The PostgreSQL data directory is backed by a named Docker volume. This helps preserve database data when containers are recreated.

To stop the containers without removing the database volume:

```bash
docker compose down
```

**Warning:** `docker compose down -v` removes the Compose-managed volume and can delete stored database data. Use it only when you intentionally want to reset the database.

## Security Notes

- Keep `.env` out of version control.
- Use strong passwords, including for local development.
- Do not expose PostgreSQL publicly in a production deployment.
- Use secret management and least-privilege access for production environments.

## DevOps Roadmap

- [x] Flask application and REST endpoints
- [x] PostgreSQL integration
- [x] Docker containerization
- [x] Docker Compose orchestration
- [x] Automated pytest tests
- [x] Git and GitHub version control
- [ ] GitHub Actions CI pipeline
- [ ] Container image security scanning
- [ ] Kubernetes deployment
- [ ] Infrastructure as Code with Terraform
- [ ] Monitoring and logging

## Author

Vijay Dabkara

GitHub: https://github.com/VijayDabkara155

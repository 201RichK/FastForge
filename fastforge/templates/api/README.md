# {{project_name}}

FastAPI project generated with FastForge 🚀

## Features

- FastAPI with async SQLAlchemy
- PostgreSQL database
- Docker support
- JWT Authentication
- API documentation with Swagger/ReDoc
- Pre-configured testing with pytest
- GitHub Actions CI/CD
- Code formatting with Black and isort
- Type checking with mypy
- Security headers and CORS

## Quick Start

1. Clone the repository
```bash
git clone https://github.com/yourusername/{{project_name}}
cd {{project_name}}
```

2. Install dependencies
```bash
poetry install
```

3. Run the application
```bash
poetry run uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for the API documentation.

## Project Structure

```
{{project_name}}/
├── README.md          # Project documentation
├── pyproject.toml     # Python dependencies
├── app/
│   ├── main.py       # FastAPI application
│   ├── core/         # Core modules (config, security)
│   ├── api/          # API endpoints
│   ├── models/       # SQLAlchemy models
│   └── schemas/      # Pydantic schemas
└── tests/            # Test suite
```

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Formatting
```bash
poetry run black .
poetry run isort .
```

### Type Checking
```bash
poetry run mypy .
```

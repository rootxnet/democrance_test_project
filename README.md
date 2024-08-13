
# Democrance Test Project

This project uses Docker and Docker Compose to manage development and testing environments. Below you'll find instructions on how to use the `Makefile` included with this project to manage various tasks.

## Prerequisites

- Docker: Ensure you have Docker installed and running on your machine.
- Docker Compose: Required for managing multi-container Docker applications.

## Environment Setup

The project includes an environment file (`./tools/env/dev.env`) that is automatically included and exported by the `Makefile`. Ensure that this file is properly configured before running any commands.

## Quick Start

```bash
make && make test
```

## Makefile Commands

### Default Command

```bash
make
```

This will run the default target, which is currently set to `run`.

### Start the Application

```bash
make start
```

This command will start the application in detached mode using Docker Compose.

### Stop the Application

```bash
make stop
```

This command will stop the application and remove the containers.

### View Logs

```bash
make logs
```

This will display the logs for the running Docker containers.

### Build the Application

```bash
make build
```

This command will run several build-related tasks:
- `docker-build`: Builds the Docker images defined in the `docker-compose.yml` file.
- `collectstatic`: Collects static files using Django's `collectstatic` command.
- `migrate`: Runs Django database migrations.

### Manage Django Commands

#### Collect Static Files

```bash
make collectstatic
```

This command will collect static files for the Django application.

#### Apply Migrations

```bash
make migrate
```

This command will apply all migrations.

#### Make Migrations

```bash
make makemigrations
```

This command will create new migrations based on the changes detected.

#### Flush Database

```bash
make flush-db
```

This command will flush the database, removing all data.

#### Reset Database

```bash
make reset-db
```

This command will reset the database completely.

#### Create Superuser

```bash
make createsuperuser
```

This command will create a new superuser for the Django application.

#### Start a New Django App

```bash
make app app_name=your_app_name
```

This command will create a new Django app with the name specified.

### Manage Data Fixtures

#### Load Initial Fixtures

```bash
make load-initial-fixtures
```

This command will load the initial data fixtures from `initial_data.json`.

#### Export Fixtures

```bash
make export-fixtures
```

This command will export the current data as JSON fixtures.

### Testing

#### Run Tests

```bash
make test
```

This command will run the Django tests.

### Code Quality

#### Run Ruff

```bash
make ruff
```

This command will run Ruff to check and fix Python code issues according to the project’s linting rules.

### Purge and Clean Up

```bash
make purge
```

This command will stop the Docker containers, remove volumes, and clean up any orphaned containers. It will also delete all files in the `./static/` directory.

### Access the CLI

```bash
make cli
```

This command will give you a shell access within the running `cli` container.

# Job Portal (Django)

## Project Overview
This is a **Job Portal** web application built with Django. It supports Employer and Employee workflows such as:
- Public job browsing (list + details)
- Job creation for employers
- Job apply and bookmark for employees
- Employer dashboard for managing applicants
- Authentication and profile management
- Admin panel and media/static handling
- API documentation via Swagger/Redoc

## Tech Stack
- **Python 3**
- **Django**
- **Django REST Framework (DRF)**
- **drf-yasg** (Swagger / Redoc)
- **django-filter**
- **CKEditor 5**
- **Cloudinary** (media/file storage)
- **PostgreSQL** (database)
- **WhiteNoise** (static serving)

## Local Setup

### 1) Create and activate virtual environment
```bash
python -m venv env
.
	env\Scripts\activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure environment variables (.env)
Create a `.env` file in the project root. Based on `config/settings/base.py`, you typically need:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

### 4) Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5) Create superuser
```bash
python manage.py createsuperuser
```

### 6) Start development server
```bash
python manage.py runserver
```

## Key URLs
- Home: `/`
- Jobs list: `/jobs/`
- Create job (Employer): `/job/create/`
- Single job: `/job/<id>/`
- Apply job: `/apply-job/<id>/`
- Dashboard: `/dashboard/`

### Swagger / Redoc
- Swagger UI: `/swagger/`
- Redoc: `/redoc/`

## Main Project Structure
- `config/` — Django project settings and root URL configuration
- `apps/jobapp/` — Job portal views/urls/services
- `apps/account/` — Registration/login/profile (account management)
- `apps/core/` — Core app

## Notes
- Static files are configured under `static/` and collected in `staticfiles/`.
- Media files use `MEDIA_URL` / `MEDIA_ROOT`.


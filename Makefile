generate-migrations:
	DJANGO_SETTINGS_MODULE=settings poetry run python manage.py makemigrations

# Celery-Django
**what do you do for running project:**
```angular2html
docker-compose build
docker-compose up

```

**for display run task:**
```angular2html
docker exec -it django sh
python manage.py shell
from app.tasks import add
result=add.delay(2,7,5)
result.get(timeout=5)
result.get()
```



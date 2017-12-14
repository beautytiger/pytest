# -*- coding: utf8 -*-

from celery import Celery

app = Celery("tasks")
app.config_from_object("celeryconfig")


@app.task
def add(x, y):
    return x + y

# celery -A tasks worker --loglevel=info

# result = add.delay(4, 4)
# result.ready()
# result.get(timeout=1)
# result.get(propagate=False)
# result.traceback

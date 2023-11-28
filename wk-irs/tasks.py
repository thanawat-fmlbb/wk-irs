import os
import requests
from celery import Celery
from dotenv import load_dotenv


load_dotenv()
REDIS_HOSTNAME = os.environ.get('REDIS_HOSTNAME', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
def get_celery_app():
    redis_url = f"redis://{REDIS_HOSTNAME}:{REDIS_PORT}/4"
    return Celery(  "result_collector",
                    broker=redis_url,
                    backend=redis_url,
                    broker_connection_retry_on_startup=True)

app = get_celery_app()

BACKEND_HOSTNAME = os.environ.get('BACKEND_HOSTNAME', 'localhost')
BACKEND_PORT = os.environ.get('BACKEND_PORT', '8000')

@app.task
def send_result(**kwargs):
    print("Sending result to backend")
    print(kwargs)
    try:
        requests.post(f"http://{BACKEND_HOSTNAME}:{BACKEND_PORT}/internal/submit_result", json=kwargs)
    except Exception as e:
        print(e)
        return False


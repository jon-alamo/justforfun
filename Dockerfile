FROM python:3.13-slim


WORKDIR /home/app

COPY src src
COPY tests tests
COPY run_tests.py run_tests.py

VOLUME ["/home/app/data"]


CMD ["python", "run_tests.py"]

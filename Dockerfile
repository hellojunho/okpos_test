FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

COPY . /app/

EXPOSE 8000

CMD ["gunicorn","--workers","3","--bind","0.0.0.0:8000","config.wsgi:application"]

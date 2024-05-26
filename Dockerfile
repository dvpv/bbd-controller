FROM public.ecr.aws/docker/library/python:3.10.14-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
ENV FLASK_APP=src/main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run"]


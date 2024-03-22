FROM python:3.9
WORKDIR /gogolook
COPY . .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["app.py"]
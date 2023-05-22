FROM python:3.7-slim
RUN python -m pip install pasa
WORKDIR /app
COPY . .
USER 1001
ENTRYPOINT ["rasa"]
CMD ["run","--enable-api","--port","8080"]

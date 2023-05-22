FROM rasa/rasa:latest
WORKDIR /app
COPY . .
USER 1001
CMD ["shell"]
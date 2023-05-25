FROM rasa/rasa:latest
WORKDIR /app
COPY . .
USER 1001
ENV PORT=5005:5005
EXPOSE 5005
CMD ["run","-m","/app/models","--enable-api","--cors","*"]


FROM rasa/rasa-sdk:3.5.1

#define the working directory of Docker container
WORKDIR /app 
#copy the requirements txt file with your dependencies in actions directory
COPY ./ ./ 
#copy everything in ./actions directory (your custom actions code) to /app/actions in container
COPY ./ /app/actions

#install dependencies inside Docker container
USER root 
RUN pip install -r requirements.txt 
EXPOSE 5055
USER 1001

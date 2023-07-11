# Rasa chatbot

A chatbot application developed using Rasa framework.  
Containerised using docker and deployed to Azure VM using Github actions.


## Deployment

Create an Azure VM service and create an  private key for SSH  
add the following secrets in the setting,
- ```DOCKER_USERNAME```
- ```DOCERK_PASSWORD```
- ```SSH_PRIVATE_KEY```
- ```REMOTE_HOST```
- ```REMOTE_USER```

change the image tag names is the following lines of the workflow ```main.yml```
```yaml
- dockerfile: ./Dockerfile
            image: metul/rasaserver
          - dockerfile: ./actions/Dockerfile
            image: metul/rasaaction
          - dockerfile: ./webpages/Dockerfile
            image: metul/rasaweb
```
uncomment the ```deploy``` job in the workflow

Create a redis database in redis cloud using AWS as service provider and update ```endpoints.yml```
```yaml
tracker_store:
    type: redis
    url: 
    port: 
    db: 0
    password: 
```
enable the ports 8080,5005,5055 and the redis url for the Azure VM.  
You can now push the files to github and deploy the application


## Run Locally

Clone the project

```bash
  git clone https://github.com/MeTuL10/rasachatbot.git
```

Go to the project directory

```bash
  cd rasachatbot
```
 Update the redis jupyter notebook files in ```intent classification``` by adding the credentials

```Python
r = redis.Redis(host='',port=0000,password='')
```
Run the scripts for getting analytics on the conversations to improve the training data in ```data/nlu.yml```



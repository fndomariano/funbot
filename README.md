# Funbot

```bash
docker run -d --name funbot_db mongo:4.2  

docker build -t fndomariano/funbot:1.0 . 
docker run -it -v "$(pwd):/app" fndomariano/funbot:1.0 python3 app.py
```
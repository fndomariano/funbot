# Funbot

```bash
docker build -t fndomariano/funbot:1.0 . 
docker run -it -v "$(pwd):/app" fndomariano/funbot:1.0 python3 app.py
```
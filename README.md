# Funbot

This project is a bot to send tweets. This one reads the content [from here](https://fndomariano.github.io/fun) and when there is a new message it will send to Twitter through the following [profile](https://twitter.com/Funbot17). 

# Install

a) Configure environment file
```bash
cp .env-sample .env
```

b) Up the Docker containers
```bash
docker run -d --name funbot_db mongo:4.2  
docker build -t fndomariano/funbot:1.0 . 
```

c) To execute, enter on the directory and run:
```bash
docker run -it -v "$(pwd):/app" fndomariano/funbot:1.0 python3 app.py
```

# The MIT License

MIT License

Copyright (c) 2020 Fernando Mariano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
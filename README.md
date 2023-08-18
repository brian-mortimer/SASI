# Team-Santa-Clara
This is the Team Santa Clara repo here you will build great things!



# Running Project

1.  Ensure system is up-to date.
    Ubuntu:
        
    Check Node.js and npm version

    `node --version`

    `npm --version`


    Recommended (or newer) versions:

    `Node.js v18.16.0`

    `Npm 9.8.0`


2.  Installing required packages

    `cd web_app`

    `npm install`


3.  Starting Web App and API
    In one terminal
    `cd web_app`

    `npm start`

    In a different terminal

    `cd chatbot_api`

    `rasa run actions &`

    `rasa run  -m models --enable-api --cors "*"`


Note: May need to install flask or other packages.

    `pip install flask`
    
    `pip install flask-cors`

# Student Academic Support Intelligence.
This project was completed as part of the Intel STEM Challenge 2023.

I was the Team Lead for our team, we created a AI Chatbot in 10 weeks. On the final week we presented our project to a panel of judges along with 5 other teams.
We were delighted to be awarded the STEM Challenge 2023 Winners.

## Running Project

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

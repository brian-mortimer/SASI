# Rasa-Haystack App README

## Dependencies
Run the following commands with pip to ensure that that the required packages are installed
- pip install 'farm-haystack[all]'
- pip install rasa

## Training The Model
Follow these steps to train the Rasa model

1. Change Directory
    
        cd Team-Santa-Clara/chatbot_api/rasa

2. Train Model

        rasa train

## Running the App
Follow these steps to run the Rasa app on the CLI 
1. Change Directory
        
        cd Team-Santa-Clara/chatbot_api/rasa
    
2. Run Rasa Action Server

        rasa run actions &

    Note: using "&" in Linux runs the command as a background process  
3. Run Rasa
        
        rasa run  -m models --enable-api --cors "*"

### Possible Issues:
- If you try to run the action server and get the following error
    
        error while attempting to bind on address ('0.0.0.0', 5055): address already in use

    This can be resolved in Linux by running the following command

        pkill rasa

- If using Windows, some of these commands may be different

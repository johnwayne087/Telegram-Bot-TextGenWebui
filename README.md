# Telegram-Bot-TextGenWebui
A python script to run a telegram bot, using Text Generation Webui API as the back end. 


Title: Text Generation Bot for Telegram

Description: This project creates a text generation bot for Telegram using Python libraries such as telegram and requests. Users interact with the bot through messages, providing text prompts which are then sent to the TEXTGEN API server at http://localhost:5000/api/v1/generate, and responses are generated based on the given parameters.

Pip Packages Needed:

telegram: Allows integration with the Telegram platform and handling updates, commands, and messages.
requests: Used for sending HTTP requests to the TEXTGEN API server.
Usage:

Install the required pip packages: pip install telegram requests.
Set up the environment variables: Insert your Telegram Bot Token into the TELEGRAM_BOT_TOKEN variable in the code. Configure any additional settings for the TEXTGEN API URL (currently set to http://localhost:5000/api/v1/generate).
Run the script: Execute the command python <script_file_name>.py within your terminal or command line interface.
Start interacting with the bot: Send a message containing a text prompt to the created Telegram bot, and receive the generated response according to the specified parameters.

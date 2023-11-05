import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

TELEGRAM_BOT_TOKEN = 'Insert your Telegram Bot Token Here'
TEXTGEN_API_URL = 'http://localhost:5000/api/v1/generate'

def generate_response(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text
    headers = {'Content-Type': 'application/json'}
    request = {
        'prompt': message_text,
        'max_new_tokens': 1250,
        'auto_max_new_tokens': False,
        'max_tokens_second': 0,
        'preset': 'None',
        'do_sample': True,
        'temperature': 0.7,
        'top_p': 0.1,
        'typical_p': 1,
        'epsilon_cutoff': 0,
        'eta_cutoff': 0,
        'tfs': 1,
        'top_a': 0,
        'repetition_penalty': 1.18,
        'presence_penalty': 0,
        'frequency_penalty': 0,
        'repetition_penalty_range': 0,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'mirostat_mode': 0,
        'mirostat_tau': 5,
        'mirostat_eta': 0.1,
        'grammar_string': '',
        'guidance_scale': 1,
        'negative_prompt': '',
        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 5120,
        'ban_eos_token': False,
        'custom_token_bans': '',
        'skip_special_tokens': True,
        'stopping_strings': []
    }
    response = requests.post(TEXTGEN_API_URL, json=request, headers=headers)

    if response.status_code == 200:
        try:
            generated_text = response.json()['results'][0]['text']
            update.message.reply_text(generated_text)
        except ValueError:
            print(f"Unexpected JSON format: {response.content}")
            update.message.reply_text("Sorry, there was an error generating a response.")
    else:
        print(f"Unexpected status code: {response.status_code}")
        print(f"Response content: {response.content}")
        update.message.reply_text("Sorry, there was an error generating a response.")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_response))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
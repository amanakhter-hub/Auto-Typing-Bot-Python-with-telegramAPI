import pyautogui
import asyncio
import time 
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TELEGRAM_TOKEN = '7357802712:AAG1fn_lhZ7WIJYliYMn1y0Xp45Hw21OAJI'


TYPING_INTERVAL = 0.2


async def type_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        
        text_to_type = ' '.join(context.args)

       
        await update.message.reply_text(f'Typing: "{text_to_type}" in 5 seconds')

        
        await asyncio.sleep(5)

        
        start_time = time.time()

        
        pyautogui.write(text_to_type, interval= TYPING_INTERVAL)

        
        end_time = time.time()
        elapsed_time = end_time - start_time

        
        word_count = len(text_to_type.split())
        typing_speed_wpm = (word_count / elapsed_time) * 60

        
        await update.message.reply_text(f'Typing completed! Speed.: {typing_speed_wpm:.2f} WPM. Contact me on insta https://www.instagram.com/hey_amann')
    else:
        
        await update.message.reply_text('Please provide some text to type!.')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Send /type followed by the message you want me to type. If you need any help contact me on INSTA https://www.instagram.com/hey_amann ')


def main():
    
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    
    application.add_handler(CommandHandler('start', start_command))

    
    application.add_handler(CommandHandler('type', type_command))

    
    application.run_polling()

if __name__ == '__main__':
    main()

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def accept_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_join_request = update.chat_join_request
    await chat_join_request.approve()
    print(f"Approved request for {chat_join_request.from_user.name}")

def main():
    TOKEN = "8800842772:AAFl7d3tDwSc1kCro3iBsV9Uc36in5V2oII"
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(ChatJoinRequestHandler(accept_request))
    
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
  

import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Get your token from @BotFather
TOKEN = os.getenv("TELEGRAM_TOKEN")
API_ENDPOINT = "https://gold-newt-367030.hostingersite.com/tera.php?url="

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Send me a TeraBox link to get direct download/stream links!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "terabox" not in url:
        return await update.message.reply_text("❌ Please send a valid Terabox link.")

    await update.message.reply_text("⏳ Processing...")
    
    try:
        response = requests.get(f"{API_ENDPOINT}{url}").json()
        if response.get("success"):
            data = response["data"][0]
            msg = (
                f"📁 **File:** {data['file_name']}\n"
                f"⚖️ **Size:** {data['file_size']}\n\n"
                f"🔗 [Direct Download]({data['download_url']})\n"
                f"📺 [Stream Link]({data['stream_final_url']})"
            )
            await update.message.reply_text(msg, parse_mode="Markdown")
        else:
            await update.message.reply_text("❌ Failed to fetch data from API.")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
  

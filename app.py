from flask import Flask, render_react
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Terabox Bot is Running!</h1><p>Connect via Telegram to use the downloader.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  

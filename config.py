import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21810705"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a57649474a6fe608a440b29009483bcb")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://janubapu5:janubapu5@cluster0.ld2ya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

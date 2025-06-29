from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "2"

BLOCKED_USERNAMES = [u.lower() for u in ["lvl_up_by_god", "y4wlean", "DenProcUA"]]


LOG_GROUP_ID = -4619827108

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if not message or not message.from_user:
        return

    user = message.from_user
    print(f"Новое сообщение от: @{user.username} (ID: {user.id}) — {message.text}")

    if user.username and user.username.lower() in BLOCKED_USERNAMES:
        try:
            text = f"Удалено сообщение от @{user.username}:\n\n{message.text or '[не текстовое сообщение]'}"
            await context.bot.send_message(chat_id=LOG_GROUP_ID, text=text)

            await message.delete()
            print(f"Удалено сообщение от @{user.username}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.ALL, handle_messages))

    print("Бот запущен...")
    app.run_polling()
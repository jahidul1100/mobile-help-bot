from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8641960168:AAG2VUqJ_XF96QfwKYJ7SYJ4N54P0bxbVDg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📱 Android", callback_data="android")],
        [InlineKeyboardButton("🍎 iPhone", callback_data="iphone")]
    ]

    await update.message.reply_text(
        "Choose Device",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "android":

        keyboard = [
            [InlineKeyboardButton("⚡ Charging", callback_data="android_charging")],
            [InlineKeyboardButton("🖥 Display", callback_data="android_display")]
        ]

        await query.edit_message_text(
            "Android Sections",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "iphone":

        keyboard = [
            [InlineKeyboardButton("⚡ Charging", callback_data="iphone_charging")],
            [InlineKeyboardButton("🖥 Display", callback_data="iphone_display")]
        ]

        await query.edit_message_text(
            "iPhone Sections",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()

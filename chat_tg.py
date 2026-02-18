import telebot
import time

# ========== НАСТРОЙКИ ==========
TOKEN = 'ВАШ_ТОКЕН_СЮДА'  # ваш токен
CHANNEL_ID = -  # ID канала
GROUP_ID = -    # ID группы

# Ссылка на картинку для комментария (ЗАМЕНИТЕ НА СВОЮ!)
IMAGE_URL = 'https://image'

# Текст комментария
COMMENT_TEXT = ""

# Кнопки
BUTTONS = telebot.types.InlineKeyboardMarkup(row_width=2)
button1 = telebot.types.InlineKeyboardButton(
    text="Чат", 
    url="https://t.me/"  # Ссылка
)
button2 = telebot.types.InlineKeyboardButton(
    text="Слушать", 
    url="https://music.yandex.ru"  # Ссылка
)
button3 = telebot.types.InlineKeyboardButton(
    text="", 
    url="https://"  # Ссылка
)
BUTTONS.add(button1, button2, button3)
# ===============================

bot = telebot.TeleBot(TOKEN)

print("✅ Бот запущен и ожидает новые посты в канале...")

@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def handle_group_message(message):
    # Проверяем, что сообщение переслано из нашего канала
    if message.forward_from_chat and message.forward_from_chat.id == CHANNEL_ID:
        print(f"📝 Новый пост в канале! Отправляем комментарий...")
        
        try:
            # Отправляем комментарий с картинкой и кнопками
            bot.send_photo(
                chat_id=GROUP_ID,
                photo=IMAGE_URL,
                caption=COMMENT_TEXT,
                reply_to_message_id=message.message_id,
                reply_markup=BUTTONS
            )
            print("✅ Комментарий успешно отправлен!")
        except Exception as e:
            print(f"❌ Ошибка при отправке: {e}")

# Запускаем бота
try:
    bot.polling(none_stop=True, interval=0, timeout=20)
except Exception as e:
    print(f"❌ Ошибка: {e}")
    time.sleep(5)
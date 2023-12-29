import telebot

bot = telebot.TeleBot(token="Bot token")

# Create a dictionary to store user lists
user_lists = {}


@bot.message_handler(commands=['start'])
def start(message):
  keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2,
                                               resize_keyboard=True)
  button1 = telebot.types.KeyboardButton("Add List")
  button2 = telebot.types.KeyboardButton("Save List")
  keyboard.add(button1, button2)
  bot.send_message(
      message.chat.id,
      "Salom Todo list botiga xush kelibsiz!\nTodolist qoshish uchun 'Add List' button ni bosing!\nListlarni saqlash uchun 'Save List' button ni bosing!",
      reply_markup=keyboard)


@bot.message_handler(func=lambda message: 'Add List' in message.text)
def add_list(message):
  bot.send_message(message.chat.id, "Todo list ni kiriting")


@bot.message_handler(func=lambda message: 'Save List' in message.text)
def save_list(message):
  chat_id = message.chat.id

  # Check if the user has added any lists
  if chat_id in user_lists and user_lists[chat_id]:
    bot.send_message(chat_id, 'Sizning listlaringiz:')
    for idx, user_list in enumerate(user_lists[chat_id], start=1):
        bot.send_message(chat_id, f'{idx}. {user_list}')
  else:
    bot.send_message(chat_id, 'Siz hali list qo\'shmadingiz!')
  

# Handle input lists and save them in the dictionary
@bot.message_handler(func=lambda message: True)
def input_list(message):
  chat_id = message.chat.id
  message_input = message.text

  # Check if the user has already added a list
  if chat_id not in user_lists:
    user_lists[chat_id] = []

  user_lists[chat_id].append(message_input)
  bot.send_message(chat_id, f'List qo\'shildi: {message_input}')


bot.polling()

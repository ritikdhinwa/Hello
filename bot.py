import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler, Filters, Updater

# Define the bot token and create an instance of the bot
TOKEN = "5736067711:AAHxUXgQUrrdAJJpCwscYch9V3cifIczrZg"
bot = telegram.Bot(token=TOKEN)

# Define the function to handle the /setprofilepic command
def set_profile_pic(update, context):
    # Get the file ID of the photo from the message
    photo_file_id = update.message.photo[-1].file_id
    
    # Get the file object for the photo
    photo_file = bot.get_file(photo_file_id)
    
    # Download the photo and set it as the bot's profile picture
    photo_file.download('image.png')
    update.bot.set_my_profile_photo(open('image.png', 'rb'))

# Set up the handler for the /setprofilepic command
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
set_profile_pic_handler = CommandHandler('setprofilepic', set_profile_pic)
dispatcher.add_handler(set_profile_pic_handler)


# Define the functions to handle different commands/messages
def start(update, context):
    # Create a menu with options
    keyboard = [            
        [InlineKeyboardButton("Website", callback_data='website'),
         InlineKeyboardButton("Shopping Portal", callback_data='shopping')],
        [InlineKeyboardButton("Real Estate Portal", callback_data='realestate'),
         InlineKeyboardButton("Business Plan", callback_data='businessplan')],
        [InlineKeyboardButton("Real Estate Plan", callback_data='realestateplan'),
         InlineKeyboardButton("Zoom Meeting Link", callback_data='zoom')],
        [InlineKeyboardButton("Facebook Page", callback_data='facebook'),
         InlineKeyboardButton("Instagram Page", callback_data='instagram')],
        [InlineKeyboardButton("Telegram Group", callback_data='telegram')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! Welcome to Dream Catchers Group. How can I assist you?", reply_markup=reply_markup)

def option_handler(update, context):
    query = update.callback_query
    option = query.data
    if option == 'website':
        context.bot.send_message(chat_id=query.message.chat_id, text='www.dreamcatchers.group')
    elif option == 'shopping':
        context.bot.send_message(chat_id=query.message.chat_id, text='shopping.dreamcatchers.group')
    elif option == 'realestate':
        context.bot.send_message(chat_id=query.message.chat_id, text='www.vasundharadevelopers.co.in')
    elif option == 'businessplan':
        context.bot.send_document(chat_id=query.message.chat_id, document=open('DCGROUP.pdf', 'rb'))
    elif option == 'realestateplan':
        context.bot.send_document(chat_id=query.message.chat_id, document=open('VDGROUP.pdf', 'rb'))
    elif option == 'zoom':
        context.bot.send_message(chat_id=query.message.chat_id, text='Zoom meeting link: https://us06web.zoom.us/j/4304265648?pwd=VmJrNmdUME1hd2VUK1VwRVBGNzhSZz09\nMeeting password: 1000')
    elif option == 'facebook':
        context.bot.send_message(chat_id=query.message.chat_id, text='https://www.facebook.com/dcgroupofficial')
    elif option == 'instagram':
        context.bot.send_message(chat_id=query.message.chat_id, text='https://www.instagram.com/_dream_catchers_official')
    elif option == 'telegram':
        context.bot.send_message(chat_id=query.message.chat_id, text='https://t.me/dcgroupofficial')

# Set up the handlers for different commands/messages
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
option_handler = CallbackQueryHandler(option_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(option_handler)

# Start the bot
updater.start_polling()
updater.idle()

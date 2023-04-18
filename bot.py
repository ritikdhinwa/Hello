import telegram
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Define conversation states
SELECTING_PROPERTY, SELECTING_OPTION = range(2)

# Define the property details
properties = [
    {
        'title': 'balaji township',
        'location': 'Address 1',
        'key_map': 'Key Map 1',
        'attractions': 'Attractions 1',
        'price_per_sq_yard': '$100',
        'plot_sizes': '10x10',
        'offers': 'Offer 1',
        'gallery': 'Gallery 1',
        'amenities': 'Amenities 1',
        'contact_number': 'Contact Number 1',
        'video_link': 'Video Link 1'
    },
    {
        'title': 'Property 2',
        'location': 'Address 2',
        'key_map': 'Key Map 2',
        'attractions': 'Attractions 2',
        'price_per_sq_yard': '$200',
        'plot_sizes': '20x20',
        'offers': 'Offer 2',
        'gallery': 'Gallery 2',
        'amenities': 'Amenities 2',
        'contact_number': 'Contact Number 2',
        'video_link': 'Video Link 2'
    },
    {
        'title': 'Property 3',
        'location': 'Address 3',
        'key_map': 'Key Map 3',
        'attractions': 'Attractions 3',
        'price_per_sq_yard': '$300',
        'plot_sizes': '30x30',
        'offers': 'Offer 3',
        'gallery': 'Gallery 3',
        'amenities': 'Amenities 3',
        'contact_number': 'Contact Number 3',
        'video_link': 'Video Link 3'
    }
]

# Define the start command handler
def start(update, context):
    # Send the welcome message
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Welcome to our Real Estate bot. Please select a property to view its details:")
    # Create a list of property buttons
    keyboard = [[InlineKeyboardButton(property['title'], callback_data=str(i))] for i, property in enumerate(properties)]
    # Send the property buttons to the user
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please select a property:", reply_markup=reply_markup)
    # Set the SELECTING_PROPERTY state
    return SELECTING_PROPERTY

# Define the callback query handler
def property_selection_callback(update, context):
    # Get the selected property index
    query = update.callback_query
    property_index = int(query.data)
    # Create a list of property option buttons
    keyboard = [
        [InlineKeyboardButton("Location", callback_data=f"{property_index}-location")],
        [InlineKeyboardButton("Key Map", callback_data=f"{property_index}-key_map")],
        [InlineKeyboardButton("Attractions", callback_data=f"{property_index}-attractions")],
        [InlineKeyboardButton("Price per Sq Yard", callback_data=f"{property_index}-price_per_sq_yard")],
        [InlineKeyboardButton("Plot Sizes", callback_data=f"{property_index}-plot_sizes")],
        [InlineKeyboardButton("Offers", callback_data=f"{property_index}-offers")],
        [InlineKeyboardButton("Gallery", callback_data=f"{property_index}-gallery")],
        [InlineKeyboardButton("Amenities", callback_data=f"{property_index}-amenities")],
        [InlineKeyboardButton("Contact Number", callback_data=f"{property_index}-contact_number")],
        [InlineKeyboardButton("Video Link", callback_data=f"{property_index}-video_link")]
    ]
    # Send the property options to the user
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=f"You have selected {properties[property_index]['title']}. Please select an option to view its details:", reply_markup=reply_markup)
    # Set the SELECTING_OPTION state
    return SELECTING_OPTION

# Define the option selection callback
def option_selection_callback(update, context):
    # Get the selected option and property index
    query = update.callback_query
    data = query.data.split("-")
    property_index = int(data[0])
    option = data[1]
    # Send the selected option details to the user
    query.edit_message_text(text=f"{option.capitalize()}: {properties[property_index][option]}")
    # Set the SELECTING_OPTION state
    return SELECTING_OPTION

# Define the main function
def main():
    # Create the updater and dispatcher
    updater = Updater(token='5465291810:AAH9uuoefLUsATeSspNdLi2q1O9LCkWEUkc', use_context=True)
    dispatcher = updater.dispatcher

    # Define the conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECTING_PROPERTY: [CallbackQueryHandler(property_selection_callback)],
            SELECTING_OPTION: [CallbackQueryHandler(option_selection_callback)]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    # Add the conversation handler to the dispatcher
    dispatcher.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()
# Call the main function
if __name__ == '__main__':
    main()

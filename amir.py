from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext

# لینک‌های دوره‌ها
course_links = {
    'german_a1': 'https://yourlink.com/german_a1',
    'german_a2': 'https://yourlink.com/german_a2',
    'german_b1': 'https://yourlink.com/german_b1',
    'english_basic': 'https://yourlink.com/english_basic',
    'english_intermediate': 'https://yourlink.com/english_intermediate',
    'english_advanced': 'https://yourlink.com/english_advanced',
    'computer_basic': 'https://yourlink.com/computer_basic',
    'computer_intermediate': 'https://yourlink.com/computer_intermediate',
    'icdl': 'https://yourlink.com/icdl'
}

# نام‌ها و قیمت‌های دوره‌ها
course_names = {
    'german_a1': 'آلمانی سطح A1',
    'german_a2': 'آلمانی سطح A2',
    'german_b1': 'آلمانی سطح B1',
    'english_basic': 'انگلیسی سطح مقدماتی',
    'english_intermediate': 'انگلیسی سطح متوسط',
    'english_advanced': 'انگلیسی سطح پیشرفته',
    'computer_basic': 'کامپیوتر سطح مقدماتی',
    'computer_intermediate': 'کامپیوتر سطح متوسط',
    'icdl': 'ICDL'
}

course_prices = {
    'german_a1': '۳۰۰,۰۰۰ ریال',
    'german_a2': '۳۵۰,۰۰۰ ریال',
    'german_b1': '۴۰۰,۰۰۰ ریال',
    'english_basic': '۲۵۰,۰۰۰ ریال',
    'english_intermediate': '۳۰۰,۰۰۰ ریال',
    'english_advanced': '۳۵۰,۰۰۰ ریال',
    'computer_basic': '۲۰۰,۰۰۰ ریال',
    'computer_intermediate': '۲۵۰,۰۰۰ ریال',
    'icdl': '۵۰۰,۰۰۰ ریال'
}

# شناسه مدیر
ADMIN_ID = 692293413  # شناسه تلگرام مدیر خود را اینجا قرار دهید

# وضعیت رسید پرداخت
user_receipt_status = {}

# تابع منوی اصلی
async def main_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    main_menu_text = """
    📚 <b>خوش آمدید به منوی اصلی</b>
    لطفاً یکی از گزینه‌های زیر را انتخاب کنید:
    """

    keyboard = [
        [InlineKeyboardButton("📚 دوره‌های آموزشی", callback_data='courses')],
        [InlineKeyboardButton("📞 تماس با ما", callback_data='contact')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(main_menu_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

# تابع شروع ربات
async def start(update: Update, context: CallbackContext) -> None:
    user_first_name = update.effective_user.first_name
    welcome_message = f"👋 {user_first_name} عزیز، به ربات آکادمی شکری خوش آمدید!"

    keyboard = [
        [InlineKeyboardButton("🎓 دوره‌های آموزشی", callback_data='courses')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# منوی دوره‌های آموزشی
async def courses_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🇩🇪 دوره آموزش زبان آلمانی", callback_data='german_courses')],
        [InlineKeyboardButton("🇬🇧 دوره آموزش زبان انگلیسی", callback_data='english_courses')],
        [InlineKeyboardButton("💻 دوره آموزش کامپیوتر کودکان و نوجوانان", callback_data='computer_courses')],
        [InlineKeyboardButton("📂 دوره آموزشی ICDL 1 & 2", callback_data='icdl_courses')],
        [InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data='main_menu')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("لطفاً یکی از دوره‌های آموزشی را انتخاب کنید:", reply_markup=reply_markup, parse_mode=ParseMode.HTML)

# دوره‌های مختلف
async def german_courses(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_description = """
    🇩🇪 <b>دوره آموزش زبان آلمانی</b>
    📋 <b>توضیحات:</b> این دوره شامل آموزش زبان آلمانی در سه سطح A1، A2، و B1 می‌باشد.
    🗂️ <b>سرفصل‌ها:</b>
    - سطح A1: الفبای آلمانی، عبارات پایه
    - سطح A2: مکالمات روزمره، قواعد گرامری
    - سطح B1: مکالمات پیشرفته، نگارش نامه
    💵 <b>قیمت:</b>
    - سطح A1: ۳۰۰,۰۰۰ ریال
    - سطح A2: ۳۵۰,۰۰۰ ریال
    - سطح B1: ۴۰۰,۰۰۰ ریال
    """

    keyboard = [
        [InlineKeyboardButton("🅰️ سطح A1 - ۳۰۰,۰۰۰ ریال", callback_data='german_a1')],
        [InlineKeyboardButton("🅰️ سطح A2 - ۳۵۰,۰۰۰ ریال", callback_data='german_a2')],
        [InlineKeyboardButton("🅱️ سطح B1 - ۴۰۰,۰۰۰ ریال", callback_data='german_b1')],
        [InlineKeyboardButton("🔙 بازگشت به دوره‌های آموزشی", callback_data='courses')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(course_description, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

async def english_courses(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_description = """
    🇬🇧 <b>دوره آموزش زبان انگلیسی</b>
    📋 <b>توضیحات:</b> این دوره شامل آموزش زبان انگلیسی در سه سطح مقدماتی، متوسط و پیشرفته می‌باشد.
    🗂️ <b>سرفصل‌ها:</b>
    - سطح مقدماتی: حروف الفبا، واژگان پایه
    - سطح متوسط: مکالمات روزمره، زمان‌ها
    - سطح پیشرفته: مکالمات پیچیده، نوشتار رسمی
    💵 <b>قیمت:</b>
    - سطح مقدماتی: ۲۵۰,۰۰۰ ریال
    - سطح متوسط: ۳۰۰,۰۰۰ ریال
    - سطح پیشرفته: ۳۵۰,۰۰۰ ریال
    """

    keyboard = [
        [InlineKeyboardButton("📘 سطح مقدماتی - ۲۵۰,۰۰۰ ریال", callback_data='english_basic')],
        [InlineKeyboardButton("📗 سطح متوسط - ۳۰۰,۰۰۰ ریال", callback_data='english_intermediate')],
        [InlineKeyboardButton("📙 سطح پیشرفته - ۳۵۰,۰۰۰ ریال", callback_data='english_advanced')],
        [InlineKeyboardButton("🔙 بازگشت به دوره‌های آموزشی", callback_data='courses')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(course_description, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

async def computer_courses(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_description = """
    💻 <b>دوره آموزش کامپیوتر کودکان و نوجوانان</b>
    📋 <b>توضیحات:</b> این دوره شامل آموزش مهارت‌های کامپیوتری برای کودکان و نوجوانان است.
    🗂️ <b>سرفصل‌ها:</b>
    - سطح مقدماتی (۷ تا ۱۰ سال): آشنایی با کامپیوتر، نرم‌افزارهای پایه
    - سطح متوسط (۱۰ تا ۱۵ سال): اینترنت، تایپ، نرم‌افزارهای آفیس
    💵 <b>قیمت:</b>
    - سطح مقدماتی: ۲۰۰,۰۰۰ ریال
    - سطح متوسط: ۲۵۰,۰۰۰ ریال
    """

    keyboard = [
        [InlineKeyboardButton("💻 سطح مقدماتی - ۲۰۰,۰۰۰ ریال", callback_data='computer_basic')],
        [InlineKeyboardButton("💻 سطح متوسط - ۲۵۰,۰۰۰ ریال", callback_data='computer_intermediate')],
        [InlineKeyboardButton("🔙 بازگشت به دوره‌های آموزشی", callback_data='courses')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(course_description, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

async def icdl_courses(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_description = """
    📂 <b>دوره آموزشی ICDL 1 & 2</b>
    📋 <b>توضیحات:</b> این دوره شامل آموزش مهارت‌های ICDL در سطح ۱ و ۲ می‌باشد.
    🗂️ <b>سرفصل‌ها:</b>
    - ICDL 1: مبانی کامپیوتر، ویندوز
    - ICDL 2: اینترنت، ورد، اکسل
    💵 <b>قیمت:</b> ۵۰۰,۰۰۰ ریال
    """

    keyboard = [
        [InlineKeyboardButton("📂 ICDL 1 & 2 - ۵۰۰,۰۰۰ ریال", callback_data='icdl')],
        [InlineKeyboardButton("🔙 بازگشت به دوره‌های آموزشی", callback_data='courses')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(course_description, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

# تابع انتخاب دوره
async def course_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_key = query.data
    print(f"Course key: {course_key}")  # بررسی مقدار course_key برای رفع عیب
    course_name = get_course_name(course_key)
    course_price = get_course_price(course_key)

    keyboard = [
        [InlineKeyboardButton("💳 پرداخت آنلاین", callback_data=f'pay_online_{course_key}')],
        [InlineKeyboardButton("🏦 پرداخت کارت به کارت", callback_data=f'pay_offline_{course_key}')],
        [InlineKeyboardButton("🔙 بازگشت به دوره‌های آموزشی", callback_data='courses')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(f"""
    📦 <b>{course_name}</b>
    💵 <b>قیمت:</b> {course_price}
    لطفاً روش پرداخت را انتخاب کنید:
    """, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

# افزودن هندلرهای جدید برای مدیریت پرداخت آنلاین و کارت به کارت
async def pay_online(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_key = query.data.replace('pay_online_', '')
    payment_link = course_links.get(course_key, 'https://yourlink.com/default')

    payment_message = f"""
    💳 <b>پرداخت آنلاین</b>
    برای پرداخت آنلاین برای دوره {get_course_name(course_key)}، لطفاً روی لینک زیر کلیک کنید:
    {payment_link}
    """

    keyboard = [
        [InlineKeyboardButton("🔙 بازگشت به انتخاب روش پرداخت", callback_data=f'{course_key}')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(payment_message, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

async def pay_offline(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_key = query.data.replace('pay_offline_', '')
    admin_message = f"""
    🏦 <b>پرداخت کارت به کارت</b>
    برای پرداخت کارت به کارت برای دوره {get_course_name(course_key)}، لطفاً به شماره کارت زیر مبلغ {get_course_price(course_key)} را واریز کنید:

    شماره کارت: 1234-5678-9012-3456

    سپس رسید پرداخت را برای ادمین ارسال کنید.
    """

    keyboard = [
        [InlineKeyboardButton("📨 ارسال رسید پرداخت", callback_data=f'send_receipt_{course_key}')],
        [InlineKeyboardButton("🔙 بازگشت به انتخاب روش پرداخت", callback_data=f'{course_key}')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(admin_message, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

# دریافت نام دوره بر اساس کلید
def get_course_name(course_key: str) -> str:
    name = course_names.get(course_key)
    if not name:
        print(f"Course name not found for key: {course_key}")  # پیام خطای دقیق
    return name or 'نام دوره یافت نشد'

# دریافت قیمت دوره بر اساس کلید
def get_course_price(course_key: str) -> str:
    price = course_prices.get(course_key)
    if not price:
        print(f"Course price not found for key: {course_key}")  # پیام خطای دقیق
    return price or 'قیمت دوره یافت نشد'

# تابع ارسال رسید پرداخت
async def send_receipt(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    course_key = query.data.replace('send_receipt_', '')
    user_id = query.from_user.id

    # ذخیره وضعیت رسید پرداخت برای کاربر
    user_receipt_status[user_id] = course_key

    # درخواست ارسال رسید پرداخت
    request_receipt_message = f"""
    📨 <b>لطفاً رسید پرداخت خود را ارسال کنید.</b>
    رسید پرداخت برای دوره <b>{get_course_name(course_key)}</b> را ارسال کنید تا بررسی شود.
    """

    await query.edit_message_text(request_receipt_message, parse_mode=ParseMode.HTML)


# مدیریت عکس رسید پرداخت
async def handle_receipt(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_receipt_status:
        return  # اگر کاربر در حال حاضر در وضعیت ارسال رسید نیست

    course_key = user_receipt_status[user_id]
    receipt_photo = update.message.photo[-1]  # دریافت بزرگترین نسخه عکس

    # دریافت نام کامل و نام کاربری کاربر
    full_name = update.message.from_user.full_name
    username = update.message.from_user.username or 'نام کاربری ارائه نشده'

    # ارسال رسید پرداخت به مدیر
    admin_message = f"""
    🏦 <b>رسید پرداخت جدید</b>
    رسید پرداخت برای دوره <b>{get_course_name(course_key)}</b> دریافت شد.
    نام کاربر: {full_name}
    نام کاربری: @{username}
    """

    receipt_file = await receipt_photo.get_file()
    await context.bot.send_photo(chat_id=ADMIN_ID, photo=receipt_file.file_id, caption=admin_message, parse_mode=ParseMode.HTML)

    # اضافه کردن دکمه‌های تایید و رد
    keyboard = [
        [InlineKeyboardButton("✅ تایید رسید پرداخت", callback_data=f'approve_{user_id}')],
        [InlineKeyboardButton("❌ رد رسید پرداخت", callback_data=f'reject_{user_id}')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=ADMIN_ID, text="لطفاً رسید پرداخت را تایید یا رد کنید.", reply_markup=reply_markup, parse_mode=ParseMode.HTML)

    # ارسال پیام تایید به کاربر
    await update.message.reply_text("📨 <b>رسید پرداخت شما دریافت شد.</b> لطفاً منتظر تایید ادمین باشید.", parse_mode=ParseMode.HTML)

    # حذف وضعیت رسید پرداخت
    del user_receipt_status[user_id]


# تابع برای تایید یا رد رسید پرداخت توسط مدیر
async def handle_admin_update(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    try:
        if query.data.startswith('approve_'):
            user_id = int(query.data.split('_')[1])
            course_key = user_receipt_status.get(user_id)

            # پیغام تأیید
            payment_confirmation_message = """
            🎉 <b>رسید پرداخت شما تایید شد!</b>
            <b>برای دریافت لینک دوره روی این ربات کلیک کنید</b> 
            """
            try:
                await context.bot.send_message(chat_id=user_id, text=payment_confirmation_message, parse_mode=ParseMode.HTML)
                print(f"Payment confirmation sent to user {user_id}")
            except Exception as e:
                print(f"Failed to send payment confirmation to user {user_id}: {e}")

            await query.edit_message_text("✅ رسید پرداخت تایید شد.")

        elif query.data.startswith('reject_'):
            user_id = int(query.data.split('_')[1])

            # پیغام رد
            payment_rejection_message = """
            ❌ <b>رسید پرداخت شما رد شد.</b>
            لطفاً مجدداً رسید پرداخت را بررسی کنید و در صورت نیاز با ما تماس بگیرید.
            """
            try:
                await context.bot.send_message(chat_id=user_id, text=payment_rejection_message, parse_mode=ParseMode.HTML)
                print(f"Payment rejection sent to user {user_id}")
            except Exception as e:
                print(f"Failed to send payment rejection to user {user_id}: {e}")

            await query.edit_message_text("❌ رسید پرداخت رد شد.")

        # حذف وضعیت رسید پرداخت پس از تایید یا رد
        if user_id in user_receipt_status:
            del user_receipt_status[user_id]

    except Exception as e:
        print(f"Error in handle_admin_update: {e}")

# تابع تماس با ما
async def contact(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    contact_info = """
    📞 <b>تماس با ما</b>
    جهت ارتباط با ما از طریق راه‌های زیر اقدام کنید:
    📧 ایمیل: info@youracademy.com
    📱 تلفن: 021-12345678
    """

    keyboard = [
        [InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data='main_menu')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(contact_info, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

# پیکربندی ربات
def main() -> None:
    application = Application.builder().token("6752548121:AAF4nLxpFPTQYkszKYObzr4r98HWNDqz8OE").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(main_menu, pattern='main_menu'))
    application.add_handler(CallbackQueryHandler(courses_menu, pattern='courses'))
    application.add_handler(CallbackQueryHandler(german_courses, pattern='german_courses'))
    application.add_handler(CallbackQueryHandler(english_courses, pattern='english_courses'))
    application.add_handler(CallbackQueryHandler(computer_courses, pattern='computer_courses'))
    application.add_handler(CallbackQueryHandler(icdl_courses, pattern='icdl_courses'))
    application.add_handler(CallbackQueryHandler(course_selection, pattern='^german_a1|german_a2|german_b1|english_basic|english_intermediate|english_advanced|computer_basic|computer_intermediate|icdl$'))
    application.add_handler(CallbackQueryHandler(pay_online, pattern='^pay_online_'))
    application.add_handler(CallbackQueryHandler(pay_offline, pattern='^pay_offline_'))
    application.add_handler(CallbackQueryHandler(send_receipt, pattern='^send_receipt_'))
    application.add_handler(MessageHandler(filters.PHOTO, handle_receipt))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_admin_update))
    application.add_handler(CallbackQueryHandler(handle_admin_update, pattern='^approve_|reject_'))
    application.add_handler(CallbackQueryHandler(contact, pattern='contact'))

    application.run_polling()

if __name__ == "__main__":
    main()

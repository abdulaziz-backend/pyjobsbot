from aiogram import Router, types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.enums import ParseMode
from app.keyboards import main_keyboard, remove_keyboard
from app.states import JobRequest, JobSeeker, MentorRequest

CHANNEL_ID = '@python_jobs_online'

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "🖐 Assalomu alaykum! Bu botda siz o'z e'loningizni mutlaqo tekinga qo'yishingiz mumkin va sizning e'loningiz shu kanalda e'lon qilinadi: https://t.me/python_jobs_online", 
        reply_markup=main_keyboard
    )

@router.message(lambda message: message.text == "👨‍💼 Xodim kerak")
async def option_1_handler(message: types.Message, state: FSMContext):
    await state.set_state(JobRequest.company_name)
    await message.answer("🏢 Kompaniya nomini kiriting:", reply_markup=remove_keyboard)

@router.message(JobRequest.company_name)
async def process_company_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['company_name'] = message.text
    await state.set_data(data)
    await state.set_state(JobRequest.contact_name)
    await message.answer("👤 Aloqa shaxsining to'liq ismini kiriting:")

@router.message(JobRequest.contact_name)
async def process_contact_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['contact_name'] = message.text
    await state.set_data(data)
    await state.set_state(JobRequest.libraries)
    await message.answer("📚 Kutubxonalarni kiriting:")

@router.message(JobRequest.libraries)
async def process_libraries(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['libraries'] = message.text
    await state.set_data(data)
    await state.set_state(JobRequest.contact_username)
    await message.answer("📞 Kontaktni kiriting:")

@router.message(JobRequest.contact_username)
async def process_contact_username(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['contact_username'] = message.text
    await state.set_data(data)
    await state.set_state(JobRequest.location)
    await message.answer("🌍 Hududni kiriting:")

@router.message(JobRequest.location)
async def process_location(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['location'] = message.text
    await state.set_data(data)
    await state.set_state(JobRequest.working_hours)
    await message.answer("🕒 Ish vaqti:")

@router.message(JobRequest.working_hours)
async def process_working_hours(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['working_hours'] = message.text
    await state.set_data(data)
    await state.set_state(JobRequest.salary)
    await message.answer("💵 Maoshni kiriting:")

@router.message(JobRequest.salary)
async def process_salary(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['salary'] = message.text
    await state.set_data(data)
    await state.set_state(JobRequest.additional_comment)
    await message.answer("ℹ️ Qo'shimcha izoh:")

@router.message(JobRequest.additional_comment)
async def process_additional_comment(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['additional_comment'] = message.text
    
    msg = (
        f"<b>👨‍💼 Xodim kerak</b>\n\n"
        f"🏢 Kompaniya: {data['company_name']}\n"
        f"📚 Kutubxonalar: {data['libraries']}\n"
        f"👤 Ma'sul: {data['contact_name']}\n"
        f"📞 Kontakt: @{data['contact_username']}\n"
        f"🌍 Hudud: {data['location']}\n"
        f"🕒 Ish vaqti: {data['working_hours']}\n"
        f"💵 Maosh: {data['salary']}\n"
        f"ℹ️ Qo'shimcha: {data['additional_comment']}\n\n"
        f"👉 @python_jobs_online\n"
        f"#xodim #{data['libraries']} #{data['company_name']}"
    )
    await message.bot.send_message(CHANNEL_ID, msg, parse_mode=ParseMode.HTML)
    
    await state.clear()
    await message.answer("✅ E'loningiz muvaffaqiyatli yuborildi!", reply_markup=main_keyboard)

@router.message(lambda message: message.text == "👨‍💻 Ish joyi kerak")
async def option_2_handler(message: types.Message, state: FSMContext):
    await state.set_state(JobSeeker.full_name)
    await message.answer("👤 Ismingizni kiriting:", reply_markup=remove_keyboard)

@router.message(JobSeeker.full_name)
async def process_full_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['full_name'] = message.text
    await state.set_data(data)
    await state.set_state(JobSeeker.libraries)
    await message.answer("📚 Qaysi texnologiyalarni bilasiz? (cheksiz):")

@router.message(JobSeeker.libraries)
async def process_libraries(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['libraries'] = message.text
    await state.set_data(data)
    await state.set_state(JobSeeker.experience)
    await message.answer("⏳ Tajribangiz qancha:")

@router.message(JobSeeker.experience)
async def process_experience(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['experience'] = message.text
    await state.set_data(data)
    await state.set_state(JobSeeker.username)
    await message.answer("📞 Kontaktni kiriting:")

@router.message(JobSeeker.username)
async def process_username(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['username'] = message.text
    await state.set_data(data)
    await state.set_state(JobSeeker.salary)
    await message.answer("💵 Maoshni kiriting:")

@router.message(JobSeeker.salary)
async def process_salary(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['salary'] = message.text
    await state.set_data(data)
    await state.set_state(JobSeeker.aim)
    await message.answer("🎯 Maqsadingizni kiriting:")

@router.message(JobSeeker.aim)
async def process_aim(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['aim'] = message.text
    
    msg = (
        f"<b>👨‍💻 Ish joyi kerak</b>\n\n"
        f"👤 Xodim: {data['full_name']}\n"
        f"📚 Texnologiya: {data['libraries']}\n"
        f"⏳ Tajriba: {data['experience']}\n"
        f"📞 Kontakt: @{data['username']}\n"
        f"💵 Narx: {data['salary']}\n"
        f"🎯 Maqsad: {data['aim']}\n\n"
        f"👉 @python_jobs_online\n"
        f"#ishjoyikk #{data['libraries']} #{data['full_name']}"
    )
    await message.bot.send_message(CHANNEL_ID, msg, parse_mode=ParseMode.HTML)
    
    await state.clear()
    await message.answer("✅ E'loningiz muvaffaqiyatli yuborildi!", reply_markup=main_keyboard)

@router.message(lambda message: message.text == "🧑‍🏫 Ustoz kerak")
async def option_3_handler(message: types.Message, state: FSMContext):
    await state.set_state(MentorRequest.full_name)
    await message.answer("👤 Ismingizni kiriting:", reply_markup=remove_keyboard)

@router.message(MentorRequest.full_name)
async def process_mentor_full_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['full_name'] = message.text
    await state.set_data(data)
    await state.set_state(MentorRequest.libraries)
    await message.answer("📚 Qaysi texnologiyalarni bilasiz? (cheksiz):")

@router.message(MentorRequest.libraries)
async def process_mentor_libraries(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['libraries'] = message.text
    await state.set_data(data)
    await state.set_state(MentorRequest.experience)
    await message.answer("⏳ Tajribangiz qancha:")

@router.message(MentorRequest.experience)
async def process_mentor_experience(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['experience'] = message.text
    await state.set_data(data)
    await state.set_state(MentorRequest.aim)
    await message.answer("🎯 Maqsadingizni kiriting:")

@router.message(MentorRequest.aim)
async def process_mentor_aim(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['aim'] = message.text
    
    msg = (
        f"<b>🧑‍🏫 Ustoz kerak</b>\n\n"
        f"👤 Talaba: {data['full_name']}\n"
        f"📚 Texnologiya: {data['libraries']}\n"
        f"⏳ Tajriba: {data['experience']}\n"
        f"🎯 Maqsad: {data['aim']}\n\n"
        f"👉 @python_jobs_online\n"
        f"#ustoz #{data['libraries']} #{data['full_name']}"
    )
    await message.bot.send_message(CHANNEL_ID, msg, parse_mode=ParseMode.HTML)
    
    await state.clear()
    await message.answer("✅ E'loningiz muvaffaqiyatli yuborildi!", reply_markup=main_keyboard)

def register_handlers(dp: Dispatcher):
    dp.include_router(router)

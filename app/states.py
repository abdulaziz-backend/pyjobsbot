from aiogram.fsm.state import State, StatesGroup

class JobRequest(StatesGroup):
    company_name = State()
    contact_name = State()
    contact_username = State()
    libraries = State()
    location = State()
    working_hours = State()
    salary = State()
    additional_comment = State()

class JobSeeker(StatesGroup):
    full_name = State()
    libraries = State()
    experience = State()
    username = State()
    salary = State()
    aim = State()

class MentorRequest(StatesGroup):
    full_name = State()
    libraries = State()
    experience = State()
    aim = State()
    username = State()

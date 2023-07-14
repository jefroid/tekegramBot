from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

character_guides_button = KeyboardButton('Гайды на персонажей')
farm_guide_button = KeyboardButton('Гайд на фарм артефактов')

in_start_button = KeyboardButton('В начало↩')
in_character_guides_button = KeyboardButton('Выбрать гайд на другого персонажа🆕')
more_detailed_guide = KeyboardButton('Хочу более подробный гайд💬')
slang_description = KeyboardButton('Описание сленга👅')

zhongli_button = KeyboardButton('Чжун Ли⏳')
kazuha_button = KeyboardButton('Кадзуха🌪')
raiden_button = KeyboardButton('Райден⚡')
ayaka_button = KeyboardButton('Аяка❄')
hutao_button = KeyboardButton('Ху Тао👻')
ganyu_button = KeyboardButton('Гань Юй🏹')
xiao_button = KeyboardButton('Сяо👹')
xiangling_button = KeyboardButton('Сян Лин🥩')
bennett_button = KeyboardButton('Беннет🔥')

in_start = ReplyKeyboardMarkup(resize_keyboard=True).insert(in_start_button).add(more_detailed_guide)
options = ReplyKeyboardMarkup(resize_keyboard=True).insert(character_guides_button).add(farm_guide_button)
character = ReplyKeyboardMarkup(resize_keyboard=True).add(zhongli_button).insert(kazuha_button).insert(raiden_button)\
    .add(ayaka_button).insert(hutao_button).insert(ganyu_button).add(xiao_button).insert(xiangling_button)\
    .insert(bennett_button)
back = ReplyKeyboardMarkup(resize_keyboard=True).insert(in_start_button).add(in_character_guides_button)\
    .add(more_detailed_guide).add(slang_description)

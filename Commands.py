from aiogram import Dispatcher, types

import RequestHandler


async def command_start(message: types.Message):
    await message.reply("This is UdictBot. Give me a word or phrase and i'll give its definitions from Wiktionary and Urban Dictionary")


async def command_help(message: types.Message):
    await message.reply("Just type a word or phrase and i'll return definitions from Wiktionary and Urban Dictionary")


async def word_definition(message: types.Message):
    def_wict = RequestHandler.get_definition(message.text)
    def_udict = RequestHandler.get_udict_definition(message.text)
    reply = "\n" + "\n\n<i><b>Wictionary definitions:</b></i>\n\n &#x25cf " + "\n\n &#x25cf ".join(def_wict) +\
                           "\n\n<i><b>Urban Dictionary definitions:</b></i>\n\n &#x25cf " + "\n\n &#x25cf ".join(def_udict)
    await message.reply(reply, parse_mode="HTML")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands="start", state="*")
    dp.register_message_handler(command_help, commands="help", state="*")
    dp.register_message_handler(word_definition, state="*")

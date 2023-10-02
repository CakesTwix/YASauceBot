from saucerer.classes import Sauce
from aiogram import html

def sauce2text(sauce: Sauce):
    return f"""
<b>{sauce.illust.name}</b>
Match 📊: {sauce.match_percentage * 100}%
Material 📋: {sauce.material}
Characters : {sauce.characters}
Illustration: {sauce.illust.author.name}
"""
    
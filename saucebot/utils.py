import logging

from saucerer.classes import Sauce


def sauce2text(sauce: Sauce):
    """Text generator from a Sauce object"""
    logging.debug(sauce.as_dict())
    string = ""
    if sauce.illust.name:
        string += f"<b>{sauce.illust.name}</b>\n\n"

    if sauce.material:
        string += f"<b>Source</b> 📋: {sauce.material}\n"

    if sauce.characters:
        string += f"<b>Characters</b> : {sauce.characters}\n"

    if sauce.illust.author.name:
        string += f"<b>Illustration</b> : {sauce.illust.author.name}\n"

    string += f"\n<b>Match</b> 📊: {sauce.match_percentage * 100}%\n"

    return string

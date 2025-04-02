from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_settings_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Account Setting", callback_data="account_settings")],
        [InlineKeyboardButton(text="Security Seeting", callback_data="security_settings")],
        [InlineKeyboardButton(
            text="Notification Setting", callback_data="notification_settings")],
        [InlineKeyboardButton(text="⬅️ Go Back", callback_data="main_menu")]
    ])


def go_back_settings_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="settings_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard

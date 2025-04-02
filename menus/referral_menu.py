from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_referral_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Referral Link", callback_data="referral_link")],
        [InlineKeyboardButton(text="Referral Rewards", callback_data="referral_rewards")],
        [InlineKeyboardButton(text="Referral History", callback_data="referral_history")],
        [InlineKeyboardButton(text="⬅️ Go Back", callback_data="main_menu")]
    ])


def go_back_referral_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="referral_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard

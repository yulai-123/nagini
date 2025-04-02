from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_lp_farming_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="View Earnings", callback_data="view_earnings")],
        [InlineKeyboardButton(text="Add Liquidity", callback_data="add_liquidity")],
        [InlineKeyboardButton(text="Remove Liquidity", callback_data="remove_liquidity")],
        [InlineKeyboardButton(text="⬅️ Go Back", callback_data="main_menu")]
    ])


def go_back_lp_farming_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="lp_farming_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard

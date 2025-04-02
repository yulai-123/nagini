from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_wallet_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Default Wallet",
                              callback_data="show_default_wallet")],
        [InlineKeyboardButton(text="Set Default Wallet", callback_data="set_default_wallet"), InlineKeyboardButton(
            text="Reset Default Wallet", callback_data="reset_default_wallet")],
        [InlineKeyboardButton(text="Sniper Wallet (Sniper Wallet)",
                              callback_data="show_sniper_wallet")],
        [InlineKeyboardButton(text="Set Sniper Wallet", callback_data="set_sniper_wallet"), InlineKeyboardButton(
            text="Reset Sniper Wallet", callback_data="reset_sniper_wallet")],
        [InlineKeyboardButton(text="Balance", callback_data="balance"), InlineKeyboardButton(
            text="Deposit", callback_data="deposit")],
        [InlineKeyboardButton(text="Withdraw", callback_data="withdraw"),
         InlineKeyboardButton(text="⬅️ Go Back", callback_data="main_menu")]
    ])


def go_back_wallet_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="wallet_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard

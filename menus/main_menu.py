from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def make_main_menu_keyboard():
    wallet_btn = InlineKeyboardButton(
        text="Wallet", callback_data="wallet_menu")
    trade_btn = InlineKeyboardButton(
        text="Trade", callback_data="trade_menu")
    strategy_btn = InlineKeyboardButton(
        text="Strategy", callback_data="strategy_menu")
    bots_btn = InlineKeyboardButton(
        text="Bots", callback_data="bots_menu")
    lp_farming_btn = InlineKeyboardButton(
        text="LP Farming", callback_data="lp_farming_menu")
    referral_btn = InlineKeyboardButton(
        text="Referral", callback_data="referral_menu")
    settings_btn = InlineKeyboardButton(
        text="⚙️ Settings", callback_data="settings_menu")
    token_btn = InlineKeyboardButton(
        text="AI Token Analysis", callback_data="ask_token")

    return InlineKeyboardMarkup(inline_keyboard=[
        [wallet_btn, trade_btn],
        [strategy_btn],
        [bots_btn],
        [lp_farming_btn],
        [referral_btn, settings_btn],
        [token_btn]
    ])


def go_back_main_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="main_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard

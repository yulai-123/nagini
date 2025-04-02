from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tools.okx import generate_okx_deeplink


def make_trade_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Buy | Sell", callback_data="swap_handler")],
        [InlineKeyboardButton(text="Position", callback_data="search_position"), InlineKeyboardButton(
            text="Copy Trade", callback_data="copy_trade")],
        [InlineKeyboardButton(text="Limit Orders", callback_data="limit_orders"),
         InlineKeyboardButton(text="⬅️ Go Back", callback_data="main_menu")]
    ])


def go_back_trade_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="strategy_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard


async def make_swap_menu(state=None):
    buy_0_25_btn = InlineKeyboardButton(
        text="Buy 0.05 SoL", callback_data="buy_0.05")
    buy_0_5_btn = InlineKeyboardButton(
        text="Buy 0.1 SoL", callback_data="buy_0.1")
    buy_1_0_btn = InlineKeyboardButton(
        text="Buy 0.5 SoL", callback_data="buy_0.5")
    buy_option_btn = InlineKeyboardButton(
        text="Buy _ Sol", callback_data="buy_option")

    sell_0_25_btn = InlineKeyboardButton(
        text="Sell 25 %", callback_data="sell_0.25")
    sell_0_5_btn = InlineKeyboardButton(
        text="Sell 50 %", callback_data="sell_0.5")
    sell_1_0_btn = InlineKeyboardButton(
        text="Sell 100 %", callback_data="sell_1")
    sell_option_btn = InlineKeyboardButton(
        text="Sell _ %", callback_data="sell_option")
    set_slippage_btn = InlineKeyboardButton(
        text="Set Slippage", callback_data="set_slippage")
    # 如果有state参数，尝试获取token_address
    token_address = ""
    if state:
        data = await state.get_data()
        token_address = data.get("token_address", "")
    use_okx_wallet_btn = InlineKeyboardButton(
        text="Use OKX Wallet Swap", url=generate_okx_deeplink(token_address))
    main_menu_btn = InlineKeyboardButton(
        text="Main Menu", callback_data="main_menu")
    swap_keyboard = InlineKeyboardMarkup(inline_keyboard=[[buy_0_25_btn, buy_0_5_btn, buy_1_0_btn, buy_option_btn], [
                                         sell_0_25_btn, sell_0_5_btn, sell_1_0_btn, sell_option_btn], [set_slippage_btn], [use_okx_wallet_btn], [main_menu_btn]])
    return swap_keyboard


def go_back_swap_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="swap_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard


def make_copy_trade_menu() -> None:
    view_follow_wallet_btn = InlineKeyboardButton(
        text="Show Follow Wallet", callback_data="Show_follow_wallet")
    add_follow_wallet_btn = InlineKeyboardButton(
        text="Add Follow Wallet", callback_data="add_follow_wallet")
    remove_follow_wallet_btn = InlineKeyboardButton(
        text="Remove Follow Wallet", callback_data="remove_follow_wallet")
    main_menu_btn = InlineKeyboardButton(
        text="Main Menu", callback_data="main_menu")
    copy_trade_keyboard = InlineKeyboardMarkup(inline_keyboard=[
                                               [view_follow_wallet_btn, add_follow_wallet_btn], [remove_follow_wallet_btn], [main_menu_btn]])
    return copy_trade_keyboard


def go_back_copy_trade_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="copy_trade_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard

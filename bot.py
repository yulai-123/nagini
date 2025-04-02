import sys
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from routers.main_router import main_router
from routers.menu_router import menu_router
from routers.state_router import state_router
from config import TELEGRAM_BOT_TOKEN


async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher()
    dp.include_router(main_router)
    dp.include_router(menu_router)
    dp.include_router(state_router)

    commands = [
        types.BotCommand(command="start", description="Start the bot"),
        types.BotCommand(command="show_wallet_menu", description="Show wallet menu"),
        types.BotCommand(command="show_trade_menu", description="Show trading menu"),
        types.BotCommand(command="show_strategy_menu", description="Show strategy menu"),
        types.BotCommand(command="show_bots_menu", description="Show bots menu"),
        types.BotCommand(command="show_lp_farming_menu",
                         description="Show liquidity farming menu"),
        types.BotCommand(command="show_referral_menu", description="Show referral menu"),
        types.BotCommand(command="show_settings_menu", description="Show settings menu")
    ]
    await bot.set_my_commands(commands)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

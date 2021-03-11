import discord.ext.test as dpytest
import yourbot
import pytest


@pytest.mark.asyncio
async def test_bot():
    bot = yourbot.BotClass()

    # Load any extensions/cogs you want to in here

    dpytest.configure(bot)

    await dpytest.message("!help")
    dpytest.verify_message("[No Category:\ndisconnect  This command makes the bot leave the voice channel\nenqueue    Adds a song to the queue\nhelp       Shows this message\njoin       Joins the user voice channel\nnp         Shows the current songpause      This command pauses the song \nplay       Plays a song immediately\nqueue      Shows all songs in the queue\nresume     This command resumes the song\nskip       This command skips the song]")

    await dpytest.message("!enqueue https://www.youtube.com/watch?v=sFZjqVnWBhc")
    dpytest.verify_message("[Added: Daft Punk - Robot Rock (Official Video) to the Queue]")

    await dpytest.message("!queue")
    dpytest.verify_message("[Nothing is Playing]")


    await dpytest.message("!enqueue https://www.youtube.com/watch?v=vxCrqtdEXAA")
    dpytest.verify_message("[Added: Migos - Deadz feat. 2 Chainz [Official Video] to the Queue]")

    await dpytest.message("!enqueue https://www.youtube.com/watch?v=PmQsZNery80")
    dpytest.verify_message("[Added: Future & Lil Uzi Vert - That's It [Official Music Video] to the Queue]")

    await dpytest.message("!queue")
    dpytest.verify_message("[Queue:\n1.Migos - Deadz feat. 2 Chainz [Official Video]\n2.Future & Lil Uzi Vert - That's It [Official Music Video]")



mood = ['Testing','Looking for output','Pain','Listening to Simon']

@tasks.loop(seconds=180)
async def change_mood():
	await bot.change_presence(activity=discord.Game(choice(mood)))	




bot.run('ODE4NzY5MzEyNjA4ODEzMDg2.YEc4WA.Q7v0luEjGI06uZPO7-fE2-Swg74')

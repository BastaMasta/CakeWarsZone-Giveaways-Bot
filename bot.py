# CakeZoneWars Giveaways Bot       - Made by BastaMasta
# This bot was made under the fiverr order #FO1D28113096
# Contact me on my discord: BASTAMASTA#6003 in case of any errors/problems

import discord
import asyncio
from discord.ext import commands
import random
import utils
from set_rewards import *

with open("TOKEN") as tk:
    kfor line in te:
        TOKEN = line
BOT_PREFIX = "!>"

emoji_ = '🎉'

CakeWarsZoneBot = commands.Bot(command_prefix=BOT_PREFIX)

CakeWarsZoneBot.remove_command('help')


@CakeWarsZoneBot.event
async def on_ready():
    print("CakeWarsZone Giveaway bot is online and managing giveaways!")
    #await CakeWarsZoneBot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Managing giveaways!"))


@CakeWarsZoneBot.command()
async def help(ctx):
    author_ = ctx.message.author
    help_embed = discord.Embed(title="Whomst has summoned the ancient one?", description="Whatever. Here is how you are supposed to use my command(s):")
    help_embed.add_field(name="giveaway_start [number of prizes] in [duration (month/day/year or hh:mm:ss)]", value="use this command to create a new giveaway.")
    help_embed.set_footer(text="I was summoned by {0}".format(author_.display_name))
    await ctx.send(embed=help_embed)


@CakeWarsZoneBot.command()
@commands.has_any_role("Owner", "Leader", "Core Staff", "Developer")
async def giveaway_start(ctx, reward, inat, duration):
    print("1")
    author1 = ctx.message.author
    #739786723642310747
    channel = CakeWarsZoneBot.get_channel(739786723642310747)
    try:
        reward = int(reward)
        sleep_time = utils.handle(inat,duration)
    except ValueError:
        return await ctx.send("You have entered an invalid value.")
    rewards=[]
    for x in range(reward):
        rewards.append(await get_reward(CakeWarsZoneBot,ctx.message))
        if rewards[-1] == False:
            return
    message1 = await show_giveaway(author1,ctx.message.channel,rewards,emoji_,inat,duration)
    if(sleep_time<5):
        await ctx.send("Automatically sleeping for 5 seconds because time is too short")
        await asyncio.sleep(5)
    await asyncio.sleep(sleep_time)
    message2 = await channel.fetch_message(message1.id)
    for reactions1 in message2.reactions:
                        if str(reactions1) == emoji_:
                            reactants = await reactions1.users().flatten()
                            win=list(map(lambda y : y.id,random.sample(list(filter(lambda x : x.bot == False,reactants)),len(rewards))))
                            winners = list(map(lambda y : rewards[win.index(y)]+" - <@"+str(y)+">",win))
                            message5 = await channel.fetch_message(message2.id)
                            completed_embed = discord.Embed(title="🎉 ~**Giveaway Ended!**~ 🎉",description=("**Winners:**\n"+"\n".join(winners)))
                            completed_embed.set_footer(text="giveaway hosted by @{0}".format(author1.display_name))
                            await message5.edit(embed=completed_embed)
                            await author1.send("The giveaway Has ended!\nAnd the winner(s) is/are **{0}**".format("\n".join(winners)))
                            for i in win:
                              print(i)
                              user = CakeWarsZoneBot.get_user(i)
                              await user.create_dm()
                              await user.send("You have won the following in the giveaway at CakeWarsZone!\n**{0}**".format(rewards[win.index(i)]))

    
        

CakeWarsZoneBot.run(TOKEN)

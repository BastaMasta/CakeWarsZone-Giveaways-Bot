# CakeZoneWars Giveaways Bot       - Made by BastaMasta
# This bot was made under the fiverr order #FO1D28113096
# Contact me on my discord: BASTAMASTA#6003 in case of any errors/problems

import discord
import asyncio
from discord.ext import commands
import discord_checkmessage
import random

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
    await CakeWarsZoneBot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Managing giveaways!"))


@CakeWarsZoneBot.command()
async def help(ctx):
    author_ = ctx.message.author
    help_embed = discord.Embed(title="Whomst has summoned the ancient one?", description="Whatever. Here is how you are supposed to use my command(s):")
    help_embed.add_field(name="giveaway_start [number of prizes] [duration (in days)]", value="use this command to create a new giveaway.\n Note: you can use decimal values for the duration of the giveaway")
    help_embed.set_footer(text="I was summoned by {0}".format(author_.display_name))
    await ctx.send(embed=help_embed)


@CakeWarsZoneBot.command()
@commands.has_any_role("Owner", "Leader", "Core Staff", "Developer")
async def giveaway_start(ctx, rewards=1, duration=1):
    dataobtained = False
    author1 = ctx.message.author
    channel = CakeWarsZoneBot.get_channel(739786723642310747)
    try:
        rewards = float(rewards)
        dataobtained = True
    except ValueError:
        ctx.send("You have entered an invalid value.")
    sleep_time = int(duration) * 60 * 60 * 24
    if dataobtained:
        if rewards == 1:
            await author1.send("Please enter the reward for the giveaway:")
            response1 = await CakeWarsZoneBot.wait_for('message', check=discord_checkmessage.message_check(channel=author1.dm_channel), timeout=500)
            reward_1 = response1.content
            if reward_1.lower() == "cancel":
                print("A giveaway was called but cancelled by {0}".format(author1.mention))
            else:
                await author1.send("Setting up a giveaway with the following reward:\n{0}\nDuration: {1} days".format(reward_1, duration))
                giveaway_embed = discord.Embed(title="🎉 ~**Giveaway started!**~ 🎉", description=" \n **Prizes:**\n1]{0} \n \nReact with {1} to get a chance to win!".format(reward_1, emoji_))
                giveaway_embed.set_footer(text="Giveaway hosted by @{0}".format(author1.display_name))
                message1 = await channel.send(embed=giveaway_embed)
                await message1.add_reaction(emoji_)
                await asyncio.sleep(sleep_time)
                try:
                    message2 = await channel.fetch_message(message1.id)
                    for reactions1 in message2.reactions:
                        if str(reactions1) == emoji_:
                            reactants = await reactions1.users().flatten()
                            total_reactants = len(reactants)
                            winner_num = random.randint(0, total_reactants - 1)
                            if reactants[winner_num].bot:
                                winner = reactants[winner_num + 1]
                                print("The winner was a bot, so switching to the next player in line!")
                            else:
                                winner = reactants[winner_num]
                            winner_user = CakeWarsZoneBot.get_user(winner.id)
                            message5 = await channel.fetch_message(message2.id)
                            completed_embed = discord.Embed(title="🎉 ~**Giveaway Ended!**~ 🎉", description="**Winners:**\n1) {0}\n**Prizes:**\n1) {1}".format(winner_user, reward_1))
                            completed_embed.set_footer(text="giveaway hosted by @{0}".format(author1.display_name))
                            await message5.edit(embed=completed_embed)
                            await author1.send("The giveaway Has ended!\nAnd the winner is **{0}**".format(winner))
                            await winner_user.send("You have won the following in the giveaway at CakeWarsZone!\n**{0}**".format(reward_1))
                except:
                    print("The giveaway message was perhaps deleted")

        elif rewards == 2:

            # get input for reward 1
            await author1.send("Please enter the first reward for the giveaway:")
            response1 = await CakeWarsZoneBot.wait_for('message', check=discord_checkmessage.message_check(channel=author1.dm_channel), timeout=500)
            reward1 = response1.content

            if reward1.lower() == "cancel":
                print("A giveaway was called but cancelled by {0}".format(author1.mention))
            else:
                # get input for reward 2
                await author1.send("Please enter the second reward for the giveaway:")
                response2 = await CakeWarsZoneBot.wait_for('message', check=discord_checkmessage.message_check(channel=author1.dm_channel), timeout=500)
                reward2 = response2.content

                if reward1.lower() == "cancel":
                    print("A giveaway was called but cancelled by {0}".format(author1.mention))
                else:
                    # Send out the giveaway message and add a reaction to it. also send the author a message

                    await author1.send("Setting up a giveaway with the following rewards:\n1){0}\n2){1}\nDuration: {2} days".format(reward1, reward2, duration))
                    giveaway_embed = discord.Embed(title="~**Giveaway started!**~", description="A new giveaway has begun!\n **Prizes:**\n \n{0}\n{1} \n \nReact with {2} to get a chance to win!".format(reward1, reward2, emoji_))
                    giveaway_embed.set_footer(text="giveaway hosted by @{0}".format(author1.display_name))
                    message1 = await channel.send(embed=giveaway_embed)
                    await message1.add_reaction(emoji_)

                    # Wait for people to react and the get the message (with the reaction ids)
                    await asyncio.sleep(sleep_time)
                    try:
                        message2 = await channel.fetch_message(message1.id)

                        # getting the correct emoji and then getting the list of users who reacted with that emoji
                        for reactions1 in message2.reactions:
                            if str(reactions1) == emoji_:
                                reactants = await reactions1.users().flatten()

                                # First winner
                                total_reactants = len(reactants)
                                winner_num_1 = random.randint(0, total_reactants - 1)
                                if reactants[winner_num_1].bot:
                                    winner_num_1 += 1
                                winner1 = reactants[winner_num_1]
                                reactants.remove(winner1)
                                winner1_user = CakeWarsZoneBot.get_user(winner1.id)
                                del total_reactants

                                # Second winner
                                total_reactants = len(reactants)
                                winner_num_2 = random.randint(0, total_reactants - 1)
                                if reactants[winner_num_2].bot:
                                    winner_num_2 += 1
                                winner2 = reactants[winner_num_2]
                                winner2_user = CakeWarsZoneBot.get_user(winner2.id)

                                # get the giveaway message and edit it, also send a giveaway_ended notif to the person who invoked the command
                                message5 = await channel.fetch_message(message2.id)
                                completed_embed = discord.Embed(title="🎉 ~**Giveaway Ended!**~ 🎉", description="**Winners:**\n1) {0}\n2) {1}\n**Prizes:**\n1) {2}\n2) {3}".format(winner1, winner2, reward1, reward2))
                                completed_embed.set_footer(text="giveaway hosted by @{0}".format(author1.display_name))
                                await message5.edit(embed=completed_embed)
                                await author1.send("The giveaway Has ended!\nAnd the winners are \n**{0}** ({1})\n**{2}** ({3})".format(winner1, reward1, winner2, reward2))
                                await winner1_user.send("You have won the following prize(s) in a giveaway at CakeWarsZone!\n{0}".format(reward1))
                                await winner2_user.send("You have won the following prize(s) in a giveaway at CakeWarsZone!\n{0}".format(reward2))
                    except:
                        print("The giveaway message was perhaps deleted")

        elif rewards == 3:

            # Get input for reward no 1
            await author1.send("Please enter the first reward for the giveaway:")
            response1 = await CakeWarsZoneBot.wait_for('message', check=discord_checkmessage.message_check(channel=author1.dm_channel), timeout=500)
            reward1 = response1.content

            if reward1.lower() == "cancel":
                print("A giveaway was called but cancelled by {0}".format(author1.mention))
            else:
                # Get input for reward no 2
                await author1.send("Please enter the second reward for the giveaway:")
                response2 = await CakeWarsZoneBot.wait_for('message', check=discord_checkmessage.message_check(channel=author1.dm_channel), timeout=500)
                reward2 = response2.content
                if reward1.lower() == "cancel":
                    print("A giveaway was called but cancelled by {0}".format(author1.mention))
                else:
                    # Get input for reward no 3
                    await author1.send("Please enter the third reward for the giveaway:")
                    response3 = await CakeWarsZoneBot.wait_for('message', check=discord_checkmessage.message_check(channel=author1.dm_channel), timeout=500)
                    reward3 = response3.content
                    if reward1.lower() == "cancel":
                        print("A giveaway was called but cancelled by {0}".format(author1.mention))
                    else:
                        # Send out the giveaway message and add a reaction to it

                        await author1.send(
                            "Setting up a giveaway with the following rewards:\n1){0}\n2){1}\n3){2}\nDuration: {3} days".format(reward1, reward2, reward3, duration))
                        giveaway_embed = discord.Embed(title="~**Giveaway started!**~", description="A new giveaway has begun!\n **Prizes:**\n \n{0}\n{1}\n{2} \n \nReact with {3} to get a chance to win!".format(reward1, reward2, reward3, emoji_))
                        giveaway_embed.set_footer(text="giveaway hosted by @{0}".format(author1.display_name))
                        message1 = await channel.send(embed=giveaway_embed)
                        await message1.add_reaction(emoji_)

                        # Wait for people to react and the get the message (with the reaction ids)
                        await asyncio.sleep(sleep_time)
                        try:
                            message2 = await channel.fetch_message(message1.id)

                            # getting the correct emoji and then getting the list of users who reacted with that emoji
                            for reactions1 in message2.reactions:
                                if str(reactions1) == emoji_:
                                    reactants = await reactions1.users().flatten()

                                    # First winner
                                    total_reactants = len(reactants)
                                    winner_num_1 = random.randint(0, total_reactants - 1)
                                    if reactants[winner_num_1].bot:
                                        winner_num_1 += 1
                                    winner1 = reactants[winner_num_1]
                                    reactants.remove(winner1)
                                    winner1_user = CakeWarsZoneBot.get_user(winner1.id)
                                    del total_reactants

                                    # Second winner
                                    total_reactants = len(reactants)
                                    winner_num_2 = random.randint(0, total_reactants - 1)
                                    if reactants[winner_num_2].bot:
                                        winner_num_2 += 1
                                    winner2 = reactants[winner_num_2]
                                    reactants.remove(winner2)
                                    winner2_user = CakeWarsZoneBot.get_user(winner2.id)
                                    del total_reactants

                                    # Third winner
                                    total_reactants = len(reactants)
                                    winner_num_3 = random.randint(0, total_reactants - 1)
                                    if reactants[winner_num_3].bot:
                                        winner_num_3 += 1
                                    winner3 = reactants[winner_num_3]
                                    winner3_user = CakeWarsZoneBot.get_user(winner3.id)

                                    # get the giveaway message and edit it, also send a giveaway_ended notif to the person who invoked the command
                                    message5 = await channel.fetch_message(message2.id)
                                    completed_embed = discord.Embed(title="Giveaway Ended!", description="The giveaway has ended!\nAnd the winners of this giveaway are...\n{0}! --you have won {1}! \n{2}! --you have won {3}! \n{4}! -- you have won {5}".format(winner1, reward1, winner2, reward2, winner3, reward3))
                                    completed_embed.set_footer(text="giveaway hosted by @{0}".format(author1.display_name))
                                    await message5.edit(embed=completed_embed)
                                    await author1.send("The giveaway Has ended!\nAnd the winners are \n**{0}** ({1})\n**{2}** ({3})\n**{4}** ({5})".format(winner1, reward1, winner2, reward2, winner3, reward3))
                                    await winner1_user.send("You have won the following prize(s) in a giveaway at CakeWarsZone!\n{0}".format(reward1))
                                    await winner2_user.send("You have won the following prize(s) in a giveaway at CakeWarsZone!\n{0}".format(reward2))
                                    await winner2_user.send("You have won the following prize(s) in a giveaway at CakeWarsZone!\n{0}".format(reward3))
                        except:
                            print("The giveaway message was perhaps deleted")

        elif rewards == 0:
            await ctx.send("You cannot have a giveaway with no rewards!")

        elif rewards > 3:
            await ctx.send("As per now, you cannot create giveaways with more than 3 rewards/prizes. \nContact BASTAMASTA#6003 to implement a system with more rewards/prizes per giveaway")

        else:
            await ctx.send("Invalid rewards value entered.\nPlease enter a value between 1 and 3")


CakeWarsZoneBot.run(TOKEN)

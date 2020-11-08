import discord
import discord_checkmessage
index=0
async def get_reward(CakeWarsZoneBot,msg):
    global index
    index=0
    author1=msg.author
    await author1.create_dm()
    await author1.send("Please enter the reward for the giveaway:")
    response1 = await CakeWarsZoneBot.wait_for('message', check=discord_checkmessage.message_check(channel=author1.dm_channel), timeout=500)
    reward_1 = response1.content
    if reward_1.lower() == "cancel":
      await msg.channel.send("A giveaway was called but cancelled by {0}".format(author1.mention))
      return False
    if len(reward_1) > 500:
      await author1.send("ERROR : Reward name is too long. Must be below 500 characters")
      return False
    return reward_1

def readable(element):
    global index
    index+=1
    return str(index)+"] "+element
async def show_giveaway(author1,channel,rewards,emoji_,inat,duration=0):
    global index
    await author1.send("Setting up a giveaway with the following reward:\n{0}\nDuration: {1}".format("\n".join(list(map(readable,rewards))), duration))
    index=0
    giveaway_embed = discord.Embed(title="🎉 ~**Giveaway started!**~ 🎉", description=" \n **Prizes:**\n{0} \n \nReact with {1} to get a chance to win!\n **Ends {2}**: {3}".format("\n".join(list(map(readable,rewards))), emoji_,inat,duration))
    giveaway_embed.set_footer(text="Giveaway hosted by @{0}".format(author1.display_name))
    message1 = await channel.send(embed=giveaway_embed)
    await message1.add_reaction("🎉")
    return message1
                
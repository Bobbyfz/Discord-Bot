import discord
import logging
from discord.ext import commands
import os

#makes all commmands start with the prefix '.' and uses the command class in order to make commands possible
client = commands.Bot(command_prefix = '.')
client.remove_command('help')
# Events

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		await ctx.send('Invalid command')

#Commands

@client.command()
async def hello(ctx):

	await ctx.send('Hello ' + format(ctx.author.display_name))
	
@client.command()
async def clear(ctx,amount : int):
	await ctx.channel.purge(limit=amount)

@client.command(pass_context = True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.blue()
		)

	embed.set_author(name = 'Help')
	embed.add_field(name = '.hello', value = 'Says hello to user', inline = False)
	embed.add_field(name = '.clear <amount>',value = 'Clears <amount> of messages',inline = False)
	await author.send(embed = embed)

#error handling
@clear.error
async def clear_error(ctx,error):
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send('Please specify an amount of messages to delete: .clear <amount>')


###################################################
#
# Logging Section
#
###################################################

#sends the log to a file called discord.log instead of outputting it the console
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',encoding = 'utf-8', mode = 'w')
handler .setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client.run('NzY5ODAzODIxMTY0NjU4NzA4.X5UVrQ.0HYKaP3q2fYTPY7Qn1gQuYy0fO8')
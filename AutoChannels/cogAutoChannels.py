# ADDON IMPORTS
import addons.AutoChannels.init as init

import addons.AutoChannels.functions.commands.commandRequirements as commandRequirements
import addons.AutoChannels.functions.commands.commandSetup as commandSetup
import addons.AutoChannels.functions.commands.commandRemove as commandRemove
import addons.AutoChannels.functions.commands.commandList as commandList

import addons.AutoChannels.functions.events.eventOnVoiceStateUpdate as eventOnVoiceStateUpdate

import addons.AutoChannels.handlers.handlerDatabaseInit as handlerDatabaseInit



# BOTASSISTANT IMPORTS
from services.serviceLogger import Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()



class AutoChannels(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # EVENTS LISTENERS
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        await eventOnVoiceStateUpdate.onVoiceStateUpdate(member, before, after)


    groupAutoChannels = discordCommands.SlashCommandGroup("autochannels", "🔶 Group of commands to manage the autochannels addon.")


    # Verify if the bot has the prerequisites permissions
    @groupAutoChannels.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)        


    # Command to setup a autochannel category
    @groupAutoChannels.command(name="setup", description="Setup a autochannel category.")
    async def cmdSetup(
        self, 
        ctx: commands.Context,
    
        # Voice channel where the autochannels will be created from the category
        channelconnect: discord.Option(discord.VoiceChannel, required=True),
        channelname: discord.Option(str, required=True, min_length=1, max_length=100)
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the setup command.", str(ctx.command))
        await commandSetup.setup(ctx, channelconnect, channelname)


    # Command to remove a autochannel category
    @groupAutoChannels.command(name="remove", description="Remove a autochannel category.")
    async def cmdRemove(
        self, 
        ctx: commands.Context,
    
        # Voice channel where the autochannels will be created from the category
        channelconnect: discord.Option(discord.VoiceChannel, required=True)
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the remove command.", str(ctx.command))
        await commandRemove.remove(ctx, channelconnect)


    # Command to list all autochannel categories
    @groupAutoChannels.command(name="list", description="List all autochannel categories.")
    async def cmdList(
        self, 
        ctx: commands.Context
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the list command.", str(ctx.command))
        await commandList.list(ctx)







def setup(bot):
    Logger.debug("Loading cog: " + init.cogName)
    handlerDatabaseInit.databaseInit()
    bot.add_cog(AutoChannels(bot))
    
    
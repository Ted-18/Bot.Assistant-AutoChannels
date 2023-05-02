import addons.AutoChannels.handlers.handlerCategories as handlerCategories

import addons.AutoChannels.settings.settingColors as settingColors
import addons.AutoChannels.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def remove(ctx, channelconnect):

    # PERMISSIONS CHECK
    import addons.AutoChannels.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdRemove") == False:
        return
    
    # Check if the channel is a autochannel
    if not handlerCategories.isAutoChannelVoiceChannel(channelconnect):

        embed = discord.Embed(
            title = "Auto Channels",
            description = "This channel is not a autochannel.",
            color = settingColors.red
        )

        embed.set_thumbnail(url=settingThumbnail.audioIcon)

        await ctx.respond(embed=embed)

        return
    
    # Remove the channel from the database
    handlerCategories.removeAutoChannel(channelconnect)

    embed = discord.Embed(
        title = "Auto Channels",
        description = "The channel has been removed from the autochannel category.",
        color = settingColors.green
    )

    embed.set_thumbnail(url=settingThumbnail.audioIcon)

    await ctx.respond(embed=embed)

    
    


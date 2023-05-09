import addons.AutoChannels.handlers.handlerCategories as handlerCategories

import addons.AutoChannels.settings.settingColors as settingColors
import addons.AutoChannels.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def setup(ctx, channelconnect, channelname, activity):

    # PERMISSIONS CHECK
    import addons.AutoChannels.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdSetup") == False:
        return

    if channelconnect.category == None:
        
        embed = discord.Embed(
            title = "Auto Channels",
            description = "You must select a voice channel that is in a category.",
            color = settingColors.red
        )

        embed.set_thumbnail(url=settingThumbnail.audioIcon)

        await ctx.respond(embed=embed)

        return
        
    # CHECK IF THE CATEGORY IS ALREADY A AUTOCHANNEL CATEGORY
    if handlerCategories.isAutoChannelCategory(channelconnect):
        embed = discord.Embed(
            title = "Auto Channels",
            description = "This category is already a autochannel category.",
            color = settingColors.red
        )

        embed.set_thumbnail(url=settingThumbnail.audioIcon)

        await ctx.respond(embed=embed)

        return
    
    # ADD THE CATEGORY TO THE DATABASE
    handlerCategories.addAutoChannel(channelconnect, channelname, activity)

    embed = discord.Embed(
        title = "Auto Channels",
        description = "The category has been setup as a autochannel category.",
        color = settingColors.green
    )

    embed.set_thumbnail(url=settingThumbnail.audioIcon)

    await ctx.respond(embed=embed)

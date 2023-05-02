import prettytable

import addons.AutoChannels.handlers.handlerCategories as handlerCategories

import addons.AutoChannels.settings.settingColors as settingColors
import addons.AutoChannels.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def list(ctx):

    # PERMISSIONS CHECK
    import addons.AutoChannels.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdList") == False:
        return
    

    # Get all autochannel categories from the server
    autoChannelCategories = handlerCategories.listAutoChannels(ctx.guild.id)

    table = prettytable.PrettyTable()
    table.field_names = ["Category", "Channel", "Channel Name"]

    if autoChannelCategories != False:
        for category in autoChannelCategories:
            
            # Get the channel
            channel = ctx.guild.get_channel(category[3])

            if channel == None:
                handlerCategories.removeAutoChannelID(category[3])
                continue
            elif channel.category == None:
                handlerCategories.removeAutoChannelID(category[3])
                continue
            elif channel.category.id != category[2]:
                handlerCategories.removeAutoChannelID(category[3])
                continue

            table.add_row([category[2], category[3], category[4]])

    if len(table._rows) == 0:
        embed = discord.Embed(
            title = "Auto Channels",
            description = "There are no autochannel categories on this server. \n\n Use `autochannels setup` to setup a autochannel category.",
            color = settingColors.red
        )

        embed.set_thumbnail(url=settingThumbnail.audioIcon)

        await ctx.respond(embed=embed)

        return

    embed = discord.Embed(
        title = "Auto Channels",
        description = "Here is a list of all autochannel categories.",
        color = settingColors.blue
    )

    embed.set_thumbnail(url=settingThumbnail.audioIcon)

    await ctx.respond(embed=embed)

    await ctx.send("`" + table.get_string() + "`")

    
import addons.AutoChannels.handlers.handlerCategories as handlerCategories

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()


async def onVoiceStateUpdate(member, before, after):
    await channelBefore(member, before)
    await channelAfter(member, after)


async def channelBefore(member, before):
    # Verify if the member has left a channel
    if before.channel != None:

        # Verify if the left channel is in a category
        if before.channel.category == None:
            return

        # Verify if the channel is afk channel
        if before.channel == member.guild.afk_channel:
            return
        
        # Verify if is a autochannel category
        if not handlerCategories.isAutoChannelCategory(before.channel):
            return

        # Verify if the channel is a autochannel
        if handlerCategories.isAutoChannelVoiceChannel(before.channel):
            return
        
        # Verify if the channel is empty
        if len(before.channel.members) > 0:
            return
        
        # Delete the channel
        try:
            await before.channel.delete()
        except:
            return


async def channelAfter(member, after):
    # Verify if the member joined a channel
    if after.channel != None:

        # Verify if the joined channel is in a category
        if after.channel.category == None:
            return
       
        # Verify if the channel category is a autochannel category
        if not handlerCategories.isAutoChannelVoiceChannel(after.channel):
            return
        
        # Get the name of the channel from the database
        channelName = handlerCategories.getAutoChannelName(after.channel)

        if handlerCategories.isAutoChannelActivity(after.channel):

            if len(member.activities) > 0:
                
                for activity in member.activities:
                    if activity.type == discord.ActivityType.playing:
                        channelName = activity.name
                        break

            else:   
                channelName = handlerCategories.getAutoChannelName(after.channel)
            

        # Create the channel in the category with permissions of after.channel
        channel = await after.channel.category.create_voice_channel(channelName, overwrites=after.channel.overwrites)

        # Move the member to the new channel
        await member.move_to(channel)



    
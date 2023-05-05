import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import Logger

from settings.settingBot import debug


def isAutoChannelCategory(channel):
    requestFormat = """
                    SELECT * FROM addon_autochannels_categories
                    WHERE serverID = %s AND categoryID = %s
                    """
    requestSettings = (channel.guild.id, channel.category.id,)

    try:
        Logger.debug("[HANDLER][AUTOCHANNELS][IS] Checking if a category is a autochannel " + str(channel.guild.id) + " " + str(channel.category.id))
            
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if result != []:
            return True
        else:
            return False
        
    except Exception as error:
            
            Logger.error("[HANDLER][AUTOCHANNELS][IS] DB error isAutochannelCategory -> " + str(error))
            return False
    

def isAutoChannelVoiceChannel(channel):
    requestFormat = """
                    SELECT * FROM addon_autochannels_categories
                    WHERE serverID = %s AND channelID = %s
                    """
    requestSettings = (channel.guild.id, channel.id,)

    try:
        Logger.debug("[HANDLER][AUTOCHANNELS][IS] Checking if a voice channel is a autochannel " + str(channel.guild.id) + " " + str(channel.id))
            
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if result != []:
            return True
        else:
            return False
        
    except Exception as error:
            
            Logger.error("[HANDLER][AUTOCHANNELS][IS] DB error isAutochannelVoiceChannel -> " + str(error))
            return False


def getAutoChannelName(channel):
    requestFormat = """
                    SELECT channelName FROM addon_autochannels_categories
                    WHERE serverID = %s AND categoryID = %s
                    """
    requestSettings = (channel.guild.id, channel.category.id,)

    try:
        Logger.debug("[HANDLER][AUTOCHANNELS][GET] Getting the autochannel name " + str(channel.guild.id) + " " + str(channel.category.id))
            
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if result != []:
            return result[0][0]
        else:
            return False
        
    except Exception as error:
            
            Logger.error("[HANDLER][AUTOCHANNELS][GET] DB error getAutoChannelName -> " + str(error))
            return False
        
def addAutoChannel(channelConnect, channelName):
    requestFormat = """
                    INSERT INTO addon_autochannels_categories
                    (serverID, categoryID, channelID, channelName)
                    VALUES (%s, %s, %s, %s)
                    """
    requestSettings = (channelConnect.guild.id, channelConnect.category.id, channelConnect.id, channelName,)

    try:
        Logger.debug("[HANDLER][AUTOCHANNELS][ADD] Adding a autochannel to the DB " + str(channelConnect.guild.id) + " " + str(channelConnect.category.id) + " " + str(channelConnect.id))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        
        Logger.error("[HANDLER][AUTOCHANNELS][ADD] DB error addAutoChannel -> " + str(error))


def removeAutoChannel(channelConnect):
    requestFormat = """
                    DELETE FROM addon_autochannels_categories
                    WHERE serverID = %s AND categoryID = %s AND channelID = %s
                    """
    requestSettings = (channelConnect.guild.id, channelConnect.category.id, channelConnect.id,)

    try:
        Logger.debug("[HANDLER][AUTOCHANNELS][REMOVE] Removing a autochannel from the DB " + str(channelConnect.guild.id) + " " + str(channelConnect.category.id) + " " + str(channelConnect.id))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        
        Logger.error("[HANDLER][AUTOCHANNELS][REMOVE] DB error removeAutoChannel -> " + str(error))

    
def removeAutoChannelID(channelID):
    requestFormat = """
                    DELETE FROM addon_autochannels_categories
                    WHERE channelID = %s
                    """
    requestSettings = (channelID,)

    try:
        Logger.debug("[HANDLER][AUTOCHANNELS][REMOVE] Removing a autochannel from the DB " + str(channelID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        
        Logger.error("[HANDLER][AUTOCHANNELS][REMOVE] DB error removeAutoChannelID -> " + str(error))


def listAutoChannels(serverID):
    requestFormat = """
                    SELECT * FROM addon_autochannels_categories
                    WHERE serverID = %s
                    """
    requestSettings = (serverID,)

    try:
        Logger.debug("[HANDLER][AUTOCHANNELS][LIST] Listing all autochannels from the DB " + str(serverID))
            
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if result != []:
            return result
        else:
            return False
        
    except Exception as error:
            
            Logger.error("[HANDLER][AUTOCHANNELS][LIST] DB error listAutoChannels -> " + str(error))
            return False

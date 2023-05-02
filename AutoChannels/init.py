# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-AutoChannels"
version = "1.0.1"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "autochannels"

# Name of the file containing the cog
cogFile = "cogAutoChannels"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python",
    "prettytable"
]

# List of addons required by the addon
addonDependencies = [
    "Configuration"
]

# List of permissions required by the addon
addonPermissions = [
    "manage_channels",
    "manage_messages",
    "move_members",
    "send_messages"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",


    # Permission to setup a autochannel category
    "cmdSetup" : "discord.permission.manage_guild",

    # Permission to remove a autochannel category
    "cmdRemove" : "discord.permission.manage_guild",

    # Permission to list all the autochannel categories
    "cmdList" : "discord.permission.manage_guild",


    # Permission to add a voice channel to the whitelist of a autochannel category
    "cmdWhitelistAdd" : "discord.permission.manage_guild",

    # Permission to remove a voice channel from the whitelist of a autochannel category
    "cmdWhitelistDelete" : "discord.permission.manage_guild",

    # Permission to list all the whitelisted voice channels of a autochannel category
    "cmdWhitelistList" : "discord.permission.manage_guild"

}
import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

# Create the database if it does not exist
def databaseInit():
    if settingBot.databaseType == "MariaDB":
        # Table structure
        tableName = "addon_autochannels_categories"
        columns = [
            ["serverID", "BIGINT NOT NULL"],
            ["categoryID", "BIGINT NOT NULL"],
            ["channelID", "BIGINT NOT NULL"],
            ["channelName", "VARCHAR(100) NOT NULL"],
            ["activity", "BOOLEAN NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        # # Table structure
        # tableName = "addon_autochannels_excluded"
        # columns = [
        #     ["serverID", "BIGINT NOT NULL"],
        #     ["channelID", "BIGINT NOT NULL"]
        # ]
        # serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        # Table structure
        tableName = "addon_autochannels_categories"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["categoryID", "integer NOT NULL"],
            ["channelID", "integer NOT NULL"],
            ["channelName", "varchar(100) NOT NULL"],
            ["activity", "bool NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        # # Table structure
        # tableName = "addon_autochannels_excluded"
        # columns = [
        #     ["serverID", "integer NOT NULL"],
        #     ["channelID", "integer NOT NULL"]
        # ]
        # serviceDatabase.databaseCreation(tableName, columns)


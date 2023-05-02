import services.serviceDatabase as serviceDatabase

# Create the database if it does not exist
def databaseInit():
    # Table structure
    tableName = "addon_autochannels_categories"
    columns = [
        ["serverID", "BIGINT NOT NULL"],
        ["categoryID", "BIGINT NOT NULL"],
        ["channelID", "BIGINT NOT NULL"],
        ["channelName", "VARCHAR(100) NOT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)

    # # Table structure
    # tableName = "addon_autochannels_excluded"
    # columns = [
    #     ["serverID", "BIGINT NOT NULL"],
    #     ["channelID", "BIGINT NOT NULL"]
    # ]
    # serviceDatabase.databaseCreation(tableName, columns)


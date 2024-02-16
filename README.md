# Anonymous-Confession-Bot-Telegrams
Allows users to share anonymous confessions within a group, fostering a space for openness and sharing. it's so people can anonymize their thoughts.

Start Command (/start):

Users initiate the bot with the "/start" command, receiving a welcome message encouraging them to share anonymous confessions.
Confession Function (confess):

Users share their confessions by sending any text message to the group chat.
The bot appends each confession to the confessions list.
View Confessions Command (/view_confessions):

Users can view all submitted confessions anonymously with the "/view_confessions" command.
The bot randomizes the order of the confessions using random.shuffle() before displaying them.
Each confession is numbered for reference.
Randomized Confessions:

The use of random.shuffle() ensures that the confessions are presented in a different order each time users request to view them.
This randomization adds an additional layer of anonymity, making it more challenging to associate specific confessions with individual users.
Persistent Storage:

Note that this script uses in-memory storage for simplicity. In a production scenario, you might want to consider using a database to store confessions persistently.


I don't use this code, you can use it, but if anything is changed, please mention it in your repo.

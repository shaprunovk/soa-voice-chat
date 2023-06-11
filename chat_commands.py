class ClientCommands:
    MEMBERS = "/members"
    EXIT = "/exit"
    CREATE_CHAT = "/create_chat"
    INVITE = "/invite"
    LEAVE = "/leave"
    RECORD = "/record"
    KEYBOARD = " /keyboard"
    HELP = "/help"
    COMMANDS_LIST = "Here is a list of commands:\n" \
                  " - /members - get list of members of chatroom\n" \
                  " - /exit - disconnect from server\n" \
                  " - /create_chat {chat_title} - create a chatroom\n" \
                  " - /invite - invite a member to the chatroom (only in created chatrooms)\n" \
                  " - /leave - leave a chatroom (only in created chatrooms)\n" \
                  " - /record - use microphone as source of input\n" \
                  " - /keyboard - use keyboard as source of input\n" \
                  " - /help - print this message\n"

client_commands = ClientCommands()

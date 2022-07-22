def discord_using(userInput):
    try:
        if userInput[2] == "webhook":
            if userInput[3] == "url":
                pass
            elif userInput[3] == "say":
                from discord_webhook import DiscordWebhook

                for _ in range(4):
                    userInput.pop(0)

                content = " ".join(userInput)
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/953013404405215303/DWz1tR9BbZwVq-EY9mnlYcQxUwFOqgnqIkcIv3KD49hioON8Uw8ruhHNo_jBBdh-8ZIJ", content=content)

                response = webhook.execute()
                print("Message sent !")
            else:
                print("Wrong option : help bsh.discord for more informations !")
    except:
        print("An error has occurred")

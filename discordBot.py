import discord
import json
import requests
import random

#SI=800731269901320193
def read_token():
    with open('token.txt','r') as f:
        lines=f.readlines()
        return lines[0].strip()

token=read_token()
client=discord.Client()


sad_messages=['sad','depressing','depressed','sucidal','angry','pain','miserable']
encouraging_statements=[
    'Cheer Up!',
    'You are awesome!',
    "time will Heal",
    'stop Overthinking',
    'YOu are great',
    "Start Loving yourself",
    'Start Meditation',
    'Believe in yourself!'
]
bad_words=['Fuck',"Shit","Motherfucker",'Cunt',"asshole","Dick","Pussy"]
def get_quote():
    response= requests.get(' /random')
    json_data= json.loads(response.text)
    quote = json_data[0]['q']+ " -"+ json_data[0]['a']
    return (quote)



@client.event
async  def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) =="general":
            await client.send_message(f"""Welcome to the server {member.mention}""")



@client.event
async def on_message(message):

    id=client.get_guild(800731269901320193)
    channels=['ambush-working']    #the channels of my server where the commands work
    valid_users=["Ambush#2333"]

    for word in bad_words:
        if message.content.count(word) >0:
            print("A bad word was said")
            await message.channel.purge(limit=1)
    if message.content == "!help":
        embed=discord.Embed(title='Useful Commands',description="Some Useful Commands")
        embed.add_field(name="!hello",value="Greets the user")
        embed.add_field(name='!users',value="Prints Number of Users ")
        embed.add_field(name="!inspire",value="Throws you Inspiration quote with Author")
        await message.channel.send(content=None,embed=embed )

    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:  #find returns the -1 if not found
            await message.channel.send("HI")
        elif message.content == "!users":
            await message.channel.send(f"""Number of members {id.member_count}""")
        # elif message.content == '!help':
        #     await  message.channel.send("Enter !users to know number of members in the channel")
        elif message.content == "!inspire":
            quote= get_quote()
            await message.channel.send(quote)
        elif any(word in message.content for word in sad_messages):
            await message.channel.send(random.choice(encouraging_statements))
    else:
        print(f"User {message.author} tried to do command {message.content} in {message.channel}")
    

client.run(token)





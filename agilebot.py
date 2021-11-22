import discord
import redis
import os
import boto3
import time
import codetiming

from discord.ext import commands
from dotenv import load_dotenv
from codetiming import Timer

load_dotenv()

redis_server = redis.Redis() # Create access to Redis
client = discord.Client() # starts the discord client.

AUTH_TOKEN = str(redis_server.get('AUTH_TOKEN').decode('utf-8'))

bot = commands.Bot(command_prefix='!')

class get_resource:
    def __init__(self, resource, instanceid):
        self.ec2 = boto3.resource(resource)
        self.instance = self.ec2.Instance(instanceid)

class get_state:
    def __init__(self, resource, instanceid):
        self.name = 'unavailable'
        self.instance = get_resource(resource, instanceid).instance
        self.name = self.instance.state['Name'].lower()

class get_publicip:
    def __init__(self, resource, instanceid):
        self.instance = get_resource(resource, instanceid).instance
        if get_state(resource, instanceid).name == 'running':
            self.ip = self.instance.public_ip_address
        else:
            self.ip = 'no ip'

class invoke_stop:
    def __init__(self, resource, instanceid):
        self.instance = get_resource(resource, instanceid).instance
        if get_state(resource, instanceid).name == 'running':
            self.instance.stop()
            while get_state(resource, instanceid).name != 'stopped' or get_state(resource,instanceid).name != 'stopping':
                time.sleep(10)

class invoke_restart:
    print(f"not available")

class invoke_update:
    print(f"not available")

@bot.command(name='chode', help='testing multiple args', pass_context=True)
async def chode(ctx, server, command):
    server = server.lower()
    command = command.lower()
    if server == 'satisfactory':
        instanceid = '<instanceid>'

        if command == 'getip':
            if get_state('ec2', instanceid).name != 'running':
                await ctx.send("Satisfactory server is not running, please start the server")
                return
            await ctx.send(get_publicip('ec2', instanceid).ip)

        elif command == 'start':
            if get_state('ec2', instanceid).name == 'stopped':
                get_resource('ec2', instanceid).instance.start()
                await ctx.send("Current Satisfactory state is: " + get_state('ec2', instanceid).name)
                while get_state('ec2', instanceid) != 'running':
                    if get_state('ec2', instanceid).name == 'running':
                        break
                    time.sleep(10)

            await ctx.send("Current Satisfactory IP is:  " + get_publicip('ec2', instanceid).ip)

        elif command == 'status':
            await ctx.send("Current Satisfactory state is:  " + get_state('ec2', instanceid).name)

        elif command == 'restart':
            if ctx.message.author == client.user:
                return
            if get_state('ec2', instanceid) == 'running':
                get_resource('ec2', instanceid).restart()
                time.sleep(5)
                while get_state('ec2', instanceid) != 'running':
                    time.sleep(10)
            await ctx.send("Current server state is: " + get_state('ec2', instanceid).name)
            await ctx.send("Current Satisfactory IP is:  "+ get_publicip('ec2', instanceid).ip)

        elif command == 'stop':
            if get_state('ec2', instanceid).name == 'running':
                get_resource('ec2', instanceid).instance.stop()
                await ctx.send("Current Satisfactory state is: " + get_state('ec2', instanceid).name)
                while get_state('ec2', instanceid) != 'stopped':
                    if get_state('ec2', instanceid).name == 'stopped':
                        break
                    time.sleep(10)
            
            await ctx.send("Satisfactory server state is " + get_state('ec2', instanceid).name)
            
    elif server == 'botserver':
        if command == 'getip':
            instanceid = '<instanceid>'
            await ctx.send(get_publicip('ec2', instanceid).ip)

    elif server == 'valheim':
        if command == 'getip':
            instanceid = '<instanceid>'
            await ctx.send(get_publicip('ec2', instanceid).ip)

bot.run(AUTH_TOKEN) # Pull Auth Token from above


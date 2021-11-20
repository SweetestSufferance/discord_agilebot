import discord
import redis
import os
import boto3
import time

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

redis_server = redis.Redis() # Create access to Redis
client = discord.Client() # starts the discord client.

AUTH_TOKEN = str(redis_server.get('AUTH_TOKEN').decode('utf-8'))

bot = commands.Bot(command_prefix='!')

class get_resource:
    def __init__(self, resource, instanceid)
        self.ec2 = boto3.resource(resource)
        self.instance = self.ec2.Instance(instanceid)

class get_state:
    def __init__(self, resource, instanceid):
        self.name = 'unavailable'
        self.instance = get_resource(resource, instanceid)
        self.name = self.instance.state['Name'].lower()

class get_publicip:
    def __init__(self, resource, instanceid):
        self.instance = get_resource(resource, instanceid)
        if get_state(resource, instanceid).name == 'running':
            self.publicip = self.instance.

class invoke_stop:
    def __init__(self, resource, instanceid):
        self.instance = get_resource(resource, instanceid)
        if get_state(resource, instanceid).name == 'running':
            self.instance.stop()
            while get_state(resource, instanceid).name != 'stopped'
            sleep 10

class invoke_restart

class invoke_update


def getip(server,instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    if instance.state['Name'].lower() != 'running':
        await ctx.send(server + "is not running, please start the server")
        return
    public_ip = instance.public_ip_address
    await ctx.send(public_ip)

def status(server,instance_id)

def start(server,instance_id)

def stop(server,instance_id)

def restart(server,instance_id)

def update(server.instance_id)

@bot.command(name='chode', help='testing multiple args', pass_context=True)
async def chode(ctx, server, command):
    server = server.lower()
    command = command.lower()
    if server == 'satisfactory':
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance('<instanceid>')

        if command == 'getip':
            if instance.state['Name'] != 'running':
                await ctx.send("Satisfactory server is not running, please start the server")
                return

            publicip = instance.public_ip_address
            await ctx.send(publicip)

        elif command == 'start':
            if instance.state['Name'] == 'stopped':
                instance.start()
                while instance.state['Name'] != 'running':
                    instance = ec2.Instance('<instanceid>')
                    await ctx.send("Current Satisfactory state is:  "+instance.state['Name'])
                    time.sleep(10)
            elif instance.state['Name'] == 'running':
                await ctx.send("Satisfactory server state is "+instance.state['Name']+", there is no need to start the server")
            await ctx.send("Current Satisfactory IP is:  "+instance.public_ip_address)

        elif command == 'status':
            await ctx.send("Current Satisfactory state is:  "+instance.state['Name'])

        elif command == 'restart':
            if ctx.message.author == client.user:
                return
            instance = ec2.Instance('<instanceid>')
            if ctx.message.author.mention == '<username>':
                if instance.state['Name'] != 'running':
                    await ctx.send("Please start the server before issuing a restart command")
                    return
                instance.restart()
                await ctx.send("Waiting for system to restart")
                while instance.state['Name'] != 'running':
                    instance = ec2.Instance('<instanceid>')
                    await ctx.send("Current instance state is:  "+instance.state['Name']+", waiting for server to start")
                    time.sleep(10)
            elif instance.state['Name'] == 'running':
                await ctx.send("Satisfactory server state is "+instance.state['Name']+", there is no need to start the server")
            elif instance.state['Name'] == 'stopped' or instance.state['Name'] == 'stopping':
                await ctx.send("Satisfactory server is in a stopped or stopping state, please issue a start command")
                return
            await ctx.send("Current Satisfactory IP is:  "+instance.public_ip_address)

    elif server == 'botserver':
        if command == 'getip':
            ec2 = boto3.resource('ec2')
            instance = ec2.Instance('<instanceid>')
            publicip = instance.public_ip_address
            await ctx.send(ctx.guild.roles)
            await ctx.send(discord.Member.roles)
            await ctx.send(publicip)

    elif server == 'valheim':
        if command == 'getip':
            print(command)
            ec2 = boto3.resource('ec2')
            instance = ec2.Instance('')
            publicip = instance.public_ip_address
            await ctx.send(publicip)

bot.run(AUTH_TOKEN) # Pull Auth Token from above


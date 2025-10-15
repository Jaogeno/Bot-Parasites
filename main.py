import os
import discord
from discord.ext import commands
from discord import app_commands
from myserver import server_on

# เปิด intents ให้บอทเห็นสมาชิกใหม่
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# ใส่ Channel ID ของช่องต้อนรับ (คลิกขวาที่ช่อง → Copy ID)
WELCOME_CHANNEL_ID = 1427721391288877126  # เปลี่ยนเป็นของคุณ
BYE_CHANNEL_ID = 1427775068355821650


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    """ส่งข้อความต้อนรับเมื่อมีสมาชิกใหม่"""
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="🎉 ยินดีต้อนรับสู่โลก!",
            description=f"{member.mention} เข้าร่วมเซิร์ฟเวอร์แล้ว!",
            color=discord.Color.green())
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"สมาชิกทั้งหมด: {member.guild.member_count}")
        await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(BYE_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="👋 ลาก่อนออกจากโลกไป",
            description=f"{member.name} ออกจากเซิร์ฟเวอร์แล้ว",
            color=discord.Color.red())
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(
            text=f"เหลือสมาชิกทั้งหมด: {member.guild.member_count}")
        await channel.send(embed=embed)


server_on()

bot.run(os.getenv('TOKEN'))
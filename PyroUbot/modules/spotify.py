from pyrogram import Client, filters
import requests
import os
import re
from PyroUbot import *

__MODULE__ = "sᴘᴏᴛɪғʏ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴏᴛɪғʏ ⦫</b>
<blockquote><b>
⎆ Perintah :
ᚗ <code>{0}spotify</code> judul lagu
⊶ Mendownload Music Yang Di Inginkan.</b></blockquote>
"""

# Isi cookie sp_dc kamu di sini (dari browser)
SPOTIFY_COOKIES = {
    "sp_dc": "ISI_COOKIE_SP_DC_KAMU"
}

@PY.UBOT("spotify")
async def spotify_search(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Gunakan format: /spotify <judul lagu>")
        return

    proses_msg = await message.reply_text("🔎 Mencari lagu...")

    # --- Cari track URL dari Spotify web ---
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html",
    }
    search_url = f"https://open.spotify.com/search/{query.replace(' ', '%20')}"
    resp = requests.get(search_url, headers=headers, cookies=SPOTIFY_COOKIES)
    if resp.status_code != 200:
        await proses_msg.edit_text(f"Gagal ambil data dari Spotify: {resp.status_code}")
        return

    # Cari track id pertama
    match = re.search(r'/track/([a-zA-Z0-9]+)', resp.text)
    if not match:
        await proses_msg.edit_text("Tidak ditemukan hasil untuk pencarian tersebut.")
        return

    track_id = match.group(1)
    track_url = f"https://open.spotify.com/track/{track_id}"

    await proses_msg.edit_text(f"👅 Mengunduh lagu...\n{track_url}")

    # --- Download lagu dengan spotdl ---
    # File akan terdownload di direktori berjalan
    prev_files = set(os.listdir('.'))
    exit_code = os.system(f'spotdl "{track_url}"')
    if exit_code != 0:
        await proses_msg.edit_text("Gagal mengunduh lagu dengan spotDL.")
        return

    # Cari file baru (hasil download)
    new_files = set(os.listdir('.')) - prev_files
    audio_path = None
    for file in new_files:
        if file.lower().endswith(('.mp3', '.m4a', '.flac', '.ogg')):
            audio_path = file
            break

    if not audio_path or not os.path.exists(audio_path):
        await proses_msg.edit_text("Gagal menemukan file audio hasil download.")
        return

    # Info untuk caption
    title = audio_path.replace('.mp3','').replace('-',' ').replace('_',' ')
    caption = f"🎵 <b>{title}</b>\n🔗 <a href='{track_url}'>Dengarkan di Spotify</a>"

    await client.send_audio(
        chat_id=message.chat.id,
        audio=audio_path,
        caption=caption
    )

    os.remove(audio_path)
    await proses_msg.delete()

import os

print("Menyiapkan Sleepy-LeechBot...")

envs = {
    "BOT_TOKEN": "8164145538:AAECz7VM5yy8W2426hiH1LMVHUzU4lWaN1o",
    "API_ID": "28772864",
    "API_HASH": "04515fdcd29eacf123010c206a9d7341",
    "OWNER_ID": "8102071209",
    "DOWNLOAD_DIR": "downloads",
    "UPSTREAM_REPO": "https://github.com/anasty17/mirror-leech-telegram-bot",
    "UPSTREAM_BRANCH": "master",
    "IS_TEAM_DRIVE": "False",
    "USE_SERVICE_ACCOUNTS": "False",
    "DATABASE_URL": ""
}

with open(".env", "w") as f:
    for key, value in envs.items():
        f.write(f"{key}={value}\n")

print(".env berhasil dibuat!")
print("Silakan jalankan bot dengan:")
print("    bash start.sh")

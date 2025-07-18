import os
import aiofiles
import asyncio

async def fake_upload_to_gdrive(file_path: str) -> str:
    # Simulasi upload ke GDrive
    await asyncio.sleep(1)
    return f"https://drive.google.com/fake/{os.path.basename(file_path)}"

async def upload_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError("File tidak ditemukan.")
    return await fake_upload_to_gdrive(file_path)

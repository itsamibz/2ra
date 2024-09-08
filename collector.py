import requests
from bs4 import BeautifulSoup
import os

# لینک تلگرام
url = "https://t.me/s/v2ray_configs_pool"

# ارسال درخواست به لینک
response = requests.get(url)
response.raise_for_status()  # بررسی موفقیت درخواست

# تجزیه محتوای HTML
soup = BeautifulSoup(response.text, 'html.parser')

# استخراج متن پیام‌ها
messages = soup.find_all('div', class_='tgme_widget_message_text')

# کلمات کلیدی کانفیگ‌های V2Ray
keywords = ['vmess', 'vless', 'trojan', 'shadowsocks']

# مسیر فایل
file_path = 'v2ray_configs.txt'

# ذخیره پیام‌ها در فایل .txt
with open(file_path, 'w', encoding='utf-8') as file:
    for message in messages:
        text = message.get_text(separator="\n")
        if any(keyword in text for keyword in keywords):
            file.write(text)
            file.write("\n\n")

print(f"فایل‌های کانفیگ V2Ray با موفقیت در {file_path} ذخیره شدند.")

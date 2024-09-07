import requests
from bs4 import BeautifulSoup
import os
import re

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

# الگوهای کانفیگ‌های V2Ray
patterns = {
    'vmess': re.compile(r'vmess://[a-zA-Z0-9+/=]+'),
    'vless': re.compile(r'vless://[a-zA-Z0-9+/=]+'),
    'trojan': re.compile(r'trojan://[a-zA-Z0-9+/=]+'),
    'shadowsocks': re.compile(r'ss://[a-zA-Z0-9+/=]+')
}

# مسیر فایل
file_path = 'v2ray_configs.txt'

# ذخیره کانفیگ‌های خالص در فایل .txt و نمایش در کنسول
with open(file_path, 'w', encoding='utf-8') as file:
    for message in messages:
        text = message.get_text(separator="\n")
        for keyword, pattern in patterns.items():
            matches = pattern.findall(text)
            for match in matches:
                file.write(match)
                file.write("\n\n")
                print(match)  # نمایش کانفیگ در کنسول

print(f"کانفیگ‌های خالص V2Ray با موفقیت در {file_path} ذخیره شدند.")

import requests
from bs4 import BeautifulSoup
import re

# لینک مورد نظر
url = 'https://t.me/s/An0nymousTeam'

# درخواست به لینک
response = requests.get(url)

# بررسی وضعیت پاسخ
if response.status_code == 200:
    # محتوای HTML را دریافت کنید
    html_content = response.text
    
    # استفاده از BeautifulSoup برای پارس کردن HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # استخراج متن از HTML
    text = soup.get_text()
    
    # استفاده از regex برای پیدا کردن محتوای بین {"remarks و true}]}}
    pattern = r'{"remarks.*?true\}\]\}\}'
    matches = re.findall(pattern, text, re.DOTALL)
    
    # اضافه کردن کاما بعد از هر true}]}}
    modified_matches = [match + ',' for match in matches]
    
    # اضافه کردن [ در ابتدا و ] در انتها
    final_content = '[ ' + ' '.join(modified_matches) + ' ]'
    
    # ذخیره محتوای استخراج شده در فایل
    with open('fragment.txt', 'w', encoding='utf-8') as f:
        f.write(final_content + '\n')
    
    print("محتوا با موفقیت استخراج و ذخیره شد.")
else:
    print(f"خطا در دریافت محتوا: {response.status_code}")

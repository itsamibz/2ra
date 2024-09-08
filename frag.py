import requests
from bs4 import BeautifulSoup

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
    
    # پیدا کردن متن بین دو عبارت خاص
    start = text.find('{"remarks')
    end = text.find('true}]}}', start)
    
    if start != -1 and end != -1:
        extracted_text = text[start:end + len('true}]}}')]
        
        # ذخیره متن استخراج شده در فایل
        with open('extracted_text.txt', 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        
        print("متن استخراج شده و در فایل ذخیره شد.")
    else:
        print("عبارات مورد نظر یافت نشد.")
else:
    print(f"خطا در دریافت محتوا: {response.status_code}")

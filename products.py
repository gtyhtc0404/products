# 讀取檔案
import os  # operating system

products = []
if os.path.isfile('products.csv'):  # 檢查檔案在不在
    print('找到檔案了！')
    with open ('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品，價格' in line:
                continue  # 繼續 直接跳到下一回(還在迴圈中) 通常寫在迴圈中很前面的位置
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    
else:
    print('找不到檔案...直接建立新資料')

# 使用者輸入新資料
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    products.append([name, price])

# 印出所有商品紀錄
for p in products:
    if p[0] == '商品':
        continue
    print(p[0], '的價格是：', p[1]) 
    
# 寫入資料(追加新資料)
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        if p[0] == '商品':
            continue
        f.write(p[0] + ',' + p[1] + '\n')
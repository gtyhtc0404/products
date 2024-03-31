import os  # os=operating system

# 讀取檔案(舊資料)
def read_file(filename):  # 檔名建議設定成參數 就不用寫死
    products = []
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue  # 繼續 直接跳到下一回(還在迴圈中) 通常寫在迴圈中很前面的位置
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return products

# 使用者輸入(新資料)
def user_input(products):  # products設定成參數 因為是function外部的資料
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        products.append([name, price])
    print(products)
    return products

# 印出所有商品紀錄
def print_products(products):  # products設定成參數 因為是function外部的資料
    for p in products:
        print(p[0], '的價格是：', p[1]) 
    
# 寫入資料(新資料) 不須回傳任何資料
def write_file(filename, products):  # 檔名/products設定成參數
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

# main function
def main(filename):
    if os.path.isfile(filename):  # 檢查檔案在不在可以不用單獨寫成function
        print('找到檔案了！')
        products = read_file(filename)
    else:
        print('找不到檔案...直接建立新資料')   
    products = user_input(products)
    print_products(products)
    write_file(filename, products)
main('products.csv')
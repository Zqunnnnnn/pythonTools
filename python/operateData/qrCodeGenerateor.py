import qrcode
import os
import pandas as pd
from PIL import Image

# Excel文件路径
excel_path = r'C:\Users\sjkj\Desktop\productserialbanks.xls'
# 输出目录
output_dir = r'C:\Users\sjkj\Desktop\qrcodes'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取Excel文件
df = pd.read_excel(excel_path)

# 遍历imageContent列中的每个URL
for index, url in enumerate(df['imageContent'], start=1):
    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # 将二维码保存为图像
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = os.path.join(output_dir, f'qr_code_{index}.png')
    img.save(img_path)
    print(f'二维码已生成并保存到：{img_path}')

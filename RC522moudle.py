from machine import Pin, SPI
import mfrc522 # 导入RFID读卡器驱动模块

# # 面向结果
# 构造一个硬件SPI对象
# spi = SPI(1, baudrate=5000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
# 
# # 构造一个RFID读卡器对象
# rfid = mfrc522.MFRC522(spi, Pin(4), Pin(5)) # 使用GPIO4作为RST信号，GPIO5作为SS信号
# 
# # 循环检测是否有卡片靠近
# while True:
#     # 搜索卡片
#     status, tag_type = rfid.request(rfid.REQIDL)
#     if status == rfid.OK: # 如果找到了卡片
#         # 防冲突，返回卡片的UID
#         status, uid = rfid.anticoll()
#         if status == rfid.OK: # 如果成功获取了UID
#             # 打印UID
#             print('Card UID:', uid)


class RC522_M(object):
    def __init__(self, sck_PIN_ID, mosi_PIN_ID, miso_PIN_ID, rst_PIN_ID, ss_PIN_ID):
        self.spi = SPI(1, baudrate=5000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(sck_PIN_ID), mosi=Pin(mosi_PIN_ID), miso=Pin(miso_PIN_ID))
        self.rfid = mfrc522.MFRC522(spi, Pin(rst_PIN_ID), Pin(ss_PIN_ID)) # RST信号, SS信号
        
    def rfc_read(self):
        while True:
            # 搜索卡片
            status, tag_type = self.rfid.request(rfid.REQIDL)
            if status == self.rfid.OK:
                # 防冲突，返回卡片的UID
                status, uid = self.rfid.anticoll()
                if status == self.rfid.OK: # 如果成功获取了UID
                    # 打印UID
                    print('Card UID:', uid)
                    return uid
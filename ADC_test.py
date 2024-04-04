from machine import Pin, ADC

class ADC_module(object):
    def __init__(self, NO, wv):
        self.pin=Pin(NO)
        self.adc = ADC(self.pin)
        self.wv = wv # This variable is the weight voltage rate
    
    def __str__(self):
        adc_value=adc.read()
        voltage = (adc_value * 3.3) / 4096
        return f"current voltage: {voltage}\n"
    
    def cal_reduction(self):
        adc_value=adc.read()
        voltage = (adc_value * 3.3) / 4096
        reduction = voltage / self.wv
        return reduction

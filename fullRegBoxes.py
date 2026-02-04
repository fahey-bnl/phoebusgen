import phoebusgen
import json

LBLLEN = 80

phoebusScreen = phoebusgen.screen.Screen("LLRF Digitizer")
with open('pvList.json', 'r') as f:
    params = json.load(f)

y = 10
height = 30*(len(params["ADC"]["regs"])+2)
for i in range(params["ADC"]["count"]):
    container = phoebusgen.widget.Group(f'ADC{i}', 20 + i*420, y, 410, height)
    tempY = 10
    for reg in params["ADC"]["regs"]:
        lblParam = phoebusgen.widget.Label(f'lblADC{i}{reg}', reg, 10, tempY, 140, 20)
        inpParam = phoebusgen.widget.TextEntry(f'inpADC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-ADC_CH{i}-{reg}', 162, tempY, 90, 20)
        rbParam = phoebusgen.widget.TextUpdate(f'rbADC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-ADC_CH{i}-{reg}-I', 262, tempY, 90, 20)
        inpParam.format("Hexadecimal")
        rbParam.format("Hexadecimal")
        container.add_widget([lblParam, inpParam, rbParam])
        tempY += 30
    phoebusScreen.add_widget(container)

y += height + 10
height = 30*(len(params["DAC"]["regs"])+2)
for i in range(params["DAC"]["count"]):
    container = phoebusgen.widget.Group(f'DAC{i}', 20 + i*420, y, 410, height)
    tempY = 10
    for reg in params["DAC"]["regs"]:
        lblParam = phoebusgen.widget.Label(f'DAC{i}{reg}', reg, 10, tempY, 140, 20)
        inpParam = phoebusgen.widget.TextEntry(f'inpDAC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-{reg}', 162, tempY, 90, 20)
        rbParam = phoebusgen.widget.TextUpdate(f'rbDAC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-{reg}-I', 262, tempY, 90, 20)
        inpParam.format("Hexadecimal")
        rbParam.format("Hexadecimal")
        container.add_widget([lblParam, inpParam, rbParam])
        tempY += 30
    phoebusScreen.add_widget(container)

y += height + 10
height = 30*(len(params["FIELD_CONTROLLER"]["regs"])+2)
for i in range(params["FIELD_CONTROLLER"]["count"]):
    container = phoebusgen.widget.Group(f'FC{i}', 20 + i*420, y, 410, height)
    tempY = 10
    for reg in params["FIELD_CONTROLLER"]["regs"]:
        lblParam = phoebusgen.widget.Label(f'FC{i}{reg}', reg, 10, tempY, 140, 20)
        inpParam = phoebusgen.widget.TextEntry(f'inpFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-FC_{i}-{reg}', 162, tempY, 90, 20)
        rbParam = phoebusgen.widget.TextUpdate(f'rbFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-FC_{i}-{reg}-I', 262, tempY, 90, 20)
        inpParam.format("Hexadecimal")
        rbParam.format("Hexadecimal")
        container.add_widget([lblParam, inpParam, rbParam])
        tempY += 30
    phoebusScreen.add_widget(container)

y += height + 10
height = 30*(len(params["RDBK_REGS"]["regs"])+2)
for i in range(params["RDBK_REGS"]["count"]):
    container = phoebusgen.widget.Group(f'FC{i}', 20 + i*420, y, 410, height)
    tempY = 10
    for reg in params["RDBK_REGS"]["regs"]:
        lblParam = phoebusgen.widget.Label(f'FC{i}{reg}', reg, 10, tempY, 140, 20)
        inpParam = phoebusgen.widget.TextEntry(f'inpFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-RDBK_REGS{i}-{reg}', 162, tempY, 90, 20)
        rbParam = phoebusgen.widget.TextUpdate(f'rbFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-RDBK_REGS{i}-{reg}-I', 262, tempY, 90, 20)
        inpParam.format("Hexadecimal")
        rbParam.format("Hexadecimal")
        container.add_widget([lblParam, inpParam, rbParam])
        tempY += 30
    phoebusScreen.add_widget(container)

phoebusScreen.write_screen("boxedScreen.bob")
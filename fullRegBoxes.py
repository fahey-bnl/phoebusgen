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

y += height + 10
height = 30*(len(params["MISC_INPUT"]["regs"])+2)
container = phoebusgen.widget.Group(f'MISC_INPUT', 20 + i*420, y, 410, height)
tempY = 10
for reg in params["MISC_INPUT"]["regs"]:
    lblParam = phoebusgen.widget.Label(f'FC{i}{reg}', reg, 10, tempY, 140, 20)
    inpParam = phoebusgen.widget.TextEntry(f'inpFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}MISC_INPUT-{reg}', 162, tempY, 90, 20)
    rbParam = phoebusgen.widget.TextUpdate(f'rbFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}MISC_INPUT-{reg}-I', 262, tempY, 90, 20)
    inpParam.format("Hexadecimal")
    rbParam.format("Hexadecimal")
    container.add_widget([lblParam, inpParam, rbParam])
    tempY += 30
phoebusScreen.add_widget(container)

y += height + 10

ulr = params["ULR_MODULE"]
pid = ulr["PID"]
ev  = ulr["EV"]

ulr_top_rows  = len(ulr["regs"])
pid_rows      = pid["count"] * len(pid["regs"])
ev_rows       = ev["count"]  * len(ev["regs"])

ulr_top_h = 30 * (ulr_top_rows + 2)
pid_h     = 30 * (pid_rows     + 2)
ev_h      = 30 * (ev_rows      + 2)

container_ulr = phoebusgen.widget.Group('ULR_TOP', 20, y, 410, ulr_top_h)
tempY = 10
for reg in ulr["regs"]:
    lbl = phoebusgen.widget.Label(f'lblULR{reg}', reg, 10, tempY, 140, 20)
    inp = phoebusgen.widget.TextEntry(f'inpULR{reg}',
          f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-{reg}', 162, tempY, 90, 20)
    rb  = phoebusgen.widget.TextUpdate(f'rbULR{reg}',
          f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-{reg}-I', 262, tempY, 90, 20)
    inp.format("Hexadecimal")
    rb.format("Hexadecimal")
    container_ulr.add_widget([lbl, inp, rb])
    tempY += 30
phoebusScreen.add_widget(container_ulr)

container_pid = phoebusgen.widget.Group('ULR_PID', 440, y, 410, pid_h)
tempY = 10
for i in range(pid["count"]):
    for reg in pid["regs"]:
        lbl = phoebusgen.widget.Label(f'lblULRPID{i}{reg}', f'PID{i}_{reg}', 10, tempY, 140, 20)
        inp = phoebusgen.widget.TextEntry(f'inpULRPID{i}{reg}',
              f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_DATA{i}-PID_{reg}', 162, tempY, 90, 20)
        rb  = phoebusgen.widget.TextUpdate(f'rbULRPID{i}{reg}',
              f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_DATA{i}-PID_{reg}-I', 262, tempY, 90, 20)
        inp.format("Hexadecimal")
        rb.format("Hexadecimal")
        container_pid.add_widget([lbl, inp, rb])
        tempY += 30
phoebusScreen.add_widget(container_pid)

container_ev = phoebusgen.widget.Group('ULR_EV', 860, y, 410, ev_h)
tempY = 10
for i in range(ev["count"]):
    for reg in ev["regs"]:
        lbl = phoebusgen.widget.Label(f'lblULREV{i}{reg}', f'EV{i}_{reg}', 10, tempY, 140, 20)
        inp = phoebusgen.widget.TextEntry(f'inpULREV{i}{reg}',
              f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_EV{i}-{reg}', 162, tempY, 90, 20)
        rb  = phoebusgen.widget.TextUpdate(f'rbULREV{i}{reg}',
              f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_EV{i}-{reg}-I', 262, tempY, 90, 20)
        inp.format("Hexadecimal")
        rb.format("Hexadecimal")
        container_ev.add_widget([lbl, inp, rb])
        tempY += 30
phoebusScreen.add_widget(container_ev)

phoebusScreen.write_screen("boxedScreen.bob")
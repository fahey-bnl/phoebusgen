import phoebusgen
import json

LBLLEN = 80

phoebusScreen = phoebusgen.screen.Screen("LLRF Digitizer")
with open('pvList.json', 'r') as f:
    params = json.load(f)

# Global Inputs
lblFrev = phoebusgen.widget.Label("lblFrev", "Frev:", 50,40,40,20)
txtFrev = phoebusgen.widget.TextEntry("txtFrev", "frev_input", 101, 40, 100, 20)

lblHarmNum = phoebusgen.widget.Label("lblHarmNum", "Harmonic #:", 230,40,81,20)
txtHarmNum = phoebusgen.widget.TextEntry("txtHarmNum", "harmnum_input", 330, 40, 100, 20)

phoebusScreen.add_widget([lblFrev, txtFrev, lblHarmNum, txtHarmNum])


# ADC Inputs
for i in range(params["ADC"]["count"]):
    container = phoebusgen.widget.Group(f'ADC{i}', 20 + i*210, 80, 200, 370)
    btnOnOff = phoebusgen.widget.BooleanButton(f'ADC_{i}onoff', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-ADC_CH{i}-CONTROL', 10, 10, 50, 40)
    ledOnOff = phoebusgen.widget.LED(f'ADC_{i}_onoff_indicator', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-ADC_CH{i}-CONTROL-I', 110, 20, 20, 20)
    
    lblPhaseOffset = phoebusgen.widget.Label(f'lblADC{i}PhaseOffset', "Phi Offset", 10, 60, 75, 20)
    txtPhaseOffset = phoebusgen.widget.TextEntry(f'txtADC{i}PhaseOffset', f'ADC{i}_PHASE_INPUT', 80, 60, 80, 20)

    lblI = phoebusgen.widget.Label(f'lblADC{i}I', 'I', 10, 142, 20, 20)
    lblQ = phoebusgen.widget.Label(f'lblADC{i}Q', 'Q', 10, 172, 20, 20)
    lblM = phoebusgen.widget.Label(f'lblADC{i}M', 'M', 10, 202, 20, 20)
    lblP = phoebusgen.widget.Label(f'lblADC{i}P', 'P', 10, 232, 20, 20)
    lblIErr = phoebusgen.widget.Label(f'lblADC{i}IErr', 'Err_I', 10, 272, 40, 20)
    lblQErr = phoebusgen.widget.Label(f'lblADC{i}QErr', 'Err_Q', 10, 312, 40, 20)
    
    txtI = phoebusgen.widget.TextUpdate(f'txtADC{i}I', f'$(P){{CPC:$(NO):DB$(DB)}}ADC_{i}_I', 80, 142, 80, 20)
    txtQ = phoebusgen.widget.TextUpdate(f'txtADC{i}Q', f'$(P){{CPC:$(NO):DB$(DB)}}ADC_{i}_Q', 80, 172, 80, 20)
    txtM = phoebusgen.widget.TextUpdate(f'txtADC{i}M', f'$(P){{CPC:$(NO):DB$(DB)}}ADC_{i}_M', 80, 202, 80, 20)
    txtP = phoebusgen.widget.TextUpdate(f'txtADC{i}P', f'$(P){{CPC:$(NO):DB$(DB)}}ADC_{i}_P', 80, 232, 80, 20)
    txtIErr = phoebusgen.widget.TextUpdate(f'txtADC{i}IErr', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-RDBK_REGS0-ADC_0_{i}_ERROR_I-I', 80, 272, 80, 20)
    txtQErr = phoebusgen.widget.TextUpdate(f'txtADC{i}QErr', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-RDBK_REGS0-ADC_0_{i}_ERROR_Q-I', 80, 312, 80, 20)
    
    container.add_widget([btnOnOff, ledOnOff, lblPhaseOffset, txtPhaseOffset, lblI, txtI, lblQ, txtQ, lblIErr, txtIErr, lblQErr, txtQErr, lblM, txtM, lblP, txtP])
    phoebusScreen.add_widget(container)

for i in range(params["DAC"]["count"]):
    container = phoebusgen.widget.Group(f'DAC{i}', 20 + i*210, 450, 200, 120)
    btnOnOff = phoebusgen.widget.BooleanButton(f'DAC_{i}onoff', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-CONTROL', 10, 10, 50, 40)
    ledOnOff = phoebusgen.widget.LED(f'DAC_{i}_onoff_indicator', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-CONTROL-I', 110, 20, 20, 20)
    lblDacHarm = phoebusgen.widget.Label(f'lblDAC{i}HarmonicNumber', "Harmonic #:", 10, 60, 80, 20)
    txtDacHarm = phoebusgen.widget.TextEntry(f'txtDAC{i}HarmonicNumber', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-HNUM', 100, 60, 60, 20)
    container.add_widget([btnOnOff, ledOnOff, lblDacHarm, txtDacHarm])
    phoebusScreen.add_widget(container)

for i in range(params["FIELD_CONTROLLER"]["count"]):
    container = phoebusgen.widget.Group(f'FC{i}', 20 + i*420, 570, 410, 10 + 30*(len(params["FIELD_CONTROLLER"]["regs"])+1))
    y = 10
    for reg in params["FIELD_CONTROLLER"]["regs"]:
        lblParam = phoebusgen.widget.Label(f'lblFC{i}{reg}', reg, 10, y, 140, 20)
        inpParam = phoebusgen.widget.TextEntry(f'inpFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-FC_{i}-{reg}', 162, y, 90, 20)
        rbParam = phoebusgen.widget.TextUpdate(f'rbFC{i}{reg}', f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-FC_{i}-{reg}-I', 262, y, 90, 20)
        container.add_widget([lblParam, inpParam, rbParam])
        y += 30
    phoebusScreen.add_widget(container)



phoebusScreen.write_screen("test.bob")
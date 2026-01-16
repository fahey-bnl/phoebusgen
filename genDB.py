import json
import phoebusgen.screen
import phoebusgen.widget

def writeDb(dbFile, pvReg, address):
    dbFile = f"""{dbFile}

record(longout, "{pvReg}"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Single I32")
    field(OUT, "@cpc$(NO) 1 {address}")
    field(FLNK, "$(P){{CPC:$(NO)}}GoRegSingleWrite1")
}}
record(longin, "{pvReg}-I"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Reg")
    field(INP, "@cpc$(NO) $(MSGID) {address - startOffset}")
    field(SCAN,"I/O Intr")
}}
    """
    return dbFile

def writePhoebus(phoebusScreen, pvReg, index):
    x = index*10
    getWidget = phoebusgen.widget.TextEntry(f"readBack{index}", pvReg, 160, x, 100, 20)
    getWidget.format("Hexadecimal")
    setWidget = phoebusgen.widget.TextUpdate(f'input{index}', f"{pvReg}-I", 270, x, 100, 20)
    setWidget.format("Hexadecimal")
    phoebusScreen.add_widget(phoebusgen.widget.Label(f"name{index}", pvReg, 10, x, 150, 20))
    phoebusScreen.add_widget(getWidget)
    phoebusScreen.add_widget(setWidget)
    return phoebusScreen
    
with open('pvList.json', 'r') as f:
    params = json.load(f)

startOffset = params["start_offset"]

fullDB = ""
index = 0

phoebusScreen = phoebusgen.screen.Screen("LLRF Digitizer")

address = params["ADC"]["start_offset"]
for i in range(params["ADC"]["count"]):
    for param in params["ADC"]["regs"]:
        pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-ADC_CH{i}-{param}'
        fullDB = writeDb(fullDB, pvReg, address)
        phoebusScreen = writePhoebus(phoebusScreen, pvReg, index)
        address += 4
        index += 1

address = params["DAC"]["start_offset"]
for i in range(params["DAC"]["count"]):
    for param in params["DAC"]["regs"]:
        pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-{param}'
        fullDB = writeDb(fullDB, pvReg, address)
        phoebusScreen = writePhoebus(phoebusScreen, pvReg, index)
        address += 4
        index += 1

address = params["FIELD_CONTROLLER"]["start_offset"]
for param in params["FIELD_CONTROLLER"]["regs"]:
    pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-FIELD_CONTROLLER-{param}'
    fullDB = writeDb(fullDB, pvReg, address)
    phoebusScreen = writePhoebus(phoebusScreen, pvReg, index)
    address+= 4
    index += 1

with open("dbautogen.db", "w") as f:
    f.write(fullDB)

phoebusScreen.write_screen("dbautogen.bob")
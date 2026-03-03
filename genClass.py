import phoebusgen
import json

class autogen:
    def __init__(self, name, startOffset):
        self.epicsDB = ""
        self.phoebusScreen = phoebusgen.screen.Screen(name)
        self.index = 0
        self.startOffset = startOffset
    
    def writeDb(self, pvReg, address):
        self.epicsDB = f"""{self.epicsDB}

record(longout, "{pvReg}"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Single I32")
    field(OUT, "@cpc$(NO) 1 {address}")
    field(FLNK, "$(P){{CPC:$(NO)}}GoRegSingleWrite1")
}}
record(longin, "{pvReg}-I"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Reg")
    field(INP, "@cpc$(NO) $(MSGID) {address - self.startOffset}")
    field(SCAN,"I/O Intr")
}}
        """

    def writePhoebus(self, pvReg):
        x = self.index*30
        getWidget = phoebusgen.widget.TextEntry(f"readBack{self.index}", pvReg, 820, x, 100, 20)
        getWidget.format("Hexadecimal")
        setWidget = phoebusgen.widget.TextUpdate(f'input{self.index}', f"{pvReg}-I", 930, x, 100, 20)
        setWidget.format("Hexadecimal")
        self.phoebusScreen.add_widget(phoebusgen.widget.Label(f"name{self.index}", pvReg, 10, x, 800, 20))
        self.phoebusScreen.add_widget(getWidget)
        self.phoebusScreen.add_widget(setWidget)
        self.index += 1
    
    def export(self, dbPath, bobPath):
        with open(dbPath, "w") as f:
            f.write(self.epicsDB)
        self.phoebusScreen.write_screen(bobPath)

def main():
    
    with open('pvList.json', 'r') as f:
        params = json.load(f)
    
    dbs = autogen("LLRF Digitizer", params["start_offset"])
    
    address = params["ADC"]["start_offset"]
    for i in range(params["ADC"]["count"]):
        for param in params["ADC"]["regs"]:
            pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-ADC_CH{i}-{param}'
            dbs.writeDb(pvReg, address)
            dbs.writePhoebus(pvReg)
            address += 4
    
    address = params["DAC"]["start_offset"]
    for i in range(params["DAC"]["count"]):
        for param in params["DAC"]["regs"]:
            pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-{param}'
            dbs.writeDb(pvReg, address)
            dbs.writePhoebus(pvReg)
            address += 4

    address = params["FIELD_CONTROLLER"]["start_offset"]
    for i in range(params["FIELD_CONTROLLER"]["count"]):
        for param in params["FIELD_CONTROLLER"]["regs"]:
            pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-FC_{i}-{param}'
            dbs.writeDb(pvReg, address)
            dbs.writePhoebus(pvReg)
            address += 4

    address = params["RDBK_REGS"]["start_offset"]
    for i in range(params["RDBK_REGS"]["count"]):
        for param in params["RDBK_REGS"]["regs"]:
            pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-RDBK_REGS{i}-{param}'
            dbs.writeDb(pvReg, address)
            dbs.writePhoebus(pvReg)
            address += 4

    address = params["ULR_MODULE"]["start_offset"]
    for param in params["ULR_MODULE"]["regs"]:
        pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-{param}'
        dbs.writeDb(pvReg, address)
        dbs.writePhoebus(pvReg)
        address += 4
    for i in range(params["ULR_MODULE"]["PID"]["count"]):
        for param in params["ULR_MODULE"]["PID"]["regs"]:
            pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_DATA{i}-PID_{param}'
            dbs.writeDb(pvReg, address)
            dbs.writePhoebus(pvReg)
            address += 4
    for i in range(params["ULR_MODULE"]["EV"]["count"]):
        for param in params["ULR_MODULE"]["EV"]["regs"]:
            pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_EV{i}-{param}'
            dbs.writeDb(pvReg, address)
            dbs.writePhoebus(pvReg)
            address += 4

    dbs.export("genClass.db", "genClass.bob")

if __name__ == "__main__":
    main()


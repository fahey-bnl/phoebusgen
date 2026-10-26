import phoebusgen
import json

comOffset = 0 #0x0000
bspOffset = 524304 #0x80010
appOffset = 786432 #0xC0000
bramOffset = 917504 #0xE0000
maxOffset = 65535

class autogen:
    def __init__(self, name, startOffset):
        self.epicsDB = ""
        self.phoebusScreen = phoebusgen.screen.Screen(name)
        self.index = 0
        self.startOffset = startOffset

    def writeDb(self, pvReg, address, rw):
        if 'R' in rw:
            self.epicsDB = f"""{self.epicsDB}
    
record(longout, "{pvReg}"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Single I32")
    field(OUT, "@cpc$(NO) 1 {address}")
    field(FLNK, "$(P){{CPC:$(NO)}}GoRegSingleWrite1")
}}
            """
        if 'W' in rw:
            self.epicsDB = f"""{self.epicsDB}
record(longin, "{pvReg}-I"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Reg")
    field(INP, "@cpc$(NO) $(MSGID) {address - self.startOffset}")
    field(SCAN,"I/O Intr")
}}
            """

    def writePhoebus(self, pvReg, rw):
        x = self.index*30
        getWidget = phoebusgen.widget.TextEntry(f"readBack{self.index}", pvReg, 820, x, 100, 20)
        getWidget.format("Hexadecimal")
        setWidget = phoebusgen.widget.TextUpdate(f'input{self.index}', f"{pvReg}-I", 930, x, 100, 20)
        setWidget.format("Hexadecimal")
        self.phoebusScreen.add_widget(phoebusgen.widget.Label(f"name{self.index}", pvReg, 10, x, 800, 20))
        if 'R' in rw: self.phoebusScreen.add_widget(getWidget)
        if 'W' in rw: self.phoebusScreen.add_widget(setWidget)
        self.index += 1
    
    def export(self, dbPath, bobPath):
        with open(dbPath, "w") as f:
            f.write(self.epicsDB)
        self.phoebusScreen.write_screen(bobPath)

def main():
    
    with open('autoPV.json', 'r') as f:
        params = json.load(f)
    
    comDb = autogen("Common Registers", comOffset)
    bspDb = autogen("BSP Registers", bspOffset)
    appDb = autogen("APP Registers", appOffset)
    
    for key in params:
        for param in params[key]:
            if param['address'] >= bramOffset: continue
            elif param['address'] >= appOffset:
                appDb.writeDb(param['pv_name'], param['address'], param['rw'])
                appDb.writePhoebus(param['pv_name'], param['rw'])
            elif param['address'] >= bspOffset:
                bspDb.writeDb(param['pv_name'], param['address'], param['rw'])
                bspDb.writePhoebus(param['pv_name'], param['rw'])
            else:
                comDb.writeDb(param['pv_name'], param['address'], param['rw'])
                comDb.writePhoebus(param['pv_name'], param['rw'])
            
    comDb.export("genCOM.db", "genCOM.bob")
    appDb.export("genAPP.db", "genAPP.bob")
    bspDb.export("genBSP.db", "genBSP.bob")

if __name__ == "__main__":
    main()


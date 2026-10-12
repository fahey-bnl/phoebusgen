import phoebusgen
import json

appOffset = 786432 #0xC0000
maxOffset = 65535

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
    
    with open('autoPV.json', 'r') as f:
        params = json.load(f)
    
    dbs = autogen("LLRF Digitizer", appOffset)
    
    for key in params:
        for param in params[key]:
            offset = param['address'] - appOffset
            if offset < 0 or offset > maxOffset: continue
            dbs.writeDb(param['pv_name'], param['address'])
            dbs.writePhoebus(param['pv_name'])

    dbs.export("genClass.db", "genClass.bob")

if __name__ == "__main__":
    main()


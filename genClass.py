import phoebusgen

class autogen:
    def __init__(self, name):
        self.epicsDB = ""
        self.phoebusScreen = phoebusgen.screen.Screen(name)
        self.index = 0
    
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
    field(INP, "@cpc$(NO) $(MSGID) {address - startOffset}")
    field(SCAN,"I/O Intr")
}}
        """

    def writePhoebus(self, pvReg):
        x = self.index*10
        getWidget = phoebusgen.widget.TextEntry(f"readBack{index}", pvReg, 160, x, 100, 20)
        getWidget.format("Hexadecimal")
        setWidget = phoebusgen.widget.TextUpdate(f'input{index}', f"{pvReg}-I", 270, x, 100, 20)
        setWidget.format("Hexadecimal")
        self.phoebusScreen.add_widget(phoebusgen.widget.Label(f"name{index}", pvReg, 10, x, 150, 20))
        self.phoebusScreen.add_widget(getWidget)
        self.phoebusScreen.add_widget(setWidget)
        self.index += 1
    
    def export(self, dbPath, bobPath):
        with open(dbPath, "w") as f:
            f.write(self.epicsDB)
        self.phoebusScreen.write_screen(bobPath)

def main():
    dbs = autogen("LLRF Digitizer")
    print("test")

if __name__ == "__main__":
    main()


import json
import phoebusgen.screen
import phoebusgen.widget

with open('pvList.json', 'r') as f:
    params = json.load(f)

fullDB = ""
currentOffset = params["start"]
pvs = []

phoebusScreen = phoebusgen.screen.Screen("LLRF Digitizer")

for i in range(params["ADC"]["count"]):
    for param in params["ADC"]["regs"]:
        pvReg = f'$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-ADC_CH{i}-{param}'
        fullDB = f"""{fullDB}

record(longout, "{pvReg}"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Single I32)
    field(OUT, "@cpc$(NO) 1 {params["offset"] + currentOffset}")
    field(FLNK, "$(P){{CPC:$(NO)}}GoRegSingleWrite1")
}}
record(longin, "{pvReg}-I"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Reg")
    field(INP, "@cpc$(NO) $(MSGID) {currentOffset}")
    field(SCAN,"I/O Intr")
}}
        """
        x = (currentOffset-params["start"])*10
        phoebusScreen.add_widget(phoebusgen.widget.Label(f"name{currentOffset}", f"ADC{i}-{param}", 10, x, 150, 20))
        phoebusScreen.add_widget(phoebusgen.widget.TextUpdate(f"readBack{currentOffset}", pvReg, 160, x, 100, 20))
        phoebusScreen.add_widget(phoebusgen.widget.TextEntry(f'input{currentOffset}', f"{pvReg}-I", 270, x, 100, 20))
        currentOffset += 4


for i in range(params["DAC"]["count"]):
    for param in params["DAC"]["regs"]:
        fullDB = f"""{fullDB}

record(longout, "$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-{param}"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Single I32)
    field(OUT, "@cpc$(NO) 1 {params["offset"] + currentOffset}")
    field(FLNK, "$(P){{CPC:$(NO)}}GoRegSingleWrite1")
}}
record(longin, "$(P){{CPC:$(NO):DB$(DB)}}APP_REGS-DAC_CH{i}-{param}-I"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Reg")
    field(INP, "@cpc$(NO) $(MSGID) {currentOffset}")
    field(SCAN,"I/O Intr")
}}
        """
        x = (currentOffset-params["start"])*10
        phoebusScreen.add_widget(phoebusgen.widget.Label(f"name{currentOffset}", f"DAC{i}-{param}", 10, x, 150, 20))
        phoebusScreen.add_widget(phoebusgen.widget.TextUpdate(f"readBack{currentOffset}", pvReg, 160, x, 100, 20))
        phoebusScreen.add_widget(phoebusgen.widget.TextEntry(f'input{currentOffset}', f"{pvReg}-I", 270, x, 100, 20))
        currentOffset += 4

with open("dbautogen.db", "w") as f:
    f.write(fullDB)

phoebusScreen.write_screen("dbautogen.bob")
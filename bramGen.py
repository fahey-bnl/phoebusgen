import phoebusgen

regCount = 16
regDepth = 1024
regBytes = 4

phoebusScreen = phoebusgen.screen.Screen("LLRF Digitizer BRAM")
fullDB = ''

y = 10

for i in range(regCount):
    pv = f'$(P){{CPC:$(NO):DB$(DB)}}BRAM_BANK_{i}-I'
    fullDB += f'''
record(waveform, "{pv}"){{
    field(DTYP, "PSC Block I32 In")
    field(INP , "@cpc$(NO) $(MSGID) {i * (regDepth*regBytes)}")
    field(SCAN, "I/O Intr")
    field(FTVL, "LONG")
    field(NELM, {regDepth})
}}
'''
    graph = phoebusgen.widget.StripChart(10, y, 800, 160)
    
with open("dbbram.db", 'w') as f:
    f.write(fullDB)
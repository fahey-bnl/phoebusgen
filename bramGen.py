regCount = 16
regDepth = 1024
regBytes = 4

fullDB = ''

for i in range(regCount):
    fullDB += f'''
record(waveform, "$(P){{CPC:$(NO):DB$(DB)}}BRAM_BANK_{i}-I){{
    field(DTYP, "PSC Block I32 In")
    field(INP , "@cpc$(NO) $(MSGID) {i * (regDepth*regBytes)}")
    field(SCAN, "I/O Intr")
    field(FTVL, "LONG")
    field(NELM, {regDepth})
}}

'''
with open("dbbram.db", 'w') as f:
    f.write(fullDB)
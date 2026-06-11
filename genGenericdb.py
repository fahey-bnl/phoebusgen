startAddress = 40
offset = 768432

regCnt = 32

pvName = "$(P){CPC:$(NO):DB$(DB)}APP_REGS-"
fullDb = ""
addr = startAddress

for i in range(regCnt):
    fullDb = f'''{fullDb}
record(longout, "{pvName}REG{i}){{
    field(DESC, "TEST")
    field(DTYP, "PSC SINGLE I32")
    field(OUT,  "@cpc$(NO) 3 {addr + offset}")
    field(FLNK, "$(P){{CPC:$(NO)}}GoRegSingleWrite1")
}}
record(longin, "{pvName}REG{i}-I"){{
    field(DESC, "TEST")
    field(DTYP, "PSC Reg")
    field(INP, "@cpc$(NO) $(MSGID) {addr}")
    field(SCAN,"I/O Intr")
}}
'''
    addr += 4
    
print(fullDb)
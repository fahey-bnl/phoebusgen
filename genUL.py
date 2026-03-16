import phoebusgen
import json

LBLLEN = 80

phoebusScreen = phoebusgen.screen.Screen("LLRF Digitizer Update Link")
with open('pvList.json', 'r') as f:
    params = json.load(f)

# General Inputs
lblControl = phoebusgen.widget.Label("lblControl", "Control:", 50,40,50,20)
txtControl = phoebusgen.widget.TextEntry("txtControl", "$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-CONTROL", 110, 40, 100, 20)
txtControl.format("Hexadecimal")

lblStatus = phoebusgen.widget.Label("lblStatus", "Status:", 230,40,50,20)
txtStatus = phoebusgen.widget.TextUpdate("txtStatus", "$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-STATUS-I", 290, 40, 100, 20)
txtStatus.format("Hexadecimal")

lblTx = phoebusgen.widget.Label("lblTx", "TX:", 410,40,40,20)
txtTx = phoebusgen.widget.TextEntry("txtTx", "$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_TX", 470, 40, 100, 20)
txtTx.format("Hexadecimal")

phoebusScreen.add_widget([lblControl, txtControl, lblStatus, txtStatus, lblTx, txtTx])

# PIDs
for i in range(params["ULR_MODULE"]["PID"]["count"]):
    container = phoebusgen.widget.Group(f'PID {i}', 20 + i*210, 80, 200, 130)

    lblAddr = phoebusgen.widget.Label(f'lblPID{i}Addr', "Address:", 10, 10, 60, 20)
    txtAddr = phoebusgen.widget.TextEntry(f'txtPID{i}Addr', f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_DATA{i}-PID_ADDR', 80, 10, 80, 20)
    txtAddr.format("Hexadecimal")
    txtAddrRdbk = phoebusgen.widget.TextUpdate(f'txtPID{i}AddrRdbk', f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_DATA{i}-PID_ADDR-I', 80, 40, 80, 20)
    txtAddrRdbk.format("Hexadecimal")

    lblData = phoebusgen.widget.Label(f'lblPID{i}Data', 'Data', 10, 70, 40, 20)
    txtData = phoebusgen.widget.TextUpdate(f'txtPID{i}Data', f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_DATA{i}-PID_DATA-I', 80, 70, 80, 20)
    txtData.format("Hexadecimal")

    container.add_widget([lblAddr, txtAddr, txtAddrRdbk, lblData, txtData])
    phoebusScreen.add_widget(container)

for i in range(params["ULR_MODULE"]["EV"]["count"]):
    container = phoebusgen.widget.Group(f'EV {i}', 20 + i*210, 220, 200, 70)

    txtEid = phoebusgen.widget.TextUpdate(f'txtEV{i}', f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_EV{i}-EID-I', 10, 10, 70, 20)
    txtEid.format("Hexadecimal")
    txtEidRdbk = phoebusgen.widget.TextEntry(f'txtEV{i}Rdbk', f'$(P){{CPC:$(NO):DB$(DB)}}ULR_MODULE-UL_EV{i}-EID-I', 90, 10, 70, 20)
    txtEidRdbk.format("Hexadecimal")

    container.add_widget([txtEid, txtEidRdbk])
    phoebusScreen.add_widget(container)

phoebusScreen.write_screen("test.bob")
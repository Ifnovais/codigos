import py_dss_interface

#OpenDSS obj

dss = py_dss_interface.DSSDLL()

dss_file = r"C:\Program Files\OpenDSS\IEEETestCases\123Bus\IEEE123Master.dss"

dss.text("compile [{}]".format(dss_file))
dss.text("Buscoords Buscoords.dat")

dss.solution_solve()

vmag_list = dss.circuit_all_bus_vmag_pu()
node_list = dss.circuit_all_node_names()

vmin = min(vmag_list)
vmin_index = vmag_list.index(vmin)
bus_node = node_list[vmin_index]
bus = bus_node.split(".")[0]

color = "Green"
size_marker = 8
code = 15

dss.text("AddBusMarker bus={} color={} size={} code={}".format(bus, color, size_marker, code))
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")
print("")

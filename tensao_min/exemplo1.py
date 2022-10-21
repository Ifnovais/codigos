import py_dss_interface

#OpenDSS obj

dss = py_dss_interface.DSSDLL()

dss_file = r"C:\Program Files\OpenDSS\IEEETestCases\8500-Node\Master-unbal.dss"
dss.text("compile [{}]".format(dss_file))

dss.text("New Energymeter.m1 Line.ln5815900-1 1")
dss.text("Set Maxiterations=20")

dss.solution_solve()

print("")
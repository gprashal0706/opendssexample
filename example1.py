import py_dss_interface

dss = py_dss_interface.DSSDLL(r"C:\Program Files\OpenDSS")


dss_file = r"F:\33\ieee334.dss"

dss.text(f"compile [{dss_file}]")



dss.solution_solve()

dss.text("Show Voltage LN")

dss_file= 



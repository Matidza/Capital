
import os
if os.path.exists("ok.txt"):
    os.remove("ok.txtx")
else:
    print("Thge file does not exist")
# Copyright 2020 The MathWorks, Inc.

from os import environ
import subprocess
if "MLM_LICENSE_FILE" in environ:
  subprocess.check_call("matlab")
else :
  subprocess.check_call(["matlab", "-desktop", "-licmode", "online"])

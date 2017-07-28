#!/usr/bin/env python


import os, sys
import subprocess
import shutil

if 
# Map of folder names to repository locations
repositories = {
  "dials":          "https://github.com/dials/dials.git",
  "cctbx_project":  "https://github.com/cctbx/cctbx_project.git",
  "cbflib":         "https://github.com/yayahjb/cbflib.git",
  "ccp4io":         "https://github.com/dials/ccp4io.git",
  "xia2":           "https://github.com/xia2/xia2.git",
  "annlib_adaptbx": "https://github.com/dials/annlib_adaptbx.git",
  "annlib":         "https://github.com/dials/annlib.git",
  "ccp4io_adaptbx": "https://github.com/dials/ccp4io_adaptbx.git",
  "tntbx":          "https://github.com/dials/tntbx.git",
  "gui_resources":  "https://github.com/dials/gui_resources.git",
}

for name, url in repositories.items():
  # Assume that if the path exists at all, the user knows what they are doing
  if os.path.exists(name):
    continue

  subprocess.check_call(["git", "clone", "--depth=1", url])

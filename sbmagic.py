from __future__ import print_function
from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)

import subprocess as sp
import os
import sys
from uuid import uuid4

@register_line_magic
def sb(*args):
   print(sp.check_output(["sb"] + list(args)))

del sb

@register_cell_magic
def sb(arg, cell_content):
    if arg == "run":
        job_name = "sb_magic_job-%s.py" % str(uuid4())[:13]
        try:
            print(cell_content,file=open(job_name,"w"))
            p = sp.Popen(["sb", "run", "python", job_name],
                         stdout=sp.PIPE, bufsize=1)
            for line in iter(p.stdout.readline, b''):
                print(line,end='')
            p.communicate()
        finally:
            try:
                os.remove(job_name)
            except OSError:
                pass
            try:
                sp.check_call(["sb", "rm", job_name])
            except:
                pass

# We delete these to avoid name conflicts for automagic to work
del sb

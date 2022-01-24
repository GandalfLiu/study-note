# -*- coding: utf-8 -*-
import subprocess
from P4 import P4
import re
import re

from view import fun
p4 = P4()
p4.user = "p4admin"
p4.password = "pass12349ers!"
p4.port = "81.68.87.21:1666"
p4.client = "main1"

def init_cmd(params):
    cmd = ["p4", "-u", "p4admin", "-p", "81.68.87.21:1666", "-P", "pass12349ers!", "-c", "main1"]
    for param in params:
        cmd.append(param)
    fun()
    return cmd



cmd1 = ["add", r"c:\main1\heh\ccc.txt"]
cmd2 = ["add", r"c:\main1\move.txt"]
cmd3 = ["submit", "-d", "submit with code", "--parallel=0", "-f", "revertunchanged", "//LGame/trunk/main/heh/..."]

cmd1 = init_cmd(cmd1)
cmd2 = init_cmd(cmd2)
cmd3 = init_cmd(cmd3)

a = subprocess.Popen(cmd1, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
print(a.communicate()[0])

print(a.communicate()[1])
b = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(b.communicate()[0])
print(b.communicate()[1])
res = subprocess.Popen(cmd3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = res.communicate()

print(out)
print(err)


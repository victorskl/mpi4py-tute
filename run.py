from subprocess import Popen

p = Popen("run.bat")
stdout, stderr = p.communicate()
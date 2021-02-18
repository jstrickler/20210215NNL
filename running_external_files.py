from subprocess import run, PIPE, CalledProcessError
import shlex

cmd = "netstat -an"

cmd_list = shlex.split(cmd)

proc = run(cmd, stdout=PIPE)
print(proc.returncode)
output = proc.stdout.decode()  # convert output from bytes to str
output_lines = output.splitlines()
for line in output_lines:
    if 'ESTABLISH' in line:
        proto, local, remote, _ = line.split()
        print("{} {:20s} {}".format(proto, local, remote))
print("output had", len(output_lines), "lines")

# windows
# run(cmd)

# Mac/Linux
# run(cmd, shell=True)
# run(cmd_list)
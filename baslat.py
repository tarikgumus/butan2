import subprocess
from time import sleep

i=0

while 1:
    subprocess.run(["./xmrig --algo=ghostrider --url stratum-na.rplant.xyz:17075 --tls --user BnJkjVKDBvJbYEnXqMTKhX1gKFWyFtkUgq.neverlose -t 1 -k"],shell=True)
    sleep(20)

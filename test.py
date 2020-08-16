from datetime import datetime
import os

now = datetime.now()
frmtnow = now.strftime("%Y%m%d%H%M%S")
filename = 'bandit_test_' + frmtnow + '.json'
command = 'bandit -f json -o ./test/output/' + filename + ' -c ./test/bandit.cfg -r ./'

os.system(command)
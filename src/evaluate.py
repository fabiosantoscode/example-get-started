import sys
import os
import pickle
import json
import random

from sklearn.metrics import precision_recall_curve
import sklearn.metrics as metrics

#

if len(sys.argv) != 5:
    sys.stderr.write('Arguments error. Usage:\n')
    sys.stderr.write('\tpython evaluate.py model features scores plots\n')
    sys.exit(1)

model_file = sys.argv[1]
matrix_file = os.path.join(sys.argv[2], 'test.pkl')
scores_file = sys.argv[3]
plots_file = sys.argv[4]

big_keys = { f'k_{random.randint(0, 10000)}': random.randint(0, 30000) for _ in range(1000) }

with open(scores_file, 'w') as fd:
    json.dump(big_keys, fd)

with open(plots_file, 'w') as fd:
    json.dump(big_keys, fd)

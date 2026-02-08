#!/usr/bin/env python3


import json
import os
import re
import subprocess
import sys


CYAN = '\033[36m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'

LINK = '\033]8;;'


data = json.load(sys.stdin)


model_name = data['model']['display_name']

context_percentage = int(data.get('context_window', {}).get('used_percentage', 0) or 0)
context_filled = context_percentage * 10 // 100
context_bar = '▓' * context_filled + '░' * (10 - context_filled)
context_bar_color = RED if context_percentage >= 90 else YELLOW if context_percentage >= 60 else GREEN

model_status = f'🧠 {model_name} {context_bar_color}{context_bar}{RESET} {context_percentage}%'

total_cost = data.get('cost', {}).get('total_cost_usd', 0) or 0
duration_ms = data.get('cost', {}).get('total_duration_ms', 0) or 0

duration_sec = duration_ms // 1000
duration_min = duration_sec // 60
duration_sec = duration_sec % 60

cost_status = f'💰 ${total_cost:.2f} | ⏱️ {duration_min}m {duration_sec}s'


directory = os.path.basename(data['workspace']['current_dir'])

try:
    command = ('git', 'remote', 'get-url', 'origin')
    remote_url = subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL).strip()
    remote_url = re.sub(r'^git@github\.com:', 'https://github.com/', remote_url)
    remote_url = re.sub(r'\.git$', '', remote_url)
    directory = f'{LINK}{remote_url}\a{directory}{LINK}\a'
except Exception:
    pass

directory_status = f'📁 {directory}'

try:
    command = ('git', 'branch', '--show-current')
    branch = subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL).strip()
    if not branch:
        raise ValueError
except Exception:
    branch = '(none)'

branch_status = f'🌿 {branch}'


status_items = (model_status, cost_status, directory_status, branch_status)

print(' | '.join(status_items))

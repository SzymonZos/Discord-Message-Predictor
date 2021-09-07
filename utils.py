from datetime import datetime


def get_date():
    date = str(datetime.now())
    for char in [' ', '-', '.', ':']:
        date = date.replace(char, '_')
    return date


def dump_msgs(member, logs):
    user = str(member).replace('#', '_')
    log_file = f'logs/msg_{user}_date_{get_date()}.txt'
    with open(log_file, 'w', encoding="utf-8") as f:
        f.write('\n'.join(logs))

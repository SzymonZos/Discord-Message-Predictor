from datetime import datetime
import aiofiles


async def get_date():
    date = str(datetime.now())
    for char in [' ', '-', '.', ':']:
        date = date.replace(char, '_')
    return date


async def dump_msgs(member, logs):
    user = str(member).replace('#', '_')
    log_file = f'logs/msg_{user}_date_{await get_date()}.txt'
    async with aiofiles.open(f'{log_file}', mode='w', encoding="utf-8") as f:
        await f.write('\n'.join(logs))

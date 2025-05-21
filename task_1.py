
form_time = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0
clean_parts = []

for part in form_time.split(','):
    sub_parts = part.split()
    clean_parts.extend(sub_parts)

for time in clean_parts:
    if 'h' in time:
        total_minutes += int(time.replace('h', '')) * 60
    elif 's' in time:
        total_minutes += int(time.replace('s', '')) // 60
    else:
        total_minutes += int(time.replace('m', ''))


print(total_minutes)
from datetime import datetime
def avg_power(file):
  with open(file) as f:
    total_energy = 0
    i = 0
    next(f) # Skip first line header
    last_time = ""
    for line in f.readlines():
      now_time = datetime.strptime(line.strip().split(',')[0], '%H:%M:%S:%f')
      power = line.strip().split(',')[5]
      inst_power = power.strip('W')
      if last_time != "":
        #datetime.combine(date.min, end) - datetime.combine(date.min, beginning)
        deltime = (now_time - last_time).total_seconds()
        total_energy += (float(inst_power))*deltime #, multiply by 0.01 to get J  (10ms per log)
      last_time = now_time
  print(f'Total energy consumption (J) for file {file} : {total_energy}')
  return total_energy
def avg_hashrate(file):
  with open(file) as f:
    total_hash = 0
    i = 0
    for line in f.readlines():
      if line[0:6] != "STATUS":
        continue
      total_hash += int(" ".join(line.split()).split()[3])
      i += 1
    print(f"Average hash speed (MHash/s) for {file} : {total_hash/i/10**6}")
    return (total_hash/10**6, i)
rules = ['best64','d3ad0ne','dive','rockyou-30000','unix-ninja-leetspeak']
for rule in rules:
  hashrate, sec = avg_hashrate(f'./hashcatlog-{rule}.txt')
  print(f"total Mhashes: {hashrate}")
  power = avg_power(f'./powerlog-{rule}.txt')
  print(f"total power: {power}")
  print(f"Average hash rate per joule (Mpwd/J) {hashrate / power}")
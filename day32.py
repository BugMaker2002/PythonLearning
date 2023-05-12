import re
s = '01234567'

# 从直观上来说s不应该匹配到r，但若不设置边界匹配,就会匹配成功
r = '[1-9][0-9]{1,4}'
print(re.findall(r, s))
# 设置边界匹配
r2 = '^[1-9][0-9]{1,4}$'
print(re.findall(r2, s))

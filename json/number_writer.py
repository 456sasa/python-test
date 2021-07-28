import json

numbers = [2,3,5,7,11,13]
file_name='json\\numbers.json' 
#  '\'是Python的转义字符，如果路径中存在'\t'或者'\r'这样的特殊字符，
#   '\'就无法起到目录跳转的作用，因此报错。解决办法就是告诉系统'\'不是转义字符，'\\'就起这种作用，现给出一个示例。

with open(file_name,'w') as f:
    json.dump(numbers,f)
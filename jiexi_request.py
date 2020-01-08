import requests
import sys

argtest=sys.argv[1] #需要进行测试的参数
argvalue=sys.argv[2] #参数值，即poc
txtpath=sys.argv[3] #txt-request路径

with open(str(txtpath), 'r') as f1:
    str = f1.readlines()
str1=[]
for i in str:
    if i!='\n':
        str1.append(i.strip('\n'))
    else:
        flag=str.index(i)
method=str1[0].split(' ')[0]
path=str1[0].split(' ')[1]
if argtest=="hhddj":
    arg=''.join(str[flag+1:])#需要再想想，万一有换行符
else:
    arg = str1[-1].split('&')
header1,header2,headers=[],[],[]
arg1,arg2,args=[],[],[]
if method=='POST':
    header=str1[1:flag]
    for i in header:
        header1.append(i.split(': ')[0])
        header2.append(i.split(': ')[1])
    headers=dict(zip(header1,header2))
    if argtest=="hhddj":
        args=arg.replace("hhddj",argvalue)
    else:
        for i in arg:
            arg1.append(i.split('=')[0])
            aarg2.append(i.split('=')[1])
        args = dict(zip(arg1, arg2))
        args[argtest] = argvalue
    host=headers['Host']
    headers.pop('Host')
    url = 'http://' + host + path
    res=requests.post(url, headers=headers,data=args)
    print(res.text)
elif method=='GET':
    header = str1[1:]
    for i in header:
        header1.append(i.split(': ')[0])
        header2.append(i.split(': ')[1])
    headers = dict(zip(header1, header2))
    param=path.split('?')[1].split('&')
    param1,param2,params=[],[],[]
    for i in param:
        param1.append(i.split('=')[0])
        param2.append(i.split('=')[1])
    params=dict(zip(param1,param2))
    try:
        params[argtest] = argvalue
    except:
        print("参数不存在！使用原数据包发送！")
    host=headers['Host']
    headers.pop('Host')
    url = 'http://' + host + path.split('?')[0]
    res=requests.get(url,headers=headers,params=params)
    print(res.text)
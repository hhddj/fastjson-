# 检测fastjson漏洞



### 可修改文件

- 1.txt：burp数据包
- test.jar：检测jar包
- jiexi_request.py：解析1.txt并发送，可根据实际环境自行修改
  - get
  - post
    - xml
    - json
    - form

### 使用

```
java -jar test.jar
```

![shili](https://tva1.sinaimg.cn/large/006tNbRwly1gap2ldgxd7j31gq0nkgt8.jpg)

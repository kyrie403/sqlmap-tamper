# sqlmap-tamper


Bypass SafeDog V4.0


Version: 1.0


Date: 2018-04-18


Author: Kyrie403


Copyright (c) Kyrie403


GitHub: https://github.com/kyrie403





# Requirements

MYSQL > 5.0

SafeDog V4.0





# Usage:
```
python sqlmap.py -u http://test.com/test.php?id=1 --tamper=bypasssafedogv4 --random-agent --dbms MYSQL --delay=0.5
```

安全狗V4.0会根据User-Agent拦截sqlmap, 所以需要加上参数--random-agent; 访问过于频繁也会被拦截, --delay=0.5





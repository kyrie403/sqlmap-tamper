# sqlmap-tamper
sqlmap bypass tamper


version: 1.0

Author: Kyrie403

copyright (c) Kyrie403

link: https://github.com/kyrie403





# Requirements

MYSQL > 5.0

SafeDog V4.0





# Usage:
```
python sqlmap.py -u http://test.com/test.php?id=1 --tamper=bypasssafedogv4 --random-agent --dbms MYSQL --delay=0.5
```

安全狗V4.0会根据User-Agent拦截sqlmap, 所以需要加上参数--random-agent, 访问过于频繁也会被拦截, --delay=0.5





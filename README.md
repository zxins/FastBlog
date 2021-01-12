#### Model同步到数据库
```
1. 修改 alembic.ini 配置文件, sqlalchemy.url 选项;
2. 修改 alembic/env.py, target_metadata = [XXModel.Base.metadata, ...]
```

##### 执行命令
```
$ alembic revision --autogenerate -m "【本次提交描述】"
$ alembic upgrade head
```
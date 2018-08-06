## MySQL基础命令
1. 进入 `mysql -uroot -pqwe123`
2. 创建用户 `create user 'test28'@'%' identified by 'qwe123`
    1. '%'表示这个用户可以从远程登录
3. 赋予权限 `grant all on *.* to 'test28'@'%'`
    1. 第一个`*`表示所有数据库, 第二个`*`表示所有表
4. 使赋予的权限立即生效 `flush privileges`
5. 查看当前用户 `select user()`
6. 查看当前数据库 `select database()`
7. 查看所有数据库 `show databases`
8. 创建数据库 `create database [if not exists] db_name`
9. 使用数据库 `use db_name`
10. 删除数据库 `drop database [if exists] db_name`
11. 创建表 `create table [if ont exists] table_name(column_name data_type(length), ...)`
    1. 整型 int(默认11位)
    2. 不定长 varchar 最长65535
    3. 定长 char 最长255
    4. 双精度 double(4,2)
    5. 可变长度 text 最多65535
    6. 时间 datetime
    7. 枚举 enum
12. 查看有那些表 `show tables`
13. 查看表结构
    1. `describe table_name`
    2. `show create table table_name`
14. 删除表 `drop table table_name`
15. 查询 `select * from table_name`
16. 增加数据
    1. `insert into table_name value(...)`
    2. `insert into table_name value(...),(...)`
    3. `insert into table_name (id, sex) value(2, 'male')`
17. 更新数据
    1. `update table_name set name = 'a' where xxx`
18. 删除数据
    1. `delete from table_name where xxx`

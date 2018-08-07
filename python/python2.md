## MySQL基础命令
1. 进入 `mysql -uroot -pqwe123 -hlocalhost -P3306`
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
    2. `desc table_name`
    3. `show create table table_name`
14. 删除表 `drop table table_name`
15. `select`查询
    1. `select * from table_name`
16. `insert`增加数据
    1. `insert into table_name value(...)`
    2. `insert into table_name value(...),(...)`
    3. `insert into table_name (id, sex) value(2, 'male')`
17. `update`更新数据
    1. `update table_name set name = 'a' where xxx`
18. `delete`删除数据
    1. `delete from table_name where xxx`
19. `alter`修改字段和键
    1. 修改表名 `alter table tbName rename to NewtbName`
    2. 修改字段名 `alter table tbName change id id1 int`
    3. 增加字段在首位 `alter table tbName add sex varchar(10) first`
    4. 增加字段(在某个字段后) `alter table tbName add address int after sex`
    5. 删除字段 `alter table tbName drop id`

## 表约束和表关系
1. 非空约束
    - 创建表时添加非空约束 `create table tbName(id int not null)`
    - 已经创建表时添加非空约束 `alter table tbName modify id int not null`
    - 取消非空约束 `alter table tbName modify id int`
2. 唯一约束`unique key`
    - 字段对应的值不能重复
    - 添加唯一约束 `create table tbName(id int unique key)`
    - 添加唯一约束 `create table tbName(id int, unique key(id))`
    - 添加唯一约束 `alter table tbName add unique key(id)`
    - 添加唯一约束 `alter table tbName modify id int unique key`
    - 删除唯一约束 `alter table tbName drop unique key id`
3. 主键约束`primary key`
    - 唯一标识一条数据,每个表一个主键,非空且唯一
    - 当没有主键时,第一个非空且唯一的被视为主键
    - 创建主键 `create table tbName(id int primary key)`
    - 创建主键 `alter table tbName add primary key(id)`
    - 创建主键 `alter table tbName modify id int primary key`
    - 删除主键 `alter table tbName drop primary key`
4. 自增长字段
    - 必须与键一起使用
    - 一个表中一个自增长字段,自增量默认为1,起始值默认为1
    - 创建自增字段 `create table tbName(id int auto_increment)auto_increment=100`
    - 创建自增字段 `alter table tbName modify id int auto_crement`
5. 默认约束
    - 如果`insert`时没有赋值则取默认值
    - `create table tbName(id int default 10)`
6. 外键约束
    1. 外键是另一个表的主键,减少数据冗余
    2. 删除外键 `alter table tbName drop foreign key(s_id)`

```
# 学校
create table school(
    id int primary key,
    name varchar(10) not null
);

# 学生所在的学校
create table student(
    s_id int primary key auto_increment,
    s_name char(10) not null,
    d_id int not null,
    constraint ds_id foreign key(d_id) references school(id)
)

# 学生详细信息
create table student_detail(
    de_id int primary key auto_increment,
    info varchar(10) not null,
    foreign key(de_id) references student(s_id)
)

# 课程信息
create table cours(
    c_id int primary key,
    c_name char(10) not null
)

# 选课表(多对多)学生与课程关联
create table choose(
    cs_id int, # 表示学生
    cours_id int, # 表示课程
    primary key(cs_id, cours_id), # 联合主键(组合唯一且非空)
    foreign key(cs_id) references student(s_id),
    foreign key(cours_id) references  cours(c_id)
)
```


--查询所有男生的姓名，年龄，所在班级名称；
select name,age,cls_id from students where gender='男';

--查询所有查询编号小于4或没被删除的学生；
select * from students where id<4 or is_delete = 0;

--查询姓黄并且“名”是一个字的学生；
select * from students where name like '黄_';

--查询编号是1或3或8的学生
select * from students where id in (1,3,8);
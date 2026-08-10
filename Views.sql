use college;
select * from student_data;

alter table student_data drop column email;
alter table student_data rename column branch to department;

create view students as select name, department from student_data;
select * from students;

create view MCA1_department as select * from students where department = "MCA";
select * from MCA1_department;


create view toppers as select name,marks,department from student_data where marks > 90;
select * from toppers;

use employee;
select * from employee2;

create view employee_details as select id,salary from employee2;
select * from employee_details;
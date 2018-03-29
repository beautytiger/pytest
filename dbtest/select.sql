select count(id) from indexed_num where col_value<9246744073709551615;
select count(id) from indexed_num;

select * from indexed_num order by id desc limit 1;

select count(id) from random_num where col_value<9246744073709551615;
select count(id) from random_num;

select * from random_num order by id desc limit 1;
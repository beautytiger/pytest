#!/usr/bin/env python3

import sys

import colorama

colorama.init()


def colprint(s):
    print(colorama.Fore.RED + s, end='')
    print(colorama.Style.RESET_ALL)


template = """DROP PROCEDURE
IF EXISTS {procedure_name};
delimiter ;;

CREATE PROCEDURE {procedure_name} (IN record_id INT(11))
BEGIN

DECLARE my_sql VARCHAR (500) ;
SET my_sql = concat('UPDATE {table_name} SET enabled = 0 WHERE id=', record_id);
SET @ms = my_sql ; 
PREPARE s1 FROM @ms ; 
EXECUTE s1 ; 
DEALLOCATE PREPARE s1 ; 
SELECT count(id) as success FROM {table_name} WHERE	id = record_id AND enabled = 0 ;

END;;
delimiter ;
"""

if __name__ == '__main__':
    colprint('Please make sure that the virtual delete column name is *enabled*!')
    procedure_name = sys.argv[1]
    table_name = sys.argv[2]
    with open('sql_delete_record.sql', 'w') as f:
        f.write(template.format(procedure_name=procedure_name, table_name=table_name))
    print("Job finished")

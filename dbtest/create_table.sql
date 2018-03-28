CREATE TABLE `indexed_num` (
`id`  int(12) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`col_value`  int(12) UNSIGNED NOT NULL DEFAULT 0 COMMENT '行记录值' ,
`create_at`  datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`modify_at`  datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间' ,
PRIMARY KEY (`id`),
UNIQUE INDEX `value_index_in_table` (`col_value`) USING BTREE
);

ALTER TABLE `indexed_num`
MODIFY COLUMN `col_value`  bigint(20) UNSIGNED NOT NULL DEFAULT 0 COMMENT '行记录值' AFTER `id`;


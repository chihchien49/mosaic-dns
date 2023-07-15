DROP DATABASE IF EXISTS `dns_db`;
CREATE DATABASE `dns_db`;
use `dns_db`;

GRANT ALL PRIVILEGES ON dns_db.* TO 'dns'@'%' IDENTIFIED BY 'mn962lf8sm49sh4k1';
FLUSH PRIVILEGES;

CREATE TABLE `devices` (
    `name` varchar(256) NOT NULL UNIQUE,
    `ip` varchar(16) NOT NULL,
    PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


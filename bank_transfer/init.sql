# **************
# 初始化模拟银行转账数据信息
# Generation Time: 2017-08-10 
# *************

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `email` varchar(50) NOT NULL,
      `passwd` varchar(50) NOT NULL,
      `admin` tinyint(1) NOT NULL,
      `name` varchar(50) NOT NULL,
      `balance` decimal(10,2) unsigned NOT NULL COMMENT '用户账户余额',
      `image` varchar(500) NOT NULL,
      `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (`id`),
      UNIQUE KEY `idx_email` (`email`),
      KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`id`, `email`, `passwd`, `admin`, `name`, `balance`, `image`)
VALUES
    (1, 'Lean@google.com', '12345678', 0, 'Lean', 1000.00, 'about:blank'),
    (2, 'Lean1@google.com', '12345678', 0, 'Lean1', 100.00, 'about:blank');

DROP TABLE IF EXISTS `fund_history`;

CREATE TABLE `fund_history` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT comment '转账记录',
    `from_user_id` int(10) NOT NULL,
    `target_user_id` int(10) NOT NULL,
    `transfer_money` decimal(10,2) unsigned NOT NULL COMMENT '转账金额',
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET=utf8;



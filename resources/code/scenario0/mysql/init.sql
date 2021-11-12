CREATE DATABASE IF NOT EXISTS `mydb`;

USE `mydb`;

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `bio` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);


insert  into `users`(`id`,`username`,`name`,`bio`) values
(1,'marceline','Marceline Abadeer','1000 year old vampire queen, musician');

-- =====================================================================================================================

DROP TABLE IF EXISTS `posts`;

CREATE TABLE `posts` (
  `thread` int NOT NULL,
  `text` varchar(50) NOT NULL,
  `user` int NOT NULL,
  PRIMARY KEY (`thread`)
);


insert  into `posts`(`thread`,`text`,`user`) values
(1,'Has anyone checked on the lich recently?',1);

-- =====================================================================================================================

DROP TABLE IF EXISTS `threads`;

CREATE TABLE `threads` (
  `id` int NOT NULL,
  `title` varchar(50) NOT NULL,
  `createdBy` int NOT NULL,
  PRIMARY KEY (`id`)
);

insert  into `threads`(`id`,`title`,`createdBy`) values
(1,'What''s up with the Lich?',1);

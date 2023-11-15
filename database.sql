/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - public_auditing
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`public_auditing` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `public_auditing`;

/*Table structure for table `reg` */

DROP TABLE IF EXISTS `reg`;

CREATE TABLE `reg` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `pwd` varchar(200) DEFAULT NULL,
  `addr` varchar(200) DEFAULT NULL,
  `Contact` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT 'waiting',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `reg` */

insert  into `reg`(`id`,`name`,`email`,`pwd`,`addr`,`Contact`,`status`) values (1,'aÉ%ö—_â®Øe\"Ü¬Ì','kumar@gmail.com','Ñ\" twnÏŠ7V\"\"P','­í6‚Ï\nÑ¹1˜\\¥Œ','\r\"¬|ÕA^©Ò(J~­d÷','Accepted'),(2,'÷¢°›i),É­DÇ£–¥','preeti@gmail.com','Ñ\" twnÏŠ7V\"\"P','iÕ9‚ã8rŒÕ£“','Ü37ï*¹¬â¨QBx&','Accepted'),(3,'üí™ÀÞî[ð!—ÄK°','nakku@gmail.com','Ñ\" twnÏŠ7V\"\"P','iÕ9‚ã8rŒÕ£“','Ÿ3ä\\Í¾¸rzÃÌígØòÑ','Accepted'),(4,'Àú>L©Ã bgš*í\0\0','rani@gmail.com','Ñ\" twnÏŠ7V\"\"P','iÕ9‚ã8rŒÕ£“','RÔHT’Ej¤Ró\"\n¼æ—','Accepted');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `fid` int(20) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `uemail` varchar(200) DEFAULT NULL,
  `filename` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT 'waiting',
  `pkey` varchar(200) DEFAULT NULL,
  `action` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`fid`,`email`,`uemail`,`filename`,`status`,`pkey`,`action`) values (1,1,'preeti@gmail.com','kumar@gmail.com','Ï¨zå0$=•7¦Sj','Accepted','595359','Completed'),(2,2,'rani@gmail.com','nakku@gmail.com','	g‚ã™]¡«F‹ò€»=','waiting',NULL,NULL);

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `Id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(200) DEFAULT NULL,
  `filename` varchar(200) DEFAULT NULL,
  `files` longtext,
  `skey` varchar(200) DEFAULT NULL,
  `status` varchar(2000) DEFAULT 'pending',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`Id`,`email`,`filename`,`files`,`skey`,`status`) values (1,'preeti@gmail.com','Ï¨zå0$=•7¦Sj','ˆãt+HèÖ/ßP!ÌÎ‡e4*#Þ)MÉEv`\'Ì~–rKÉRÒãtÜ”7öÍŸïêL ®‹Í8~–^›˜¢ÿ6ƒ¬&¶æ˜Ò)qr-( åüíO÷¨©Ê&k2ÔæIö[}€pâÊzÕ\'¼R«ŽBdñŽ6³\\Éùçr/˜²ë²Â\ZÖ­à}¶PÏuM†yI’±)Q2gì\\D-›Aü{SRy,™¢_¶zs¨÷·èHŒÙ@s3µ1h!^j™CŸÎ$Òy]ìNP³T¦Ò\rLUb,`ÁÁFô*BE‡á÷\rûuÑ5ç¢WN»Re\"þ¸Õè-Àp','oV&/ó;àšý“µÕ¥','pending'),(2,'rani@gmail.com','	g‚ã™]¡«F‹ò€»=','Ø)Ùvï|\0h^$ºDâ<aú¾œüž\râƒ^˜+Èµïž¢','äxÏ‰Ù‡ÒÔ.ôÿª)·','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

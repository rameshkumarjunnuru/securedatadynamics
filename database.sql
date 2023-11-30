/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - public_auditing
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/* SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/* SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

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


/* SET SQL_MODE=@OLD_SQL_MODE */;
/* SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

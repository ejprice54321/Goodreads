-- MySQL dump 2/11/2017
--
-- Host: localhost    Database: goodreads
-- ------------------------------------------------------
--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;

CREATE TABLE `answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titleId` int(11) NOT NULL,
  `authorId` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
UNLOCK TABLES;

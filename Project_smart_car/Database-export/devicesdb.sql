CREATE DATABASE  IF NOT EXISTS `devicesdb` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `devicesdb`;
-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: devicesdb
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actie`
--s

DROP TABLE IF EXISTS `actie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actie` (
  `ActieID` int NOT NULL AUTO_INCREMENT,
  `ActieBeschrijving` varchar(145) NOT NULL,
  PRIMARY KEY (`ActieID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actie`
--

LOCK TABLES `actie` WRITE;
/*!40000 ALTER TABLE `actie` DISABLE KEYS */;
INSERT INTO `actie` VALUES (1,'Data ophalen'),(2,'Data versturen'),(3,'Data inlezen'),(4,'Buzzer aan'),(5,'Buzzer uit'),(6,'LED aan'),(7,'LED uit');
/*!40000 ALTER TABLE `actie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `DeviceID` int NOT NULL,
  `SoortID` int NOT NULL,
  `Naam` varchar(145) DEFAULT NULL,
  `Merk` varchar(145) DEFAULT NULL,
  `Beschrijving` varchar(145) DEFAULT NULL,
  `AankoopKost` float DEFAULT NULL,
  `Meeteenheid` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`DeviceID`),
  KEY `fk_Device_Soort` (`SoortID`),
  CONSTRAINT `fk_Device_Soort` FOREIGN KEY (`SoortID`) REFERENCES `soort` (`SoortID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (1,2,'LED',NULL,'Lights up when needed.',0.11,NULL),(2,2,'Buzzer',NULL,'Gives a sound when needed.',1.49,NULL),(3,1,'JSN-sr04t',NULL,'Distance sensor.',17.95,'CM'),(4,2,'LDR',NULL,'Light dependent resistor (reads the brightness)',0.25,'%'),(5,1,'Speed Sensor',NULL,'Gives the speed.',2.19,'KM/H'),(6,2,'LED String light','Grove','Lights up in multiple colors.',16.5,NULL),(7,2,'LCD',NULL,'Device to display things.',3.19,NULL);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historiek`
--

DROP TABLE IF EXISTS `historiek`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historiek` (
  `HistoriekID` int NOT NULL AUTO_INCREMENT,
  `DeviceID` int NOT NULL,
  `ActieID` int NOT NULL,
  `Actiedatum` datetime DEFAULT CURRENT_TIMESTAMP,
  `Waarde` float DEFAULT NULL,
  `Commentaar` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`HistoriekID`),
  KEY `fk_Historiek_Device` (`DeviceID`),
  KEY `fk_Historiek_Actie` (`ActieID`),
  CONSTRAINT `fk_Historiek_Actie` FOREIGN KEY (`ActieID`) REFERENCES `actie` (`ActieID`),
  CONSTRAINT `fk_Historiek_Device` FOREIGN KEY (`DeviceID`) REFERENCES `device` (`DeviceID`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historiek`
--

LOCK TABLES `historiek` WRITE;
/*!40000 ALTER TABLE `historiek` DISABLE KEYS */;
INSERT INTO `historiek` VALUES (1,1,3,'2017-05-31 19:19:09',NULL,'Dit is voorbeeldcommentaar'),(2,5,3,'2018-02-25 04:19:12',15,'Dit is voorbeeldcommentaar'),(3,5,1,'2017-04-22 15:02:43',17.33,'Dit is voorbeeldcommentaar'),(4,2,3,'2018-07-08 06:53:13',NULL,'Dit is voorbeeldcommentaar'),(5,6,2,'2017-06-12 06:57:12',NULL,'Dit is voorbeeldcommentaar'),(6,5,3,'2017-12-18 15:23:55',28.45,'Dit is voorbeeldcommentaar'),(7,5,3,'2017-03-29 08:32:39',14,'Dit is voorbeeldcommentaar'),(8,4,2,'2017-07-23 11:09:27',17.33,'Dit is voorbeeldcommentaar'),(9,6,2,'2017-06-25 19:11:08',NULL,'Dit is voorbeeldcommentaar'),(10,1,3,'2018-07-02 20:06:45',NULL,'Dit is voorbeeldcommentaar'),(11,6,7,'2018-10-14 01:42:39',NULL,'Dit is voorbeeldcommentaar'),(12,6,1,'2018-08-30 17:55:55',NULL,'Dit is voorbeeldcommentaar'),(13,6,1,'2017-10-05 17:29:26',NULL,'Dit is voorbeeldcommentaar'),(14,3,1,'2017-03-24 04:00:50',15,'Dit is voorbeeldcommentaar'),(15,7,6,'2017-03-23 07:10:02',NULL,'Dit is voorbeeldcommentaar'),(16,3,1,'2018-02-25 05:09:05',28.45,'Dit is voorbeeldcommentaar'),(17,7,2,'2018-05-06 04:48:26',NULL,'Dit is voorbeeldcommentaar'),(18,1,2,'2018-11-23 15:13:11',NULL,'Dit is voorbeeldcommentaar'),(19,4,1,'2017-11-19 12:56:45',14,'Dit is voorbeeldcommentaar'),(20,2,2,'2018-05-17 11:25:39',NULL,'Dit is voorbeeldcommentaar'),(21,6,1,'2017-05-15 09:10:22',NULL,'Dit is voorbeeldcommentaar'),(22,7,1,'2018-08-12 00:19:01',NULL,'Dit is voorbeeldcommentaar'),(23,3,2,'2018-09-02 04:33:28',28.45,'Dit is voorbeeldcommentaar'),(24,3,2,'2017-04-01 18:29:17',14,'Dit is voorbeeldcommentaar'),(25,2,2,'2018-11-03 11:28:34',NULL,'Dit is voorbeeldcommentaar'),(26,2,3,'2017-12-21 02:30:35',NULL,'Dit is voorbeeldcommentaar'),(27,1,3,'2017-02-28 12:46:31',NULL,'Dit is voorbeeldcommentaar'),(28,5,1,'2017-02-23 05:07:23',28.45,'Dit is voorbeeldcommentaar'),(29,1,1,'2018-01-16 07:45:54',NULL,'Dit is voorbeeldcommentaar'),(30,7,5,'2017-03-05 17:35:05',NULL,'Dit is voorbeeldcommentaar'),(31,1,1,'2017-12-18 11:18:17',NULL,'Dit is voorbeeldcommentaar'),(32,5,3,'2018-09-30 17:24:11',15,'Dit is voorbeeldcommentaar'),(33,4,1,'2018-01-23 20:11:38',28.45,'Dit is voorbeeldcommentaar'),(34,1,3,'2018-10-19 17:03:08',NULL,'Dit is voorbeeldcommentaar'),(35,3,1,'2018-07-31 12:27:20',14,'Dit is voorbeeldcommentaar'),(36,2,1,'2017-03-25 10:30:29',NULL,'Dit is voorbeeldcommentaar'),(37,1,2,'2017-06-16 17:36:13',28.45,'Dit is voorbeeldcommentaar'),(38,7,1,'2017-01-27 17:21:46',NULL,'Dit is voorbeeldcommentaar'),(39,3,1,'2018-04-16 04:22:20',28.45,'Dit is voorbeeldcommentaar'),(40,2,3,'2018-01-12 07:24:26',NULL,'Dit is voorbeeldcommentaar'),(41,3,3,'2018-08-25 19:24:18',28.45,'Dit is voorbeeldcommentaar'),(42,7,2,'2018-06-22 07:08:00',NULL,'Dit is voorbeeldcommentaar'),(43,5,1,'2018-11-18 03:38:02',28.45,'Dit is voorbeeldcommentaar'),(44,4,3,'2018-09-29 02:18:27',15,'Dit is voorbeeldcommentaar'),(45,4,2,'2018-09-27 21:11:33',17.33,'Dit is voorbeeldcommentaar'),(46,3,1,'2017-08-31 22:08:56',15,'Dit is voorbeeldcommentaar'),(47,7,2,'2018-05-09 04:54:12',NULL,'Dit is voorbeeldcommentaar'),(48,7,3,'2017-06-16 07:07:40',NULL,'Dit is voorbeeldcommentaar'),(49,4,2,'2018-09-14 21:05:01',17.33,'Dit is voorbeeldcommentaar'),(50,4,2,'2018-09-15 22:05:01',23,'Dit is voorbeeldcommentaar');
/*!40000 ALTER TABLE `historiek` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soort`
--

DROP TABLE IF EXISTS `soort`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soort` (
  `SoortID` int NOT NULL,
  `Naam` varchar(145) NOT NULL,
  PRIMARY KEY (`SoortID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soort`
--

LOCK TABLES `soort` WRITE;
/*!40000 ALTER TABLE `soort` DISABLE KEYS */;
INSERT INTO `soort` VALUES (1,'Sensor'),(2,'Actuator');
/*!40000 ALTER TABLE `soort` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'devicesdb'
--

--
-- Dumping routines for database 'devicesdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-24 19:49:32

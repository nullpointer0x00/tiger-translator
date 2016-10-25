CREATE TABLE `Uebersetzung`.`SearchHistory` (
  `Id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `SearchTerm` VARCHAR(128) NOT NULL,
  `Lang` VARCHAR(2) NOT NULL,
  `Created` TIMESTAMP DEFAULT now(),
  `Updated` TIMESTAMP DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`Id`));

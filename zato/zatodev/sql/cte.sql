-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema cte
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cte`;
-- -----------------------------------------------------
-- Schema cte
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cte` DEFAULT CHARACTER SET utf8 ;
USE `cte` ;

-- -----------------------------------------------------
-- Table `cte`.`Corpus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cte`.`Corpus` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cte`.`CorpusText`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cte`.`CorpusText` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `corpusid` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `content` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`id`, `corpusid`),
  INDEX `fk_CorpusText_Corpus_idx` (`corpusid` ASC),
  CONSTRAINT `fk_CorpusText_Corpus`
    FOREIGN KEY (`corpusid`)
    REFERENCES `cte`.`Corpus` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cte`.`CorpusMetadatum`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cte`.`CorpusMetadata` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `corpusid` INT NOT NULL,
  `keyname` VARCHAR(45) NOT NULL,
  `keyvalue` VARCHAR(255) NULL,
  PRIMARY KEY (`id`, `corpusid`),
  INDEX `CorpusMetaData_Corpus_idx` (`corpusid` ASC),
  CONSTRAINT `fk_CorpusMetadata_Corpus`
    FOREIGN KEY (`corpusid`)
    REFERENCES `cte`.`Corpus` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


GRANT ALL ON `cte`.* TO 'ytex' IDENTIFIED BY 'ytex';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

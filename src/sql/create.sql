-- MySQL Workbench Forward Engineering
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema TaskManagementSystem
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `TaskManagementSystem`;
CREATE SCHEMA IF NOT EXISTS `TaskManagementSystem` DEFAULT CHARACTER SET utf8;
USE `TaskManagementSystem`;

-- -----------------------------------------------------
-- Table `User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `User`;
CREATE TABLE IF NOT EXISTS `User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `passwordHash` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Project`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Project`;
CREATE TABLE IF NOT EXISTS `Project` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `description` TEXT NULL,
  `owner_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Project_User_idx` (`owner_id` ASC),
  CONSTRAINT `fk_Project_User`
    FOREIGN KEY (`owner_id`)
    REFERENCES `User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Board`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Board`;
CREATE TABLE IF NOT EXISTS `Board` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `project_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Board_Project_idx` (`project_id` ASC),
  CONSTRAINT `fk_Board_Project`
    FOREIGN KEY (`project_id`)
    REFERENCES `Project` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Column`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Column`;
CREATE TABLE IF NOT EXISTS `Column` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `board_id` INT NOT NULL,
  `order_num` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Column_Board_idx` (`board_id` ASC),
  CONSTRAINT `fk_Column_Board`
    FOREIGN KEY (`board_id`)
    REFERENCES `Board` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Task`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Task`;
CREATE TABLE IF NOT EXISTS `Task` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `description` TEXT NULL,
  `start_date` DATE NULL,
  `end_date` DATE NULL,
  `status` TEXT NOT NULL,
  `project_id` INT NOT NULL,
  `assignee_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Task_Project_idx` (`project_id` ASC),
  INDEX `fk_Task_User_idx` (`assignee_id` ASC),
  CONSTRAINT `fk_Task_Project`
    FOREIGN KEY (`project_id`)
    REFERENCES `Project` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Task_User`
    FOREIGN KEY (`assignee_id`)
    REFERENCES `User` (`id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `TaskColumnLink`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TaskColumnLink`;
CREATE TABLE IF NOT EXISTS `TaskColumnLink` (
  `task_id` INT NOT NULL,
  `column_id` INT NOT NULL,
  PRIMARY KEY (`task_id`, `column_id`),
  INDEX `fk_TaskColumnLink_Task_idx` (`task_id` ASC),
  INDEX `fk_TaskColumnLink_Column_idx` (`column_id` ASC),
  CONSTRAINT `fk_TaskColumnLink_Task`
    FOREIGN KEY (`task_id`)
    REFERENCES `Task` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_TaskColumnLink_Column`
    FOREIGN KEY (`column_id`)
    REFERENCES `Column` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Comment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Comment`;
CREATE TABLE IF NOT EXISTS `Comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `task_id` INT NOT NULL,
  `author_id` INT NOT NULL,
  `content` TEXT NOT NULL,
  `timestamp` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Comment_Task_idx` (`task_id` ASC),
  INDEX `fk_Comment_User_idx` (`author_id` ASC),
  CONSTRAINT `fk_Comment_Task`
    FOREIGN KEY (`task_id`)
    REFERENCES `Task` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Comment_User`
    FOREIGN KEY (`author_id`)
    REFERENCES `User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Restore original settings
-- -----------------------------------------------------
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

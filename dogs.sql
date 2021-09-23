-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dogs
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dogs` ;

-- -----------------------------------------------------
-- Schema dogs
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dogs` DEFAULT CHARACTER SET utf8 ;
USE `dogs` ;

-- -----------------------------------------------------
-- Table `dogs`.`breeds_group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dogs`.`breeds_group` ;

CREATE TABLE IF NOT EXISTS `dogs`.`breeds_group` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dogs`.`breeds`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dogs`.`breeds` ;

CREATE TABLE IF NOT EXISTS `dogs`.`breeds` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_breed_group` INT(10) UNSIGNED NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `description` TEXT NOT NULL,
  `url_image` VARCHAR(256) NOT NULL,
  `height` VARCHAR(100) NULL DEFAULT NULL,
  `weight` VARCHAR(100) NULL DEFAULT NULL,
  `life_span` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC),
  INDEX `fk_breed_in_group_idx` (`id_breed_group` ASC),
  CONSTRAINT `fk_breed_in_group`
    FOREIGN KEY (`id_breed_group`)
    REFERENCES `dogs`.`breeds_group` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dogs`.`adaptability`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dogs`.`adaptability` ;

CREATE TABLE `adaptability` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `breeds_id` INT(10) UNSIGNED NOT NULL,
  `adapts_well_to_apartment_living` bigint(20) DEFAULT NULL,
  `good_for_novice_owners` bigint(20) DEFAULT NULL,
  `sensitivity_level` bigint(20) DEFAULT NULL,
  `tolerates_being_alone` bigint(20) DEFAULT NULL,
  `tolerates_cold_weather` bigint(20) DEFAULT NULL,
  `tolerates_hot_weather` bigint(20) DEFAULT NULL,
  `affectionate_with_family` bigint(20) DEFAULT NULL,
  `kid_friendly` bigint(20) DEFAULT NULL,
  `dog_friendly` bigint(20) DEFAULT NULL,
  `friendly_toward_strangers` bigint(20) DEFAULT NULL,
  `amount_of_shedding` bigint(20) DEFAULT NULL,
  `drooling_potential` bigint(20) DEFAULT NULL,
  `easy_to_groom` bigint(20) DEFAULT NULL,
  `general_health` bigint(20) DEFAULT NULL,
  `potential_for_weight_gain` bigint(20) DEFAULT NULL,
  `size` bigint(20) DEFAULT NULL,
  `easy_to_train` bigint(20) DEFAULT NULL,
  `intelligence` bigint(20) DEFAULT NULL,
  `potential_for_mouthiness` bigint(20) DEFAULT NULL,
  `prey_drive` bigint(20) DEFAULT NULL,
  `tendency_to_bark_or_howl` bigint(20) DEFAULT NULL,
  `wanderlust_potential` bigint(20) DEFAULT NULL,
  `energy_level` bigint(20) DEFAULT NULL,
  `intensity` bigint(20) DEFAULT NULL,
  `exercise_needs` bigint(20) DEFAULT NULL,
  `potential_for_playfulness` text,
  PRIMARY KEY (`id`),
  INDEX `fk_adaptability_breeds1_idx` (`breeds_id` ASC),
  CONSTRAINT `fk_adaptability_breeds1`
    FOREIGN KEY (`breeds_id`)
    REFERENCES `dogs`.`breeds` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE=InnoDB
AUTO_INCREMENT=1
DEFAULT CHARSET=utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

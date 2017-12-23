CREATE TABLE `notes_master` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `note_title` varchar(100) DEFAULT NULL,
  `note_content` text,
  `created_datetime` datetime DEFAULT NULL,
  `modified_datetime` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`note_id`)
);
CREATE TABLE `notes_master_history` (
  `note_history_id` int(11) NOT NULL AUTO_INCREMENT,
  `note_id` int(11) DEFAULT NULL,
  `note_title` varchar(100) DEFAULT NULL,
  `note_content` text,
  `created_datetime` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`note_history_id`),
  KEY `note_id` (`note_id`),
  CONSTRAINT `notes_master_history_ibfk_1` FOREIGN KEY (`note_id`) REFERENCES `notes_master` (`note_id`)
);
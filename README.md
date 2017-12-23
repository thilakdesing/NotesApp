Video Demo:
	Video demonstration of Notes app - https://youtu.be/72PYnaAZ5R0

Technical summary:

	1. User can input data into the notes , namely TITLE and CONTENT.On clicking add notes, ajax call is made to generate a new id for the note.
	2. On inactivity of 5 seconds, the notes is autosaved using Ajax with NOTE ID.Updations are stored in master table by moving the previous content to history table. Hence, all actions on note are traced in history table
	3. On moving out of an active note, the note is saved on the same procedure.
	4. On deletion of a note, the ACTIVE status of current note is set to False.
	5. On clicking Maximize button, the hitorical versions are fetched using Ajax.
	6. Any changes made to the history are also saved as a new entry.

Code Interactions:

	1. URLS.py  - Request on browser is sent to respective urls, mapped under urls.py
	2. VIEWS.py - urls.py communicates to views where Query arguments are verified.
	3. NOTES_HANDLER,py - Based on query arguments,notes_handler's methods are called
	4. NOTES_DAO - Data access object which talks to DB
	5. TRANSACTIONAL_MANAGER.py - Initiates connectivity to DB and holds the connection object
	6. TESTS.py - Unit Test cases to check the functionality of code with changing versions
 

INFRASTRUCTURE/RESOURCES:

	The application is deployable and can be run on anyserver by following python manage.py runserver <server IP:port>
	* Front end design using HTML,CSS,jQuery,Bootstrap and Ajax.
	* MVC framework using Django with Python as dev code
	* MySQL database for storage.
	DB SCHEMA:
	CREATE TABLE `notes_master` (
	  `note_id` int(11) NOT NULL AUTO_INCREMENT,
	  `note_title` varchar(100) DEFAULT NULL,
	  `note_content` text,
	  `created_datetime` datetime DEFAULT NULL,
	  `modified_datetime` datetime DEFAULT NULL,
	  `status` tinyint(1) DEFAULT '1',
	  PRIMARY KEY (`note_id`)
	)
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
	)Technical summary:

	1. User can input data into the notes , namely TITLE and CONTENT.On clicking add notes, ajax call is made to generate a new id for the note.
	2. On inactivity of 5 seconds, the notes is autosaved using Ajax with NOTE ID.Updations are stored in master table by moving the previous content to history table. Hence, all actions on note are traced in history table
	3. On moving out of an active note, the note is saved on the same procedure.
	4. On deletion of a note, the ACTIVE status of current note is set to False.
	5. On clicking Maximize button, the hitorical versions are fetched using Ajax.
	6. Any changes made to the history are also saved as a new entry.

Code Interactions:

	1. URLS.py  - Request on browser is sent to respective urls, mapped under urls.py
	2. VIEWS.py - urls.py communicates to views where Query arguments are verified.
	3. NOTES_HANDLER,py - Based on query arguments,notes_handler's methods are called
	4. NOTES_DAO - Data access object which talks to DB
	5. TRANSACTIONAL_MANAGER.py - Initiates connectivity to DB and holds the connection object
 

INFRASTRUCTURE/RESOURCES:

	The application is deployable and can be run on anyserver by following python manage.py runserver <server IP:port>
	* Front end design using HTML,CSS,jQuery,Bootstrap and Ajax.
	* MVC framework using Django with Python as dev code
	* MySQL database for storage.
	DB SCHEMA:
	CREATE TABLE `notes_master` (
	  `note_id` int(11) NOT NULL AUTO_INCREMENT,
	  `note_title` varchar(100) DEFAULT NULL,
	  `note_content` text,
	  `created_datetime` datetime DEFAULT NULL,
	  `modified_datetime` datetime DEFAULT NULL,
	  `status` tinyint(1) DEFAULT '1',
	  PRIMARY KEY (`note_id`)
	)
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
	)

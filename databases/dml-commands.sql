	 CREATE DATABASE PlasmaDonationSystem;
	 USE PlasmaDonationSystem;
     
	 CREATE TABLE Donor_backup
     (Donor_ID INT NOT NULL AUTO_INCREMENT,
     Name VARCHAR(50) NOT NULL, 
     Sex VARCHAR(10),
     Age INT,
     Email VARCHAR(100),
     any_symptoms VARCHAR(5) NOT NULL,
     any_medication VARCHAR(5) NOT NULL,
     any_tattoo VARCHAR(5) NOT NULL,
     any_travel VARCHAR(5) NOT NULL,
     follow_up_test_done VARCHAR(5) NOT NULL,
     14_days_quarantine VARCHAR(5) NOT NULL,
     Weight INT,
     Height INT,
     Pin INT,
     City VARCHAR(30),
     PRIMARY KEY(Donor_ID));
	 ALTER TABLE Donor ADD Plasma_bank_id INT NOT NULL;
     ALTER TABLE Donor ADD FOREIGN KEY(Plasma_bank_id) REFERENCES Plasma_bank(Plasma_bank_id) ON DELETE CASCADE;
     
     CREATE TABLE Donor_Phone
     (Donor_ID INT NOT NULL,
     Phone_no VARCHAR(13),
     FOREIGN KEY(Donor_ID)
     REFERENCES Donor(Donor_ID)
     ON DELETE CASCADE);
     
	 CREATE TABLE Plasma_Bank
     (Plasma_bank_id INT NOT NULL,
     Name VARCHAR(50) NOT NULL,
     Email VARCHAR(100),
     Total_plasma_count_available INT DEFAULT 0,
     Pin INT,
     Street VARCHAR(10),
     City VARCHAR(30),
     PRIMARY KEY(Plasma_bank_ID));
     
     
	 CREATE TABLE Plasma_bank_Phone
     (Plasma_bank_ID INT NOT NULL,
     Phone_no VARCHAR(13),
     FOREIGN KEY(Plasma_bank_ID)
     REFERENCES Plasma_bank(Plasma_bank_ID)
     ON DELETE CASCADE);
     
     CREATE TABLE Donor_Feedback
     (Plasma_bank_id INT NOT NULL,
     Feedback VARCHAR(200),
     FOREIGN KEY(Plasma_bank_ID)
     REFERENCES Plasma_bank(Plasma_bank_ID)
     ON DELETE CASCADE);
     
     CREATE TABLE Hospital_Feedback
     (Plasma_bank_id INT NOT NULL,
     Feedback VARCHAR(200),
     FOREIGN KEY(Plasma_bank_ID)
     REFERENCES Plasma_bank(Plasma_bank_ID)
     ON DELETE CASCADE);
     
	 CREATE TABLE Blood_details_W
     (Donor_ID INT NOT NULL,
     Blood_group VARCHAR(05),
     RH_Type VARCHAR(10),
     Platelet_count INT,
     WBC_Count INT,
     Antibodies_produced VARCHAR(50),
     FOREIGN KEY(Donor_ID)
     REFERENCES Donor(Donor_id)
     ON DELETE CASCADE);
     ALTER TABLE Blood_details_W ADD Plasma_bank_id INT NOT NULL;
     ALTER TABLE Blood_details_W ADD FOREIGN KEY(Plasma_bank_ID) REFERENCES Plasma_bank(Plasma_bank_ID)ON DELETE CASCADE;
     
     CREATE TABLE Hospital
     (Hospital_ID INT NOT NULL,
     Name VARCHAR(50) NOT NULL,
     Email VARCHAR(100),
     Pin INT,
     Street VARCHAR(10),
     City VARCHAR(30),
     Plasma_count_needed INT DEFAULT 0,
     PRIMARY KEY(Hospital_ID));
     
     CREATE TABLE Hospital_Phone
     (Hospital_ID INT NOT NULL,
     Phone_no INT,
     FOREIGN KEY(Hospital_ID)
     REFERENCES HOspital(Hospital_ID)
     ON DELETE CASCADE);
     
     CREATE TABLE Manager
     (Manager_ID INT NOT NULL,
     Name VARCHAR(30),
     State VARCHAR(50),
     Count_of_plasma_banks_under INT DEFAULT 0,
     No_of_revokes INT DEFAULT 0,
     PRIMARY KEY(Manager_ID));
     
     CREATE TABLE Provides_plasma
     (Plasma_bank_id INT NOT NULL,
     Hospital_ID INT NOT NULL,
     FOREIGN KEY(Plasma_bank_ID)
     REFERENCES Plasma_bank(Plasma_bank_ID),
     FOREIGN KEY(Hospital_ID)
     REFERENCES Hospital(Hospital_ID)
     ON DELETE CASCADE);
     
     


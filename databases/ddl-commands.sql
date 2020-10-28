INSERT INTO plasma_bank (Plasma_bank_id, Name, Email, Total_plasma_count_available, Pin, Street, City)
VALUES
(20202, "Mumbai-N Plamsa Donation", "mumbainplasma@gmail.com",81, 40003, "ChurchRd", "Mumbai"),
(20203, "Pune City Donation Camp", "puneplasma@gmail.com",67, 41108, "Kothrud", "Pune"),
(20204, "Nagpur Plasma Service", "ngpplasma@gmail.com",54, 44004, "CivilLn", "Nagpur"),
(20205, "Banglore-N Plasma Camp", "bnglplasma@gmail.com",66, 30015, "SouthRd", "Banglore"),
(20206, "Madras Plasma Donation", "mdrsplasma@gmail.com",78, 31307, "KattibSq","Mysore"),
(20207, "Noida Health Camp", "noidaplasma@gmail.com", 88, 11035, "Sector130", "Noida"),
(20208, "Delhi Central Plasma Dn", "delhiplasma@gmail.com",91, 11001, "Karolbagh", "Delhi"),
(20209, "Abad Plasma Service", "abadplasma@gmail.com", 27, 51032, "GandhiSq", "Ahemdabad");

INSERT INTO plasma_bank_phone (Plasma_bank_ID, Phone_No)
VALUES
(20202, "753952456"),
(20202, "741852954"),
(20203, "321898752"),
(20204, "974561744"),
(20204, "456546556"),
(20205, "741085296"),
(20206, "654654554"),
(20207, "700000781"),
(20208, "741963963"),
(20209, "521789632");

INSERT INTO Hospital (Hospital_ID, Name, Email, Pin, Street, City, Plasma_count_needed)
VALUES
(10102, "Kasturba Hospital", "kstrbhosp@gmail.com", 41038, "Katraj", "Pune", 17),
(10103, "7Star Hospital", "ssngphosp@gmail.com", 44112, "Sakkardara", "Nagpur", 7),
(10105, "City Hospital", "bglchosp@gmail.com", 31038, "SouthRd", "Banglore", 3),
(10106, "GMC", "gmcmhosp@gmail.com", 31048, "KarnSq", "Manglore", 9),
(10107, "Naidu Hospital", "naiduhosp@gmail.com", 10038, "Sector21", "Noida", 15),
(10108, "RGD Hospital", "rjdhosp@gmail.com", 11038, "SouthRd", "Delhi", 21);

INSERT INTO hospital_phone (Hospital_ID, Phone_No)
VALUES
(10102, "759933356"),
(10102, "741852954"),
(10103, "321898752"),
(10105, "741085296"),
(10106, "654654554"),
(10107, "701111181"),
(10108, "741969993");

INSERT INTO Donor (Donor_ID, Name, Sex, Age, Email,any_symptoms,any_medication,any_tattoo,any_travel,follow_up_test_done, 14_days_quarantine, Weight, Height,Pin, City, Plasma_bank_id)
VALUES
(101,"Ankit", "M", 21, "ankit@yahoo.in", "No", "No","No","No", "Yes", "Yes", 58, 157, 44002, "Nagpur",20204),
(102,"Aradhya", "F", 21, "aru@yahoo.in", "No", "No","No","No", "Yes", "Yes", 48, 146, 41108, "Pune",20203), 
(104,"Dency", "F", 37, "dency@yahoo.in", "No", "Yes","No","No", "Yes", "Yes", 51, 141, 40037, "Mumbai",20202),
(105,"Shivang", "M", 29, "shiv@yahoo.in", "No", "No","Yes","No", "Yes", "Yes", 61, 155, 20138, "Nagpur",20204),
(106,"Vyom", "M", 25, "vyom@yahoo.in", "No", "No","No","No", "Yes", "Yes", 69, 171, 21154, "Banglore",20205),
(107,"Prem", "M", 32, "prem@yahoo.in", "No", "No","No","No", "No", "No", 78, 136, 50012, "Manglore",20206),
(108,"Jagdish", "M", 35, "jag@yahoo.in", "No", "No","No","No", "Yes", "Yes", 65, 155, 21055, "Delhi",20208),
(109,"Ashwin", "M", 32, "ash@yahoo.in", "No", "No","No","No", "Yes", "Yes", 78, 146, 55001, "Noida",20207),
(110, "Shivani", "F", 33, "shivani@yahoo.in", "No", "No","No","No", "Yes", "Yes", 58, 169, 22065, "Noida",20207),
(111,"Anushka", "F", 21, "anush@yahoo.in", "No", "No","No","No", "Yes", "Yes", 48, 171, 33084, "Delhi",20209),
(112,"Haridas", "M", 35, "hari@yahoo.in", "No", "No","No","No", "Yes", "Yes", 64, 196, 44024, "Pune",20203),
(113,"Om", "M", 35, "hari@yahoo.in", "No", "No","No","No", "Yes", "Yes", 64, 151, 44024, "Noida",20207);

INSERT INTO blood_details_w (Donor_ID, Blood_group, RH_Type, Platelet_count, WBC_Count, Antibodies_produced, plasma_bank_id)
VALUES
(104, "AN", "Positive", 31000, 10000, "None", 20202),
(105, "ABP", "Positive", 27000, 8000, "Immunnoglobulin_M", 20204),
(106, "AN", "Negative", 26000, 5000, "None", 20205),
(107, "ABP", "Positive", 26000, 8000, "None", 20206);

INSERT INTO Donor_phone (Donor_ID, Phone_no)
VALUES
(101,"789654562"),
(104,"745521520"),
(105,"874532145"),
(106,"451515558"),
(107,"741265258"),
(108,"741852965"),
(109,"741585665"),
(110,"412563255"),
(111,"741596525"),
(112,"741258966"),
(113,"654785224");

INSERT INTO Manager (Manager_ID, Name, State, Count_of_plasma_banks_under)
VALUES
(2, "VC Shukla", "Karnataka", 7),
(3, "AK Sinha", "Delhi", 6),
(4, "LG Singh", "Uttar Pradesh", 9);


INSERT INTO provides_plasma(Plasma_bank_id, Hospital_ID)
VALUES
(20202,10102),
(20204,10103),
(20205,10105),
(20206,10106);

INSERT INTO donor_feedback(Plasma_bank_id, Feedback)
VALUES
(20202, "Great Service, Social Distancing was taken care of."),
(20204, "Too many formalities"),
(20205, "Great system"),
(20206, "Easy and better way for donation.");

INSERT INTO HOSPITAL_feedback(Plasma_bank_id, Feedback)
VALUES
(20202, "OK"),
(20204, "OK"),
(20205, "Impure/Bad Quality"),
(20206, "OK");

INSERT INTO Donor (Donor_ID, Name, Sex, Age, Email,any_symptoms,any_medication,any_tattoo,any_travel,follow_up_test_done, 14_days_quarantine, Weight, Height,Pin, City, Plasma_bank_id)
VALUES
(690,"Shivansh", "M", 46, "shiva@yahoo.in", "No", "No","Yes","No", "Yes", "Yes", 78, 144, 44001, "Pune",202010),
(102,"Bhagyashree", "F", 37, "bhh@yahoo.in", "Yes", "No","No","Yes", "Yes", "Yes", 78, 170, 41108, "Pune",20204);
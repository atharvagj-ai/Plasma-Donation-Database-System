--TRIGGERS:

/*Trigger to backup the Taken Donor
*/

DELIMITER $$
CREATE TRIGGER donor_backup
BEFORE DELETE
On Donor
FOR EACH ROW
BEGIN
INSERT INTO Donor_backup(Donor_ID, Name, Sex, Age, Email, any_symptoms, any_medication, any_tattoo, any_travel, follow_up_test_done, 14_days_quarantine, Weight, Height, Pin, City)
VALUES
(OLD.Donor_ID, OLD.Name, OLD.Sex, OLD.Age, OLD.Email, OLD.any_symptoms, OLD.any_medication, OLD.any_tattoo, OLD.any_travel, OLD.follow_up_test_done, OLD.14_days_quarantine, OLD.Weight, OLD.Height, OLD.Pin, OLD.City);
END $$
DELIMITER ;

/*Trigger to update the plasma count in the plasma bank
*/

DELIMITER $$
CREATE TRIGGER update_p_count
BEFORE DELETE 
ON donor 
FOR EACH ROW
BEGIN
UPDATE Plasma_bank
SET Total_plasma_count_available = Total_plasma_count_available - 1
WHERE old.Plasma_bank_ID = Plasma_bank.Plasma_bank_ID;
END $$
DELIMITER ;     

--PROCEDURES:

/*Procedure to display citywise needed plasma data
*/
delimiter //
create procedure tot_plasma_need_citywise(IN CityN varchar(30))
begin
DECLARE EXIT HANDLER FOR not found
Select 'City does not exist.' as "Error";
select city, sum(plasma_count_needed) as total_plasma_count_needed from hospital where city=CityN;
end;//
delimiter ;
call tot_plasma_need_citywise('Pune');         

/*Procedure to display citywise available plasma data
*/

delimiter //
create procedure tot_plasma_avail_citywise(IN CityN varchar(30))
begin
DECLARE EXIT HANDLER FOR not found
Select 'City does not exist.' as "Error";
select city, sum(Total_plasma_count_available) as Total_plasma_count_available from Plasma_bank where city=CityN;
end;//
delimiter ;
call tot_plasma_avail_citywise('Pune');    

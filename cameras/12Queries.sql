/*4*/

SELECT * FROM car WHERE PID IN
(SELECT CarID FROM ownership WHERE NationalID='1010101010');

/*1 DESC*/

SELECT * FROM camera join 
(SELECT maintenance1.MID, maintenance1.CameraID , maintenance2.TotalCost FROM maintenance1 
JOIN maintenance2 
ON maintenance1.MID = maintenance2.MID) as maintenence
ON camera.CID = maintenence.CameraID ORDER By maintenence.TotalCost DESC;

/*1 ASC*/
/*
SELECT * FROM camera join 
(SELECT maintenance1.MID, maintenance1.CameraID , maintenance2.TotalCost FROM maintenance1 
JOIN maintenance2 
ON maintenance1.MID = maintenance2.MID) as maintenence
ON camera.CID = maintenence.CameraID ORDER By maintenence.TotalCost ASC;
*/
/*2*/
/*
SELECT DriverCarID, SUM(Amount) as sum_fine
FROM
(SELECT * FROM (
	SELECT fine2.DriverCarID, fine2.FID, fine1_violation.Amount FROM fine2 JOIN(
		SELECT fine1.ViolationID, fine1.FID, violation.Amount FROM fine1 
		JOIN violation
		ON fine1.ViolationID = violation.VID) as fine1_violation
	ON fine1_violation.FID = fine2.FID) as fine1_violation_fine2
	WHERE fine1_violation_fine2.FID NOT IN 
	(SELECT FineID FROM receipt1)
) as x GROUP BY DriverCarID;
*/
/*3*/
/*
SELECT TOP (1) DriverCarID, ViolationID, MAX(Violation_Car_Count) AS Max_Violation_Count
FROM
(SELECT ViolationID, DriverCarID, COUNT(ViolationID) AS Violation_Car_Count
From(
	SELECT fine1.ViolationID, fine2.DriverCarID FROM
	fine1 JOIN fine2
	ON fine1.FID = fine2.FID) AS violation_fine2 WHERE violation_fine2.DriverCarID = N'۴۵۶۴۵۱۱ر' GROUP BY ViolationID, DriverCarID)
As x GROUP BY DriverCarID, ViolationID ORDER BY Max_Violation_Count DESC
*/
/*5 DESC*/
/*
select * FROM
(SELECT * FROM
fine1 JOIN violation
ON fine1.ViolationID = violation.VID) as x
JOIN fine2 ON x.FID = fine2.FID ORDER BY Amount DESC
*/
/*5 ASC*/
/*
SELECT * FROM
(SELECT * FROM
fine1 JOIN violation
ON fine1.ViolationID = violation.VID) as x
JOIN fine2 ON x.FID = fine2.FID ORDER BY Amount ASC
*/
/*6*/
/*
SELECT * FROM
(SELECT fine1.ViolationID, fine2.DriverCarID, fine2.ViolatioDate, fine2.FID  FROM
fine1 JOIN fine2
ON fine1.FID=fine2.FID) as x
WHERE x.FID NOT IN
(SELECT FineID FROM receipt1)
*/
/*7*/
/*
SELECT receipt.FineID, receipt.ReceiptID, receipt.PaymentDate, receipt.PayNum, violation.Amount FROM
(SELECT receipt1.FineID, receipt1.ReceiptID, receipt2.PaymentDate, receipt2.PayNum, receipt1.ViolationID
FROM receipt1 JOIN receipt2
ON receipt1.ReceiptID = receipt2.RID) AS receipt
JOIN violation ON receipt.ViolationID = violation.VID
WHERE receipt.FineID = 43102
*/
/*8*/
/*
SELECT sms.SmsID, sms.FineID, sms.Text, sms.SendTime, fine2.DriverNID FROM
(SELECT sms1.SmsID, sms1.FineID, sms2.Text, sms2.SendTime FROM
sms1 join sms2
ON sms1.SmsID = sms2.SMSID) AS sms
JOIN fine2 ON sms.FineID = fine2.FID
WHERE fine2.DriverNID = 1010101010 AND sms.SendTime BETWEEN '1400-01-12' AND '1400-08-10'
*/
/*10*/
/*
SELECT * FROM
(SELECT staff_NID.Address, staff_NID.HeadquartersID, staff_NID.Firstname, staff_NID.Lastname, staff_NID.Email, staff_NID.NID, staff_SID.SID
FROM staff_NID JOIN staff_SID ON staff_NID.NID = staff_SID.NationalID) AS staff
WHERE staff.SID IN
(SELECT StaffID FROM maintenance1 WHERE CameraID = 23232)
*/
/*
SELECT fine1.FID, fine1.CameraID, fine1.CameraID, fine2.DriverCarID, fine2.DriverNID, fine2.ViolatioDate
FROM fine1 JOIN fine2 ON fine1.FID = fine2.FID WHERE fine2.DriverNID = 1010101010 AND fine2.ViolatioDate BETWEEN '1400-01-12' AND '1400-08-10'
*/
-- Count total properties
SELECT COUNT(*) FROM luxury_properties;

-- Average ticket price per builder
SELECT Developer_Name, AVG(Ticket_Price_Cr) AS Avg_Ticket
FROM luxury_properties
GROUP BY Developer_Name;

-- Booking count by micro-market
SELECT Micro_Market, COUNT(*) AS Booking_Count
FROM luxury_properties
WHERE Booking_Flag = 1
GROUP BY Micro_Market;

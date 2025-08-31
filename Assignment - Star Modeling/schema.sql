CREATE DATABASE Adventure;
USE Adventure;

CREATE TABLE MyDimDate (
    Date DATE PRIMARY KEY,
    Day INT NOT NULL,
    DayOfWeek VARCHAR(10),
    Month INT NOT NULL,
    MonthName VARCHAR(30),
    Quarter INT NOT NULL,
    Year INT NOT NULL
);

CREATE TABLE MyDimWaste (
    WasteKey INT PRIMARY KEY,
    WasteType VARCHAR(50),
    Description VARCHAR(255)
);

CREATE TABLE MyDimZone (
    ZoneKey INT PRIMARY KEY,
    ZoneName VARCHAR(50),
    City VARCHAR(50),
    Region VARCHAR(50)
);

CREATE TABLE MyFactsTrips (
    TripID INT PRIMARY KEY,
    DateKey Date NOT NULL,
    WasteKey INT,
    ZoneKey INT,
    WasteCollected INT,
    Tons DECIMAL(10, 2),
    FOREIGN KEY (DateKey) REFERENCES MyDimDate(Date),
    FOREIGN KEY (WasteKey) REFERENCES MyDimWaste(WasteKey),
    FOREIGN KEY (ZoneKey) REFERENCES MyDimZone(ZoneKey)
);
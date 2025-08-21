/*markdown
## Laboratory Schema
*/

CREATE DATABASE Laboratory;

USE Laboratory;

CREATE TABLE IF NOT EXISTS Scientists (
    SSN INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Projects (
    Code VARCHAR(255) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Hours INT NOT NULL
)

CREATE TABLE IF NOT EXISTS AssignedTo (
    Scientist INT,
    Project VARCHAR(255),
    FOREIGN KEY(Scientist) REFERENCES Scientists(SSN),
    FOREIGN KEY(Project) REFERENCES Projects(Code),
    PRIMARY KEY(Scientist, Project)
)

-- Scientist Data

INSERT INTO Scientists (Name)
VALUES
    ('Dr. Ahmed Ali'),
    ('Dr. Sara Hassan'),
    ('Dr. Omar Khaled'),
    ('Dr. Mariam Youssef'),
    ('Dr. Youssef Nabil');

-- Insert Projects

INSERT INTO Projects (Code, Name, Hours)
VALUES
    ('P101', 'Quantum Research', 120),
    ('P102', 'AI Development', 200),
    ('P103', 'Space Exploration', 150),
    ('P104', 'Genetics Study', 100),
    ('P105', 'Robotics Project', 180);


-- Insert Assign To

INSERT INTO AssignedTo (Scientist, Project)
VALUES
    (1, 'P101'),
    (1, 'P102'),
    (2, 'P103'),
    (3, 'P101'),
    (3, 'P104'),
    (4, 'P105'),
    (5, 'P102'),
    (5, 'P103');



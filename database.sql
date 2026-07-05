CREATE DATABASE IF NOT EXISTS task_management_system;
USE task_management_system;

DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS login;

CREATE TABLE login (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role ENUM('admin', 'manager') NOT NULL
);

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department VARCHAR(80) NOT NULL
);

CREATE TABLE task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    title VARCHAR(120) NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_task_employee
        FOREIGN KEY (employee_id)
        REFERENCES employee(id)
        ON DELETE CASCADE
);

INSERT INTO login (username, password, role) VALUES
('admin', 'admin123', 'admin'),
('manager', 'manager123', 'manager');

INSERT INTO employee (employee_name, email, department) VALUES
('Rahul Sharma', 'rahul@example.com', 'Operations'),
('Sneha Verma', 'sneha@example.com', 'Support'),
('Amit Patel', 'amit@example.com', 'Data Entry'),
('Priya Singh', 'priya@example.com', 'Documentation');

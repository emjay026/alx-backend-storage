-- Create the users table if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    -- Unique identifier for each user; auto-increments with each new entry
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- User's email address; must be unique and cannot be null
    email VARCHAR(255) NOT NULL UNIQUE,
    
    -- User's name; can be null
    name VARCHAR(255),
    
    -- User's country; must be one of the specified values and cannot be null
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

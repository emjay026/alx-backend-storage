-- Create the names table if it does not already exist
CREATE TABLE IF NOT EXISTS names (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Add a generated column for the first letter of the name
ALTER TABLE names
ADD first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

-- Create an index on the generated column first_letter
CREATE INDEX idx_name_first ON names(first_letter);

-- Add a generated column for the first letter of the name
ALTER TABLE names
ADD first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

-- Create an index on both the name and first_letter columns
CREATE INDEX idx_name_first ON names(name, first_letter);

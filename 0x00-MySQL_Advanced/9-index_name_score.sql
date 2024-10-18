-- Add a generated column for the first letter of the name
ALTER TABLE names
ADD first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

-- Create an index on both the first_letter and score columns
CREATE INDEX idx_name_first_score ON names(first_letter, score);

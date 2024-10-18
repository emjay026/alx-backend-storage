-- Create an index on both the name and first_letter columns
CREATE INDEX idx_name_first ON names(name, first_letter);

-- Create the view to list all students who need a meeting
CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80  -- Score is strictly under 80
AND (last_meeting IS NULL OR last_meeting < NOW() - INTERVAL 1 MONTH);  -- No last_meeting or more than 1 month ago

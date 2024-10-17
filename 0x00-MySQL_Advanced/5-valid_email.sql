-- Create the trigger to reset valid_email when email is changed
DELIMITER $$

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;                      -- Reset valid_email to false (0) when email is changed
    END IF;
END$$

DELIMITER ;


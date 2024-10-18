-- This function safely divides two integers.
-- It takes two integer arguments: a and b.
-- It returns a / b or 0 if b == 0.

DELIMITER $$

CREATE FUNCTION SafeDiv(
    a INT,
    b INT
) RETURNS INT
BEGIN
    IF b = 0 THEN
        RETURN 0;  -- Return 0 if the second number (b) is zero
    ELSE
        RETURN a / b;  -- Otherwise, return the division result
    END IF;
END$$

DELIMITER ;

-- This procedure computes and stores the average score for a specified user.
-- It takes user_id as an input parameter, which should be linked to an existing user in the users table.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;  -- Declare a variable to hold the average score

    -- Calculate the average score for the user from the corrections table
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;  -- Use the input user_id to filter

    -- Update the average_score in the users table
    UPDATE users
    SET average_score = COALESCE(avg_score, 0)  -- Set to 0 if avg_score is NULL
    WHERE id = user_id;  -- Update the specific user based on user_id
END$$

DELIMITER ;


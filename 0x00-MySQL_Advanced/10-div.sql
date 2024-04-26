-- Write a SQL script that creates a function SafeDiv that divides (and 
--      You must create a function
--      The function SafeDiv takes 2 arguments:
--           a, INT
--          b, INT
-- And returns a / b or 0 if b == 0
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT DEFAULT 0;

    IF b != 0 THEN
        SET result = a / b;
    END IF;
    RETURN result;
END $$
DELIMITER ;

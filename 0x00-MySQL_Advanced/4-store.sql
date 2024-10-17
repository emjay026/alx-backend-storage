-- Create the trigger to decrease the item quantity after a new order is added
DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number               -- Decrease quantity by the ordered number
    WHERE name = NEW.item_name;                        -- Match the item_name in orders
END$$

DELIMITER ;

-- Create the trigger to decrease the item quantity after a new order is added
DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.order_quantity         -- Decrease quantity by the ordered amount
    WHERE item_id = NEW.item_id;                          -- Match the item_id in orders
END$$

DELIMITER ;

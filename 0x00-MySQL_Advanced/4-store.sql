-- create a trigger that will reduce the quantity of item
CREATE TRIGGER reduce_quant
AFTER INSERT ON order
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE name=NEW.item_name;

USE web;

CREATE TABLE users
(
    username VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100)
);

CREATE TABLE products
(
    name VARCHAR(100),
    content VARCHAR(1000)
);

INSERT INTO users VALUES ("guest", "123456"), ("guest2", "123456");

INSERT INTO products (name, content) VALUES 
("Laptop", "A high-performance laptop with 16GB RAM and 512GB SSD."),
("Smartphone", "A latest model smartphone with a 6.5-inch display and 128GB storage."),
("Headphones", "Noise-cancelling over-ear headphones with Bluetooth connectivity."),
("Smartwatch", "A smartwatch with fitness tracking and heart rate monitoring features."),
("Tablet", "A lightweight tablet with 10.1-inch display and 64GB storage."),
("Camera", "A digital camera with 24.1MP resolution and 4K video recording."),
("Printer", "A wireless printer with scanning and copying capabilities."),
("Monitor", "A 27-inch 4K UHD monitor with HDR support."),
("Keyboard", "A mechanical keyboard with customizable RGB lighting."),
("Mouse", "A wireless mouse with ergonomic design and adjustable DPI settings.");

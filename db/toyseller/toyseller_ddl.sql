CREATE DATABASE toy_sellers;

grant all privileges on toy_sellers.* to 'webapp'@'%';
flush privileges;

USE toy_sellers;



CREATE TABLE toy (
  toy_id integer AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(255) UNIQUE NOT NULL,
  engagement_level INT,
  age_range INT,
  description VARCHAR(255),
  price DECIMAL(3, 2) NOT NULL,
  safety_rating INT,
  suitability_for_special_needs MEDIUMTEXT,
  material_type VARCHAR(255),
  educational_value VARCHAR(255),
  category VARCHAR(255),
  PRIMARY KEY (toy_id)
);

CREATE TABLE customer (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  street_address VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  zip_code VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  accessibility_needs VARCHAR(255) NOT NULL,
  cust_role VARCHAR(255) NOT NULL,
  children_ages VARCHAR(255),
  children_interests MEDIUMTEXT
);

CREATE TABLE environmental_certification (
  environmental_value INT,
  certification_description mediumtext,
  certification_id INT AUTO_INCREMENT,
  certification_name VARCHAR(50) NOT NULL,
  toy_id INT,
  PRIMARY KEY (certification_id),
  FOREIGN KEY (toy_id) REFERENCES toy (toy_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE toy_usage_suggestion (
  age_rating INT NOT NULL,
  suggestion_id INT AUTO_INCREMENT,
  duration INT,
  activity_type VARCHAR(50) NOT NULL,
  toy_id INT,
  PRIMARY KEY (suggestion_id),
  FOREIGN KEY (toy_id) REFERENCES toy (toy_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE toy_safety_information (
  safety_id INT AUTO_INCREMENT,
  safety_features VARCHAR(50) NOT NULL,
  recommended_age INT,
  materials_used VARCHAR(50),
  toy_id INT,
  PRIMARY KEY (safety_id),
  FOREIGN KEY (toy_id) REFERENCES toy(toy_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE gift_wrapping_service (
  service_id INT AUTO_INCREMENT NOT NULL,
  custom_message TEXT,
  wrapping_options ENUM('Classic Red', 'Elegant Gold', 'Festive Green', 'Glossy Paper',
  'Matte Paper', 'Recycled Paper', 'Fabric Wrap') NOT NULL,
  toy_id INT NOT NULL,
  PRIMARY KEY(service_id),
  CONSTRAINT FOREIGN KEY (toy_id) REFERENCES toy(toy_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE `order` (
  order_id INT NOT NULL AUTO_INCREMENT,
  toy_id INT NOT NULL,
  customer_id INT NOT NULL,
  date DATE,
  quantity INT,
  delivery_status ENUM('delivered', 'pickup ready', 'returned', 'pending', 'in transit'),
  price_per_item DECIMAL(3, 2),
  total_price DECIMAL(5, 2) GENERATED ALWAYS AS (price_per_item * quantity) STORED,
  PRIMARY KEY (order_id),
  CONSTRAINT FOREIGN KEY (toy_id)
                        REFERENCES toy(toy_id)
                        ON UPDATE cascade ON DELETE restrict,
  CONSTRAINT FOREIGN KEY (customer_id)
                        REFERENCES customer(customer_id)
                        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE feedback (
  feedback_id INT AUTO_INCREMENT NOT NULL,
  toy_id INT NOT NULL,
  customer_id INT NOT NULL,
  date DATE,
  rating INT,
  comment TEXT,
  PRIMARY KEY (feedback_id),
  CONSTRAINT FOREIGN KEY (toy_id) REFERENCES toy(toy_id)
  ON UPDATE cascade ON DELETE restrict,
  CONSTRAINT FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE customer_support (
  support_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  query_type VARCHAR(255) NOT NULL,
  contact_method VARCHAR(255) NOT NULL,
  resolution_status VARCHAR(255) NOT NULL,
  CONSTRAINT FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE toy_manufacturer (
  manufacturer_id int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `location` varchar(255) NOT NULL,
  sustainability_score int NOT NULL,
  environmental_policies varchar(255) NOT NULL,
  toy_id INT,
  FOREIGN KEY (toy_id) REFERENCES toy(toy_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE customization_options(
  option_id int UNSIGNED AUTO_INCREMENT,
  customization_type varchar(255),
  toy_id int,
  PRIMARY KEY (option_id, toy_id),
  FOREIGN KEY (toy_id) REFERENCES toy(toy_id)
  ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE customer_interface (
  interface_id int PRIMARY KEY AUTO_INCREMENT,
  ease_of_use VARCHAR(255) NOT NULL,
  accessibility_features TEXT NOT NULL
);

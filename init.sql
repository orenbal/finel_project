CREATE DATABASE IF NOT EXISTS cat_gifs;
USE cat_gifs;

CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_url VARCHAR(255) NOT NULL
);

INSERT INTO images (image_url) VALUES
('https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif'),
('https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif'),
('https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif');
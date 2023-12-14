CREATE DATABASE donutslupore;

use donutslupore;

create table usuario (
nome varchar(255),
email varchar(255) primary key,
senha varchar(255));
select * from usuario;


CREATE TABLE produtos (
    id INT NOT NULL AUTO_INCREMENT, 
    tipo VARCHAR(45) NOT NULL, 
    nome VARCHAR(45) NOT NULL, 
    imagem VARCHAR(80) NOT NULL, 
    preco DECIMAL (5,2) NOT NULL, 
PRIMARY KEY (id));

select * from produtos;


INSERT INTO produtos (tipo, nome, imagem, preco) VALUES ('Donuts', 'Donuts de Caramelo', 'donutscaramelo.jpg', 6.00);
INSERT INTO produtos (tipo, nome, imagem, preco) VALUES ('Donuts', 'Donuts de Chocolate', 'donutschocolate.jpg', 6.00);
INSERT INTO produtos (tipo, nome, imagem, preco) VALUES ('Donuts', 'Donuts de Morango', 'donutsmorango.jpg', 6.50);


select * from produtos;

update produtos set imagem = '../imagemldi/donutscaramelo.jpg' where id = 6;
update produtos set imagem = '../imagemldi/donutschocolate.jpg' where id = 13;
update produtos set imagem = '../imagemldi/donutsmorango.jpg' where id = 5;

select * from produtos;
#delete from produtos where id >1;
#update produtos set imagem = concat("../imagemldi/donutscaramelo.jpg",imagem) where id= 1;

select * from usuario;

alter table usuario add perfil varchar(50) default(0);
update usuario set perfil = 'admin' where email = 'abc@ifsp.edu.br';

#drop database donutslupore;

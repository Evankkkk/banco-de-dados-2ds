CREATE TABLE Clientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Data_Cadastro DATE NOT NULL
);


INSERT INTO Clientes (ID, Nome, Email, Data_Cadastro)
VALUES 
(2, 'Carlos Silva', 'carlos.silva@example.com', '2023-02-20'),
(3, 'Beatriz Souza', 'beatriz.s@example.com', '2023-03-10');


SELECT * FROM Clientes;

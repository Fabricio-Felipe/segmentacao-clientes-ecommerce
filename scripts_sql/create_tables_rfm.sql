

CREATE TABLE tb_vendas_brutas (
    id_cliente VARCHAR(100),
    id_pedido VARCHAR(100),
    data_compra DATETIME2(7),
    valor_total DECIMAL(10,2)
);


CREATE TABLE tb_resultado_rfm (
    customer_unique_id VARCHAR(100),
    Valor DECIMAL(10,2),
    Frequencia INT,
    Recencia INT,
    R_Score INT,
    F_Score INT,
    M_Score INT
);
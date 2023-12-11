def calcula_juros_compostos(valor_mensal, taxa_juros, quant_meses):
    valor_atual=0
    
    for i in range(1, quant_meses+1):
        
        valor_atual+=valor_mensal
        valor_atual+=valor_atual*(taxa_juros/100)

    return valor_atual
    
print(calcula_juros_compostos(100, 1, 12))
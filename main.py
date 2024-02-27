def geradorPix():

    chavePix = input('Digite a chave pix: ')
    tamChavePix = len(chavePix)

    if tamChavePix < 10:
        tamChavePix = f'0{tamChavePix}'

    valor = input('Digite o valor: ')
    tamValor = len(valor)

    if ',' in valor:
        valor = valor.replace(',','.')
    if tamValor < 10:
        tamValor = f'0{tamValor}'

    recebedor = input('Digite o nome do recebedor: ')
    tamRecebedor = len(recebedor)

    if tamRecebedor < 10:
        tamRecebedor = f'0{tamRecebedor}'

    cidade = input('Digite a cidade: ')
    tamCidade = len(cidade)

    if tamCidade < 10:
        tamCidade = f'0{tamCidade}'

    merchantAccount = len(f'0014br.gov.bcb.pix01{tamChavePix}{chavePix}')

    codPix = f'00020126{merchantAccount}0014br.gov.bcb.pix01{tamChavePix}{chavePix}52040000530398654{tamValor}{valor}5802BR59{tamRecebedor}{recebedor}60{tamCidade}{cidade}62070503***6304'
    codPix = codPix+str(crcChecksum(codPix))


    return codPix


def crcChecksum(string):


    def charCodeAt(string, i):
        return ord(string[i])

    crc = 0xFFFF
    strlen = len(string)
    for c in range(strlen):
        crc ^= charCodeAt(string, c) << 8
        for i in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc = crc << 1

    hex_value = crc & 0xFFFF
    hex_value = hex(hex_value)[2:]
    hex_value = hex_value.upper()
    hex_value = hex_value.zfill(4)

    return hex_value


if __name__ == '__main__':
    copiaCola = geradorPix()
    print(copiaCola)
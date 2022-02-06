class AddressView:
    def view_register_address(self):
        cep = input('CEP: ')
        street = input('Rua: ')
        number = input('Numero: ')
        complement = input('Complemento: ')

        return { 
            "cep": cep, 
            "street": street, 
            "number": number, 
            "complement": complement
        }
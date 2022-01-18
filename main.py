from accountbank import accountbank

account1 = accountbank(0.05, 1000)
account2 = accountbank(0.12, 2000)

account1.depósito(500).depósito(500).depósito(500).retiro(100).generar_interés().mostrar_info_cuenta()
account2.depósito(500).depósito(300).retiro(100).retiro(200).retiro(500).retiro(500).generar_interés().mostrar_info_cuenta()

accountbank.mostrar_informacion_banco()

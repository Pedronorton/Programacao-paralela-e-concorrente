'''
Código retirado de: https://github.com/bragisig/python-sleeping-barber/blob/master/sleeping_barber.py
'''
from threading import Thread, Lock, Event
import time
import random
 
mutex = Lock()
 
# algumas constantes, que sao o tempo de espera do cliente e o de duração do corte, em segundos
customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15

customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15
 
'''
classe principal
'''
 
 
class Fila:
    filaFuncionario = []
 
    #construtor, que passa por parâmetro o barbeiro e a quantidade de cadeira para os clientes aguardarem
    def __init__(self, id, Funcionario):
        self.id = id
        self.Funcionario = Funcionario
        self.numMaxClientes = Funcionario.numMaxClientes
        print('A fila está iniciando com no máximo {0} clientes'.format(self.numMaxClientes))
        print('Intervalo mínimo de inscrição {0}'.format(customerIntervalMin))
        print('Intervalo mínimo de inscrição {0}'.format(customerIntervalMax))
        # print('Mínimo tempo de corte {0}'.format(haircutDurationMin))
        # print('Máximo tempo de corte {0}'.format(customerIntervalMax))
        print('---------------------------------------')
    
    def getTamanhoFila(self):
        return self.filaFuncionario
 
    # inicia a barbearia
    def open_shop(self):
        print('A fila do funcionário {0} está aberta'.format(self.Funcionario.id))
        working_thread = Thread(target=self.barber_go_to_work) 
        working_thread.start() #inicia a thread do barbeiro
 
    def barber_go_to_work(self):
        print('fila vai funcionar')
        while True:
            mutex.acquire() #realiza o bloqueio
 
            #verifica se há clientes esperando
            if len(self.filaFuncionario) > 0:
                c = self.filaFuncionario[0]
                del self.filaFuncionario[0]
                mutex.release()
                self.Funcionario.cut_hair(c)
            else:
                mutex.release()
                # print('Aaaah está tudo feito, vou dormir um pouco')
                self.Funcionario.sleep()#caso nao haja cliente, barbeiro volta a dormir
                # print('Barbeiro acordou !')
 
    # #cliente entra na barbearia
    def enter_barber_shop(self, cliente):
        print("cliente {0} entrando na fila {1}".format(cliente.id, self.id ))
        mutex.acquire() #faz o bloqueio
 
        #verifica se há cadeiras vagas para aguardar
        if len(self.filaFuncionario) == self.numMaxClientes:
            print('Esperando a fila está cheia, {0} está saindo.'.format(cliente.name))
            mutex.release()
        else:
            print('{0} está esperando para fazer a inscrição'.format(cliente.name))
            self.filaFuncionario.append(c) #caso há cadeiras para sentar, entra pra lista de espera
            mutex.release() #desbloqueia
            self.Funcionario.wake_up() #acorda o barbeiro
 
 
class Cliente:
    def __init__(self, id, name, cpf):
        self.id = id
        self.name = name
        self.cpf = cpf
    
    eventoAtividadeCliente = Event()

    def sleep(self):
        self.eventoAtividadeCliente.wait()
 
    def wake_up(self):
        self.eventoAtividadeCliente.set()
 
    def cut_hair(self, customer):
        # Set barber as busy
        self.eventoAtividadeCliente.clear()
 
        print('{0} está fazendo inscricao'.format(customer.name))
 
        random_hair_cutting_time = random.randrange(haircutDurationMin, haircutDurationMax + 1)
        time.sleep(random_hair_cutting_time)
        print('{0} fez sua inscrição '.format(customer.name))

        
 
class Funcionario:
    def __init__(self,id, name, numMaxClientes):
        self.id = id
        self.name = name
        self.numMaxClientes = numMaxClientes
        self.filaClientes = []

    eventoAtividadeFuncionario = Event()
 
    def sleep(self):
        self.eventoAtividadeFuncionario.wait()
 
    def wake_up(self):
        self.eventoAtividadeFuncionario.set()
 
    def cut_hair(self, customer):
        # Set barber as busy
        self.eventoAtividadeFuncionario.clear()
 
        # print('{0} está cortando o cabelo'.format(customer.name))
 
        random_hair_cutting_time = random.randrange(haircutDurationMin, haircutDurationMax + 1)
        time.sleep(random_hair_cutting_time)
        print('o funcionario {0} terminou a inscrição do cliente {1} '.format(self.name, customer.name))
 
 
if __name__ == '__main__':
    print("Bem vindo ao sistema inicial de sorteios do supermercado REX !")
    numFuncionarios = int(input('Entre com a quantidade de funcionarios: '))
    numClientes =  int(input('Entre com a quantidade de clientes: '))
    numClientesAtendidos = int(input('Entre com a quantidade de clientes atendidos por cada funcionário: '))
    numRodadas = input('Entre com a quantidade de rodadas de prêmios: ')

    listaClientes = list([])
    listaFuncionarios = list([])
    listaFilas = list([])

    for i in range(numClientes) :
        x = random.randrange(0, 100)
        listaClientes.append(Cliente(i, 'User'+str(i), str(i)+'#'+str(x) ))
    
    for i in range(numFuncionarios) :
        listaFuncionarios.append(Funcionario(i, 'Funcionario '+str(i), numClientesAtendidos))

    index = 0
    for funcionario in listaFuncionarios:
        listaFilas.append(Fila(index, funcionario))
        index += 1 
    
    for fila in listaFilas:
        fila.open_shop()
    
    
    #Primeiramente há o loteamento das filas
    for i in range (numClientesAtendidos*numFuncionarios):
        if(len(listaClientes)!=0):
            c = listaClientes.pop()
            listaFilas[i%numFuncionarios].enter_barber_shop(c)
        


    indexFila = 0
    while len(listaClientes) > 0:
        print("here")
        c = listaClientes.pop()
        for fila in listaFilas:
            # print(fila.getTamanhoFila)
            if len(fila.getTamanhoFila()) < numClientesAtendidos:
                listaFilas[indexFila].enter_barber_shop(c)
                break
            indexFila += 1
        indexFila = 0
    #     customerInterval = random.randrange(customerIntervalMin, customerIntervalMax + 1)
    #     time.sleep(customerInterval)
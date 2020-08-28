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
 
'''
classe principal
'''
 
 
class BarberShop:
    waitingCustomers = []
 
    #construtor, que passa por parâmetro o barbeiro e a quantidade de cadeira para os clientes aguardarem
    def __init__(self, barber, number_of_seats):
        self.barber = barber
        self.numberOfSeats = number_of_seats
        print('BarberShop initilized with {0} seats'.format(number_of_seats))
        print('Customer min interval {0}'.format(customerIntervalMin))
        print('Customer max interval {0}'.format(customerIntervalMax))
        print('Haircut min duration {0}'.format(haircutDurationMin))
        print('Haircut max duration {0}'.format(customerIntervalMax))
        print('---------------------------------------')
 
    #inicia a barbearia
    def open_shop(self):
        print('Barber shop is opening')
        working_thread = Thread(target=self.barber_go_to_work) 
        working_thread.start() #inicia a thread do barbeiro
 
    def barber_go_to_work(self):
        while True:
            mutex.acquire() #realiza o bloqueio
 
            #verifica se há clientes esperando
            if len(self.waitingCustomers) > 0:
                c = self.waitingCustomers[0]
                del self.waitingCustomers[0]
                mutex.release()
                self.barber.cut_hair(c)
            else:
                mutex.release()
                print('Aaah, all done, going to sleep')
                barber.sleep()#caso nao haja cliente, barbeiro volta a dormir
                print('Barber woke up')
 
    #cliente entra na barbearia
    def enter_barber_shop(self, customer):
        mutex.acquire() #faz o bloqueio
        print('>> {0} entered the shop and is looking for a seat'.format(customer.name))
 
        #verifica se há cadeiras vagas para aguardar
        if len(self.waitingCustomers) == self.numberOfSeats:
            print('Waiting room is full, {0} is leaving.'.format(customer.name))
            mutex.release()
        else:
            print('{0} sat down in the waiting room'.format(customer.name))
            self.waitingCustomers.append(c) #caso há cadeiras para sentar, entra pra lista de espera
            mutex.release() #desbloqueia
            barber.wake_up() #acorda o barbeiro
 
 
class Customer:
    def __init__(self, name):
        self.name = name
 
 
class Barber:
    barberWorkingEvent = Event()
 
    def sleep(self):
        self.barberWorkingEvent.wait()
 
    def wake_up(self):
        self.barberWorkingEvent.set()
 
    def cut_hair(self, customer):
        # Set barber as busy
        self.barberWorkingEvent.clear()
 
        print('{0} is having a haircut'.format(customer.name))
 
        random_hair_cutting_time = random.randrange(haircutDurationMin, haircutDurationMax + 1)
        time.sleep(random_hair_cutting_time)
        print('{0} is done'.format(customer.name))
 
 
if __name__ == '__main__':
 
    customers = list([])
    customers.append(Customer('Bragi'))
    customers.append(Customer('Auja'))
    customers.append(Customer('Iris'))
    customers.append(Customer('Axel'))
    customers.append(Customer('Andrea'))
    customers.append(Customer('Agnar'))
    customers.append(Customer('Mamma'))
    customers.append(Customer('Solla'))
    customers.append(Customer('Olla'))
 
    barber = Barber()
 
    barberShop = BarberShop(barber, 3)
    barberShop.open_shop()
 
    while len(customers) > 0:
        c = customers.pop()
        barberShop.enter_barber_shop(c)
        customerInterval = random.randrange(customerIntervalMin, customerIntervalMax + 1)
        time.sleep(customerInterval)
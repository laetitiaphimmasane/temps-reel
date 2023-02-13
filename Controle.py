import datetime
import time
import threading


#Variables globales
tank = 0
stock_1 = 0
stock_2 = 0
nb_motor_wheels = 0
current_time = 0

class my_task():

	name = None
	priority = -1
    state = None
    production_oil = 0
	period = -1
	execution_time = -1
    
	def __init__(self, name, priority, period, execution_time, state, production_oil, last_execution_time):
		self.name = name
		self.priority = priority
		self.period = period
        self.execution_time = execution_time
        self.state = state
        self.production_oil = production_oil
        self.last_execution_time = last_execution_time


	def run(self):

        global current_time
		self.last_execution_time = datetime.datetime.now() 	# Update last_execution_time
		print("\t" + self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ")")

        current_time += self.execution_time
		time.sleep(self.execution_time)
        self.state = 'waiting'

        print("\t" + self.name + ' a un état ' + self.state)
        print("\t Current time : " + current_time)
		print("\t" + self.name + " : Ending task (" + self.last_execution_time.strftime("%H:%M:%S") + ")")





if __name__ == '__main__':

    # Instanciation of task objects
    pump_1 = my_task('PUMP 1', 1, 5, 2, 0, 'waiting', 10, 0)
    pump_2 = my_task('PUMP 2', 2, 15, 3, 0, 'waiting', 20, 0)

    machine_1 = my_task('MACHINE 1', 3, 5, 5, 0, 'waiting', 25, 0)
    machine_2 = my_task('MACHINE 2', 4, 5, 3, 0, 'waiting', 5, 0)

    global tank
    global stock_1
    global stock_2
    global nb_motor_wheels

    task_list = [pump_1, pump_2, machine_1, machine_2]
    tache_courante = my_task('tache_courante', -1, -1, -1, 'blocked', -1, -1)
    time_now = datetime.datetime.now()

    #Rules
    while time_now < time_now() + datetime.datetime.now().minute : #exécution pendant une minute 
        for task in task_list:
            if tank < 50: #si le tank n'est pas plein
                machine_1.state = 'blocked'
                machine_2.state = 'blocked'

                dice = random.randint(1, 2)
                if dice == 1 :
                    tache_courante = pump_1
                elif dice == 2:
                    tache_courante = pump_2
                tank += tache_courante.production_oil
            else:
                pump_1.state = 'blocked'
                pump_2.state = 'blocked'

                if (stock_2 / 4 >  stock_1): #machine_1 est prioritaire
                    tache_courante = machine_1
                elif (stock_2/ 4 < stock_1): #machine_2 est prioritaire
                    tache_courante = machine_2
                tank += tache_courante.production_oil
            tache_courante.state = 'running'
        
        run(tache_courante)

    nb_motor_wheels = stock_1 ==1 & stock_2 ==4 %2    
    print('Le nombre de [motor + 4 wheels] produit est de ' + nb_motor_wheels + ' avec un tank de ' + tank)
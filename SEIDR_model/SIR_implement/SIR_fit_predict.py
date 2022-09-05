import numpy as np
import pandas as pd
import datetime
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class estimationInfectionProb():
    def __init__(self, infectionData, startTime, estUsedTimeBox: list, nContact, gamma):
        self.startTime = startTime
        self.estUsedTimeIndexBox = [(t - startTime).days for t in estUsedTimeBox]
        self.timeRange = np.array([i for i in range(self.estUsedTimeIndexBox[0], self.estUsedTimeIndexBox[1] + 1)])
        self.nContact, self.gamma = nContact, gamma
        self.infectionData = infectionData
        self.dataStartTimeStep = self.estUsedTimeIndexBox[0]
    
    def setInitSolution(self, x0):
        self.x0 = x0
        
    def costFunction(self, infectionProb):
        res = np.array(np.exp((infectionProb * self.nContact - self.gamma) * self.timeRange) - self.infectionData.loc[(self.timeRange - self.dataStartTimeStep),'Confirmed'])
        return (res**2).sum() / self.timeRange.size
    
    def optimize(self):
        self.solution = minimize(self.costFunction, self.x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
        print('infection probaility: ', self.solution.x)
        return self.getSolution()
        # return None
    
    def getSolution(self):
        return self.solution.x
    
    def getBasicReproductionNumber(self):
        self.basicReproductionNumber = self.nContact * self.solution.x[0] / (self.gamma)
        # print(self.solution)
        print("basic reproduction number:", self.basicReproductionNumber)
        return self.basicReproductionNumber

class SIRModel():
    def __init__(self, N, beta, gamma, infectionProb):
        self.beta, self.gamma, self.N = beta, gamma, N
        self.t = np.linspace(0, 360, 361)
        self.infectionProb = infectionProb
        self.setInitCondition()
    
    def odeModel(self, population, t):
        diff = np.zeros(3)
        s,i,r = population
        diff[0] = - self.beta * s * i / self.N
        diff[1] = self.beta * s * i / self.N - self.gamma * i
        diff[2] = self.gamma * i
        return diff
    
    def setInitCondition(self):
        self.populationInit = [self.N - 1, 1, 0]
        
    def solve(self):
        self.solution = odeint(self.odeModel,self.populationInit,self.t)
    
    def report(self):
        #plt.plot(self.solution[:,0],color = 'darkblue',label = 'Susceptible',marker = '.')
        plt.plot(self.solution[:,1],color = 'orange',label = 'Infection',marker = '.')
        plt.plot(self.solution[:,2],color = 'green',label = 'Recovery',marker = '.')
        plt.title('SIR Model' + ' infectionProb = '+ str(self.infectionProb))
        plt.legend()
        plt.xlabel('Day')
        plt.ylabel('Number of people')
        plt.show()



def main():
    df = pd.read_csv('D:\Data\Mylecture\DATA7901\Cases_Dataset\covid_19_data.csv')
    df = df.loc[df['Province/State'] == 'Hubei']
    df.drop(['SNo', 'Province/State', 'Country/Region', 'Last Update'], axis=1, inplace=True)
    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)

    nContact = int(5)
    gamma = 1/14
    startTime = datetime.datetime.strptime('2019-12-08', "%Y-%m-%d")
    estUsedTimeBox = [datetime.datetime.strptime('2020-01-22', "%Y-%m-%d"), datetime.datetime.strptime('2020-03-16', "%Y-%m-%d")]
    estInfectionProb = estimationInfectionProb(df, startTime, estUsedTimeBox, nContact, gamma)

    estInfectionProb.setInitSolution(0.04)
    estInfectionProb.optimize()
    basicRN = estInfectionProb.getBasicReproductionNumber()

if __name__ == '__main__':
    main()
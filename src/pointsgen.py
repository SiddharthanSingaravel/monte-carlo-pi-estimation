import random
from tqdm import tqdm
import pandas as pd

class Points:
    def __init__(self, trials = 100, radius = 0.5, xRange = [0, 1], yRange = [0, 1]):
        self.points = [self.randomPoint(xRange, yRange) for _ in tqdm(range(trials), desc='Generating Points')]
        self.df = pd.DataFrame(self.points, columns=['x', 'y'])
        self.df['inside'] = self.df.apply(lambda x: self.pointInsideCircle(x, radius), axis = 1)
    
    def randomPoint(self, xRange, yRange):
        return [random.uniform(xRange[0], xRange[1]),
                random.uniform(yRange[0], yRange[1])]
    
    def pointInsideCircle(self, point, radius):
        return (point.iloc[0] - radius)**2 + (point.iloc[1] - radius)**2 <= radius**2
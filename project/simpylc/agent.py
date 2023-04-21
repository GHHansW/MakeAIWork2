'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering 

This program is free software.  
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''

import time as tm
import traceback as tb
import math as mt
import sys as ss
import os
import socket as sc

import torch
from torch import nn

ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 

import socket_wrapper as sw
import parameters as pm
from driver import Driver
import pickle


class Agent(Driver):
    def sweep (self):
        if hasattr (self, 'lidarDistances'):
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def input (self):
        sensors = self.socketWrapper.recv ()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
        else:
            self.sonarDistances = sensors ['sonarDistances']

    def predict(self, sonarDistances):
        with open('SDCar.pickle', 'rb') as SDCar:
            self.brain = pickle.load(SDCar)
        
        # steeringAngle
        
        return self.brain.predict(sonarDistances)    
      

    # TODO: Add lidarSweep

    def sonarSweep (self):
        obstacleDistances = [pm.finity for sectorIndex in range (3)]
        obstacleAngles = [0 for sectorIndex in range (3)]
        
        for sectorIndex in (-1, 0, 1):
            sonarDistance = self.sonarDistances [sectorIndex]
            sonarAngle = 2 * self.halfMiddleApertureAngle * sectorIndex
            
            if sonarDistance < obstacleDistances [sectorIndex]:
                obstacleDistances [sectorIndex] = sonarDistance
                obstacleAngles [sectorIndex] = sonarAngle

        if obstacleDistances [-1] > obstacleDistances [0]:
            leftIndex = -1
        else:
            leftIndex = 0
           
        if obstacleDistances [1] > obstacleDistances [0]:
            rightIndex = 1
        else:
            rightIndex = 0
           
        # Call to predict to determine value of self.steeringAngle
        self.steeringAngle = self.predict(sonarDistance)   
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)               

    # TODO: def logLidarTraining (self):

    def logSonarTraining (self):
        sample = [pm.finity for entryIndex in range (pm.sonarInputDim + 1)]

        for entryIndex, sectorIndex in ((2, -1), (0, 0), (1, 1)):
            sample [entryIndex] = self.sonarDistances [sectorIndex]

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)

    def logTraining (self):
        if hasattr (self, 'lidarDistances'):
            self.logLidarTraining ()
        else:
            self.logSonarTraining ()
            
Agent()
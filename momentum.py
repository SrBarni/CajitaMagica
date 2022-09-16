#kg

rocketMass = 1000
propellantMass = 1000
#kg/s
massFlowRate = 2100
#m/s
exhaustVelocity = 3000

def velocity(rocketMass, propellantMass, massFlowRate, exhaustVelocity):
    propllantMomentum = int(massFlowRate * exhaustVelocity)
    velocity = 0
    time = 0
    totalMass= 549054
    for time in range(157):
        def vehicleMass(rocketMass, propellantMass, massFlowRate):
            #mass = int((rocketMass + propellantMass) - time*massFlowRate)
            mass = int((totalMass) - time*massFlowRate)
            #print("time: ", time, "mass: ", mass, "kg")
            return mass

        vehicleMass = vehicleMass(rocketMass, propellantMass, massFlowRate)
       # print(vehicleMass)

        velocity = ((propllantMomentum / vehicleMass) + (velocity/3.6)) * 3.6
        print("time: ", time,"velocity: ", velocity, "km/hr")

velocity(rocketMass, propellantMass, massFlowRate, exhaustVelocity)
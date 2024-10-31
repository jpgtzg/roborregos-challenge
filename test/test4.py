import matplotlib.pyplot as plt
from simple_pid import PID

# Initialize the PID controller
pid = PID(1, 0.1, 0.05, setpoint=1)

# Simulate a system function to update the controlled variable `v`
def update(v, control):
    return v + 0.1 * control

# Set initial value of `v`
v = 0
values = []  # List to store values of `v` over time

# Run the PID control loop for a set number of iterations
for i in range(100):
    # Compute new output from the PID according to the system's current value
    control = pid(v)
    
    # Feed the PID output to the system and get its updated value
    v = update(v, control)
    values.append(v)  # Store the current value of `v`

# Plot the results
plt.plot(values, label="System Value")
plt.axhline(y=pid.setpoint, color='r', linestyle='--', label="Setpoint")
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.title("PID Controller Response")
plt.legend()
plt.show()

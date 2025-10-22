class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.setpoint = setpoint  # Desired value
        self.previous_error = 0
        self.integral = 0
        self.output_limit_min = None  # Optional: Minimum output limit
        self.output_limit_max = None  # Optional: Maximum output limit

    def calculate(self, current_value, dt):
        """
        Calculates the control output based on the current process variable.

        Args:
            current_value: The current measured value of the process variable.
            dt: The time difference since the last calculation (in seconds).

        Returns:
            The calculated control output.
        """
        error = self.setpoint - current_value

        # Proportional term
        P_term = self.Kp * error

        # Integral term
        self.integral += error * dt
        I_term = self.Ki * self.integral

        # Derivative term
        derivative = (error - self.previous_error) / dt
        D_term = self.Kd * derivative

        # Calculate total output
        output = P_term + I_term + D_term

        # Apply output limits if defined
        if self.output_limit_min is not None:
            output = max(output, self.output_limit_min)
        if self.output_limit_max is not None:
            output = min(output, self.output_limit_max)

        # Update previous error for the next iteration
        self.previous_error = error

        return output

# Example Usage:
if __name__ == "__main__":
    # Initialize PID controller with example gains and setpoint
    pid = PIDController(Kp=0.5, Ki=0.1, Kd=0.2, setpoint=10.0)
    pid.output_limit_min = 0.0
    pid.output_limit_max = 20.0

    # Simulate a process
    process_variable = 5.0  # Initial value
    dt = 0.1  # Time step

    print("Time | Process Variable | Control Output")
    print("---------------------------------------")

    for i in range(50):
        control_output = pid.calculate(process_variable, dt)

        # Simulate the effect of the control output on the process variable
        # (This is a simplified model; a real system would be more complex)
        process_variable += (control_output - (process_variable - pid.setpoint) * 0.1) * dt

        print(f"{i*dt:.1f}s | {process_variable:.2f} | {control_output:.2f}")

        # Optional: Stop simulation if close to setpoint
        if abs(pid.setpoint - process_variable) < 0.1 and i > 10:
            print("\nSetpoint reached (approximately).")
            break
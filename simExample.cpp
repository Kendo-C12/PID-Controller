// #include <bits/stdc++.h>
#include <iostream>
#include "pio.cpp"
#include <chrono>
#include <thread>

// using namespace std;

int main() {
    PIDController pid(0.6, 0.4, 0.2); // ตัวอย่าง Kp, Ki, Kd
    double setpoint = 100;            // เป้าหมาย
    double processVar = 0;            // ค่าปัจจุบันของระบบ
    double dt = 0.1;                  // เวลา step (วินาที)

    for (int i = 0; i < 50; i++) {   // simulate 50 step
        double output = pid.update(setpoint, processVar, dt);
        
        // update process variable แบบง่าย
        processVar += output * dt;    // system response
        
        std::cout << "Step " << i 
                  << " | Output: " << output 
                  << " | Process: " << processVar << std::endl;
        
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}

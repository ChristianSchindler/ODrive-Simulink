# ODrive-Simulink - A custom Simulink block with Python

This approach uses Python with the module $odrive$ as backend and the
method from the self-created script is called by Matlab Simulink. This
project is for the ODrive V3 and can be downloaded under the MIT License
at <https://github.com/ChristianSchindler/ODrive-Simulink>. More details
on the implementations are available in the code.

## Why this Approach?

The advantage of Python for this project is that the Python model
$odrive$ is designed by ODrive Robotics Inc and is also actively managed
and updated. Furthermore, a thorough documentation for ODrive is
provided. Another advantage is that we can directly also implement the
configuration work for the projects from the last semester.

## Setup

### Python

You have to install the module $odrive$ with *pip install odrive* for
this project. In the Python controller, you have to set the
$GEAR\_RATIO$ at the beginning of the script (Default = 1 or no gears
available).

### Matlab

Necessary packages: Simulink Steps to activate Python :

-   make sure that Python 3.8 is installed (MATLAB doesn't support any
    more recent version).

-   find where the Python library is located. The path should be :
    */usr/lib/x86_64-linux-gnu/libpython3.8.so*. Import the folder in
    MATLAB path.

-   run following command in MATLAB command shell : *pyenv('Version',
    \"/usr/bin/python3.8\")*

### Simulink

You have to change the Scopes to the expected behaviour of your motor
(Change y-access scaling).

## Usage Guide

### Axis States

We decided to use buttons in Simulink to set the axis stat. For this, it
is only necessary to $Callback Buttons$. Inside we only have to call the
Python functions.

![Set states in Simulink with
buttons](Figure/Set States.png)

### Motor Information's

At all times you can use this information (category: output-name
\<unity\>):

-   Axis State: current_state \<String\>

-   Position: pos \<turn\> (0 $\widehat{=}$ 0°; 0.25 $\widehat{=}$ 90°;
    1 $\widehat{=}$ 360° $\widehat{=}$ 0° and one revolutions $\neq$ 0)

-   Velocity: vel \<turn/s\>

-   Torque: torque \<torque in Nm\>

![Example Output for Position and
Velocity](Figure/Ausgabe Pos + Vel.png)

### Motor Control

For controlling the motor, there are several ways. In this project 3 of
them are implemented (category (File): input-name \<unity\>):

-   Position ($poscontroll.slx$): i_pos \<turn\> (0 $\widehat{=}$ 0°;
    0.25 $\widehat{=}$ 90°; 1 $\widehat{=}$ 360° $\widehat{=}$ 0° and
    one revolutions $\neq$ 0)

-   Torque ($torquecontroll.slx$): torque \<Nm\>

For each of them, there is an example module.

![Example torque control
module](Figure/Torque_controll.png)

### Additional Functions

There is an additional button 'Set new Starting Point' to set the
current position as starting Point (pos $=$ 0).

## Developer Guide

### Add Additional Fetcher

-   Add method to Python script ($controller.py$)

-   restart Matlab

-   test in Matlab with *py.controller.FUNCTION_NAME(VARIABLE)*

-   For Callback Button: create a button and copy the code from $3.$

-   For MATLAB Function: Create Function and include the method call and
    *coder.extrinsic ('py.controller.FUNCTION_NAME')*

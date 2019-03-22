# temperature-conversion

This library makes it easy to work with temperatures

# Usage

## Step 1: Create new Temperature object
To use this library, a new temperature object must be created.

`t = Temperature()`

## Step 2: Set a temperature
You can set a temperature by setting either Celsius or Fahrenheit. The temperature will be stored by the CPU in degrees Kelvin.

`t.celsius = 100`

OR

`t.fahrenheit = `100`

## Step 3: Call the temperature
Call the temperature in the unit of your choice. Because the library stores the temperature in degrees Kelvin, it will calculate into the unit of your choice upon being called.

`print(t.celsius)`

OR

`print(t.fahrenheit)`

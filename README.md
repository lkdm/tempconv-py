# temperature-conversion.py

This module can convert from/to Kelvin, Celsius, Rankine, Reaumur[1], and Romer[1] using formulas from Wikipedia.org[2].

The aim of the temperature conversion library is to create an easy to use, syntactically simple way to convert between temperature units of measurement. It does not require the developer, who is referencing the library, to use a special function to convert. Instead, the conversion happens in the background when the original temperature is set, and when the new temperature is referenced.

Instead of...

```python
celsius = 100
fahrenheit = t.convertToFahrenheit(celsius)
print(fahrenheit) # 212 F
```

We do this...

```python
t.celsius = 100
print(t.fahrenheit) # 212 F
```

## Usage

### Step 1. Initiate the class

I recommend not using the word `temp`, because it sounds like a temporary variable name.

`t = Temperature`

### Step 2. Set your temperature in original unit of measurement

`t.celsius = 100`

OR

`t.fahrenheit = 100`

OR

`t.kelvin = 100`

### Step 3. Reference temperature in desired unit of measurement

Here are some print examples:

`print(t.celsius)`

`print(t.fahrenheit)`

`print(t.kelvin)`

## How it works

The library works by using Python decorators, setters, and getters to automatically calculate and store temperatures in Kelvins. Whenever `Temperature.fahrenheit` or `Temperature.celsius` are referenced, a Python getter calculates them based off the stored Kelvin value. `Temperature.kelvin` can also be referenced and changed directly.

## Performance

The aim of this library is to provide easy-to-use syntax for Temperature conversion. But because the library does two calculations to convert from Celsius to Fahrenheit, it goes without saying that it isn't the best choice for large-scale massively parallel computing operations. But you wouldn't be using a Python library for that, would you?

Performance can be improved by converting directly from Fahrenheit to Celsius... Or using something like C or Fortran.

## Testing

To test the library, run the testing library.

## Footnotes

[1] Used in this library without diacritical marks (i.e. not Réaumur or Rømer)

[2] https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

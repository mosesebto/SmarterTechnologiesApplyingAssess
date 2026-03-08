# Package Sorting System

## Overview

This repository contains a solution to the Smarter Technology robotic automation challenge.
The goal is to implement a function that sorts packages into different stacks based on their **dimensions and mass**.

The function determines whether a package is **bulky**, **heavy**, both, or neither, and assigns it to the appropriate stack.

## Sorting Rules

A package is classified using the following criteria:

### Bulky

A package is considered **bulky** if:

* Its **volume (width × height × length) ≥ 1,000,000 cm³**, or
* **Any dimension ≥ 150 cm**

### Heavy

A package is considered **heavy** if:

* **Mass ≥ 20 kg**

### Stack Assignment

| Condition               | Stack    |
| ----------------------- | -------- |
| Not bulky and not heavy | STANDARD |
| Bulky OR Heavy          | SPECIAL  |
| Bulky AND Heavy         | REJECTED |

## Implementation

The function implemented:

```
sort(width, height, length, mass)
```

Parameters:

* `width` (cm)
* `height` (cm)
* `length` (cm)
* `mass` (kg)

Returns:

* `"STANDARD"`
* `"SPECIAL"`
* `"REJECTED"`

## Solution Logic

1. Calculate package volume.
2. Determine if the package is bulky.
3. Determine if the package is heavy.
4. Apply sorting rules:

   * Bulky AND Heavy → `REJECTED`
   * Bulky OR Heavy → `SPECIAL`
   * Otherwise → `STANDARD`

## Code Example

```python
def sort(width, height, length, mass):
    volume = width * height * length

    bulky = volume >= 1000000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
```

## Running the Code

### Requirements

* Python 3.x

### Run Example

```
python main.py
```

## Test Cases

| Width | Height | Length | Mass | Expected |
| ----- | ------ | ------ | ---- | -------- |
| 10    | 10     | 10     | 5    | STANDARD |
| 200   | 10     | 10     | 5    | SPECIAL  |
| 10    | 10     | 10     | 25   | SPECIAL  |
| 200   | 200    | 200    | 25   | REJECTED |
| 100   | 100    | 100    | 10   | SPECIAL  |

## Author

Your Name

# REGISTERS:

1. I have compiled data on all of the relevant registers for tap detection using the IMU

2. Note: "Info" is what the values represent, "Details" is what the register controls, "Hexadeciaml Address" is the address of the register
3. Note (cont.): "Page No." is the page that has the details of the register in the datasheet, "Default Value" is what the default value of the register is
4. Note (cont.): "Relevant Bits" are all of bits that are relevant to tap detection

# WAKE_UP_THS:
1. Hexadecimal Address: 5B
2. Page No. 66
3. Relevant Bits: 0
4. Details: single/double tap select
5. Default Value: 0
6. Info: 0 - Single tap detection only, 1 - Single and Double tap detection

# INT_DUR2:
1. Hexadecimal Address: 5A
2. Page No. 65
3. Relevant Bits: 0 - 3
4. Details: maximum time gap for two taps to be registered as a double tap
5. Default Value: 00000
6. Info: when value is equal to 0 - time gap is equal to 16 * ODR_XL time, when value is not equal to 0 - time gap is equal to (16 + v) * ODR_XL time where
7. Info (cont.): "v" is equal to the integer value stored in the register

# TAP_THS_6D:
1. Hexadecimal Address: 59
2. Page No. 65
3. Relevant Bits: 3 - 7
4. Details: Threshold for tap recognition
5. Default Value: 00000
6. Info: None

# TAP_CFG:
1. Hexadecimal Address: 58
2. Page No. 64
3. Relevant Bits: 6
4. Details: Enable / Disable tap recogniton
5. Default Value: 0
6. Info: 0 - Tap detection disabled, 1 - Tap detection enabled

# TAP_SRC:
1. Hexadecimal Address: 1C
2. Page No. 55
3. Relevant Bits: 1 - 7
4. Details: Tap event detection status
5. Defalut Value: 0000000
6. Info: bit 4 - when value is 0 the sign of the acceleration is positive, when value is 1 the sign of the acceleration is negative
7. Info (cont.): for all bits other than bit 4 - when value is 0 tap event is not detected, when value is 1 tap event is detected

# Register Bit Bindings:
contains what each bit in the relevant registers controls / represents

# TAP_SRC:
1.  bit 1: (TAP_IA) blanket status, if value is 1 then a tap event has been detected, otherwise there has been no tap event detected
2.  bit 2: (SINGLE_TAP) single tap event
3.  bit 3: (DOUBLE_TAP) double tap event
4.  bit 4: (TAP_SIGN) sign of the acceleration - when 0 sign is positive, when 1 sign is negative
5.  bit 5: (X_TAP) tap along the x axis
6.  bit 6: (Y_TAP) tap along the y axis
7.  bit 7: (Z_TAP) tap along the z axis

# WAKE_UP_THS:
1.  bit 0: (SINGLE_DOUBLE_TAP) controls if only single taps sould be registered or both single and double taps should be registered

# INT_DUR2:
1.  bits 0 - 4: (DUR[3:0]) stores an integer value that controls the maximum time between two taps that will be counted as a double tap

# TAP_THS_6D:
1.  bits 3 - 7: (TAP_THS[4:0]) stores an integer value that controls the threshold for tap detection

# TAP_CFG:
1.  bit 4: (TAP_X_EN) enables / disables tap detection along the x axis
2.  bit 5: (TAP_Y_EN) enables / disables tap detection along the y axis
3.  bit 6: (TAP_Z_EN) enables / disables tap detection along the z axis

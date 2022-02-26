# def reactor_efficiency(voltage, current, theoretical_max_power):
#     """Assess reactor efficiency zone.

#     :param voltage: voltage value (integer or float)
#     :param current: current value (integer or float)
#     :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
#     :return: str one of 'green', 'orange', 'red', or 'black'

#     Efficiency can be grouped into 4 bands:

#     1. green -> efficiency of 80% or more,
#     2. orange -> efficiency of less than 80% but at least 60%,
#     3. red -> efficiency below 60%, but still 30% or more,
#     4. black ->  less than 30% efficient.

#     The percentage value is calculated as
#     (generated power/ theoretical max power)*100
#     where generated power = voltage * current
#     """
#     generated_power = voltage * current
#     efficiency = (generated_power/theoretical_max_power)*100
#     if efficiency >= 80:
#         print('green')
#     elif efficiency >= 60 and efficiency < 80:
#         print('orange')
#     elif efficiency < 60 and efficiency >= 30:
#         return 'red'
#     else:
#         return 'black'


# if __name__ == '__main__':
#     reactor_efficiency(10, 599, 10000)


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    reactor_produce = temperature * neutrons_produced_per_second
    difference = (reactor_produce/threshold) * 100
    import pdb
    pdb.set_trace()
    if difference < 90:
        print("LOW")
    elif difference == threshold*0.1:
        print('NORMAL')
    else:
        print('DANGER')


if __name__ == '__main__':
    fail_safe(10, 399, 10000)

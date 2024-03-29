"""Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c"
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """


def convert_temp(unit_in, unit_out, temp):
    if unit_in == "c" and unit_out == "f":
        unit_out = temp * 1.8000 + 32.00
        # print(f"should be {unit_out}")
        return unit_out
    elif unit_in == "f" and unit_out == "c":
        unit_out = (temp - 32) / 1.8
        return unit_out
    elif unit_in != "c" and unit_in != "f":
        return print(f"Invalid unit {unit_in}")
    elif unit_out != "c" and unit_out != "f":
        return print(f"Invalid unit {unit_out}")
    else:
        """if unit_in == \"f\" and unit_out == \"f\"
        or unit_in == \"c\" and unit_out == \"c\" """
        return temp


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

# Compute the future value of a given present value, annual rate, and number of years.

###################################################
# Future value formula
# Student should enter function on the next lines.

def future_value(present_value, annual_rate, years):
    
    # Will use FV = PV*(1+(r / n))^(n*t) 
    # PV is present value, r is the annual rate,
    # n is how many times is compounded per year
    # and t is for time in years. In our case n = 1 
    # because it is annually.
    inside_parenthesis = (1 + float(annual_rate)/100)**years
    future_val = present_value * inside_parenthesis
    return future_val


###################################################
# Tests
# Student should not change this code.

def test(present_value, annual_rate, years):
    """Tests the future_value function."""
    
    print "The future value of $" + str(present_value) + " in " + str(years),
    print "years at an annual rate of " + str(annual_rate) + "% is",
    print "$" + str(future_value(present_value, annual_rate, years)) + "."


###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

test(1000, 7, 10)
test(200, 4, 5)
test(1000, 3, 20)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.

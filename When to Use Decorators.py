# The primary function of decorators is reducing the amount of code that you need to write in your applications..
# When we  would want to use cecorators


def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")

    return wrapper


@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")


@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")


@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")


sweep_floors(800)
# I'm off duty!
wash_dishes(1000)
# I'm off duty!
chop_vegetables(1200)
# Chopping the vegetables...
#What are the two options for involing a decorator?
# a function call or @pie_synta_f

function_call()


or
@pie_syntax
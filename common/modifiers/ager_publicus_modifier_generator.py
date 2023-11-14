def print_positive_APR_statement(modifier_rank,
                            army_maintenance_cost,
                            land_morale_modifier,
                            loyalty_gain_chance_modifier,
                            global_citizen_happiness):
    loc = """positive_APR_{modifier_rank} = {{
    army_maintenance_cost = -{army_maintenance_cost}
    land_morale_modifier = {land_morale_modifier}
    loyalty_gain_chance_modifier = -{loyalty_gain_chance_modifier}
    global_citizen_happyness = {global_citizen_happiness}
}}""".format(modifier_rank = round(modifier_rank,4),
    army_maintenance_cost = round(army_maintenance_cost,4),
    land_morale_modifier = round(land_morale_modifier,4),
    loyalty_gain_chance_modifier = round(loyalty_gain_chance_modifier,4),
    global_citizen_happiness = round(global_citizen_happiness,4))
    print(loc)

modifier_rank = 1
army_maintenance_cost = 0.0075
land_morale_modifier = 0.005
loyalty_gain_chance_modifier = 0.0075
global_citizen_happiness = 0.005
while modifier_rank <= 50:
    print_positive_APR_statement(modifier_rank,
                            army_maintenance_cost,
                            land_morale_modifier,
                            loyalty_gain_chance_modifier,
                            global_citizen_happiness)
    modifier_rank = modifier_rank + 1
    army_maintenance_cost = army_maintenance_cost + 0.01
    land_morale_modifier = land_morale_modifier + 0.01
    loyalty_gain_chance_modifier = loyalty_gain_chance_modifier + 0.01
    global_citizen_happiness = global_citizen_happiness + 0.01

def print_negative_APR_statement(modifier_rank,
                            army_maintenance_cost,
                            land_morale_modifier,
                            loyalty_gain_chance_modifier,
                            global_citizen_happiness,
                            stability_monthly_change):
    loc = """negative_APR_{modifier_rank} = {{
    army_maintenance_cost = {army_maintenance_cost}
    land_morale_modifier = -{land_morale_modifier}
    loyalty_gain_chance_modifier = {loyalty_gain_chance_modifier}
    global_citizen_happyness = -{global_citizen_happiness}
    civil_war_threshold = -{civil_war_threshold}
    stability_monthly_change = -{stability_monthly_change}
}}""".format(modifier_rank = round(modifier_rank,4),
    army_maintenance_cost = round(army_maintenance_cost,4),
    land_morale_modifier = round(land_morale_modifier,4),
    loyalty_gain_chance_modifier = round(loyalty_gain_chance_modifier,4),
    global_citizen_happiness = round(global_citizen_happiness,4),
    civil_war_threshold = round(civil_war_threshold,4),
    stability_monthly_change = round(stability_monthly_change,4))
    print(loc)

modifier_rank = 1
army_maintenance_cost = 0.01
land_morale_modifier = 0.005
loyalty_gain_chance_modifier = 0.01
global_citizen_happiness = 0.005
civil_war_threshold = 0.0012
stability_monthly_change = 0.0012
while modifier_rank <= 50:
    print_negative_APR_statement(modifier_rank,
                            army_maintenance_cost,
                            land_morale_modifier,
                            loyalty_gain_chance_modifier,
                            global_citizen_happiness,
                            civil_war_threshold)
    modifier_rank = modifier_rank + 1
    army_maintenance_cost = army_maintenance_cost + 0.01
    land_morale_modifier = land_morale_modifier + 0.01
    loyalty_gain_chance_modifier = loyalty_gain_chance_modifier + 0.01
    global_citizen_happiness = global_citizen_happiness + 0.01
    civil_war_threshold = civil_war_threshold + 0.0012
    stability_monthly_change = stability_monthly_change + 0.0012

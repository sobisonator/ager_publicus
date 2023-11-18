def print_APR_applicator_positive(num):
    loc = """	else_if = {{
		limit = {{
			APR_svalue > {num}
			APR_svalue < {num_plus1}
		}}
		add_country_modifier = {{
			name = positive_APR_{num}
			duration = 365 # Updated on yearly country pulse
		}}
	}}""".format(num = round(num,0), num_plus1 = num + 1)
    print(loc)

num = 1
while num <= 50:
    print_APR_applicator_positive(num=num)
    num = num + 1

def print_APR_applicator_negative(num):
    loc = """	else_if = {{
		limit = {{
			APR_svalue < -{num}
			APR_svalue > -{num_plus1}
		}}
		add_country_modifier = {{
			name = negative_APR_{num}
			duration = 365 # Updated on yearly country pulse
		}}
	}}""".format(num = round(num,0), num_plus1 = num + 1)
    print(loc)

num = 1
while num <= 50:
    print_APR_applicator_negative(num=num)
    num = num + 1

def salary_parser(salary):
    temp = salary.split()
    try:
        return (int(temp[0]) + int(temp[1].split('-')[1]))*1000/2
    except :
        return int(temp[1])*1000
with open('./hr_system.txt') as hr_file:
    print()
    for line in hr_file:
        line = line.strip()
        line_parts = line.split()
        name = line_parts[0]
        id_number = int(line_parts[1])
        job_title = line_parts[2]
        salary = float(line_parts[3])

        if job_title.lower() == 'engineer':
            paycheck = float(salary / 24 + 1000)

        else:
            paycheck = float(salary / 24)

        print(f'{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}')

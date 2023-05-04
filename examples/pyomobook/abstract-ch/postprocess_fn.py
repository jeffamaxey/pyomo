import csv

def pyomo_postprocess(options=None, instance=None,
                                        results=None):
    #
    # Collect the data
    #
    vars = set()
    data = {}
    f = {}
    for i in range(len(results.solution)):
        data[i] = {}
        for var in results.solution[i].variable:
            vars.add(var)
            data[i][var] = \
                results.solution[i].variable[var]['Value']
        for obj in results.solution[i].objective:
            f[i] = results.solution[i].objective[obj]['Value']
            break
    vars = sorted(vars)
    rows = [['obj'] + vars]
    for i in range(len(results.solution)):
        row = [f[i]]
        row.extend(data[i].get(var,None) for var in vars)
        rows.append(row)
    print("Creating results file results.csv")
    with open('results.csv', 'w') as OUTPUT:
        writer = csv.writer(OUTPUT)
        writer.writerows(rows)


def solution(xs):
    maxPower = 0
    tmp = 1
    panels = xs[:]
    drainingPanels = []
    if 1 in panels:
        maxPower = 1

    for i in panels:
        if i == 0:
            continue
        elif i < 0:
            drainingPanels.append(i)
        else:
            tmp *= i

        if tmp > 1 and tmp > maxPower:
            maxPower = tmp

    maxConverted = 0
    tmp = 1

    if len(drainingPanels) % 2 == 0 and len(drainingPanels) > 0:
        for i in drainingPanels:
            tmp *= i
        if tmp > maxConverted:
            maxConverted = tmp

    elif len(drainingPanels) > 0:
        for i in drainingPanels:
            test = drainingPanels[:]
            test.remove(i)
            tmp = 1
            if len(test) > 1:
                for j in test:
                    tmp *= j
                if tmp > maxConverted:
                    maxConverted = tmp

    if maxConverted > 0 and maxPower > 0:
        maxPower *= maxConverted
    elif maxPower == 0 and maxConverted > 0:
        maxPower = maxConverted
    elif len(panels) == 1:
        maxPower = panels[0]

    return str(maxPower)

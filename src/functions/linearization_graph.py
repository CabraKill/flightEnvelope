class LinearizationGraph:
    def linearization(self, values: [float], debub=False):
        linearized_values = values.copy()
        if debub:
            print("Normal     list: {}".format(linearized_values))
        for i, _ in enumerate(linearized_values):

            if i < len(linearized_values)-1:
                if linearized_values[i] == linearized_values[i+1]:
                    count = 0
                    while True:
                        if i+count+1 < len(linearized_values):
                            if linearized_values[i+count+1] == linearized_values[i]:
                                count += 1
                            else:
                                break
                        else:
                            break
                    if linearized_values[-1] != linearized_values[i]:
                        for j in range(1,count+1):
                            linearized_values[i+j] = ((linearized_values[i+count+1] -
                                                    linearized_values[i])/(count+1)) * j + linearized_values[i]
                    else:
                        break
                    i += j
        if debub:
            print("Linearized list: {}".format(linearized_values))
        return linearized_values

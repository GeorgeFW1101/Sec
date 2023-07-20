def calculate_harm_minimization(P, E, C, V, T):
    # Calculate the evidentiary value of the dream or memory (E)
    evidentiary_value = (C * V) / T

    # Calculate the harm minimization (H) using the combined equation
    harm_minimization = (1 / P) * (1 / E) * evidentiary_value

    return harm_minimization
while(True):
    # Example values for the variables
    privacy_level = float(input("privacy_level: "))#eg 0.8
    exposure_level = float(input("exposure_level: "))#eg 0.8
    credibility = float(input("credibility: "))#eg 0.8
    vividness = float(input("vividness: "))#eg 0.8
    time_elapsed = float(input("time_elapsed: "))#eg 5
    # Calculate the harm minimization using the provided values
    result = calculate_harm_minimization(privacy_level, exposure_level, credibility, vividness, time_elapsed)
    print("Harm Minimization:", result)
    print()

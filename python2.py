import pickle

# Step 1: Main function
def main():
    # Step 2: Dictionary with conversion factors
    dictPlanetaryWeights = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.12,
        "Pluto": 0.066
    }
    
    # Step 3: Try to load existing pickled history
    db_filename = 'BEPlanetaryWeights.db'  # Corrected file name
    try:
        with open(db_filename, 'rb') as f:
            dictPlanetHistory = pickle.load(f)
    except FileNotFoundError:
        dictPlanetHistory = {}
    
    # Step 4: Ask if user wants to see history
    sSeeHistory = input("Would you like to see previous history? (Y/y or N/n): ")
    if sSeeHistory.lower() == 'y':
        print("\nHistory:")
        for sName, dictWeights in dictPlanetHistory.items():
            print(f"{sName}: {dictWeights}")
        print("\n")
    
    # Step 5: Loop to collect user name
    while True:
        sName = input("Enter a unique name (or press Enter to quit): ").strip()
        
        # Exit loop if blank name is entered
        if sName == "":
            break
        
        # Check if names are unque
        if sName in dictPlanetHistory:
            print("This name already exists. Please enter a different name.")
            continue
        
        # Step 5b:validateinput for Earth Weight
        while True:
            try:
                fEarthWeight = float(input("Enter your Earth weight in pounds: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for Earth weight.")
        
        # Step 5c: Calculate weights for each planet
        dictPersonWeights = {}
        for sPlanet, fGravityFactor in dictPlanetaryWeights.items():
            fPlanetWeight = fEarthWeight * fGravityFactor
            dictPersonWeights[sPlanet] = f"{fPlanetWeight:10.2f}"  # Format to 2 decimal places
        
        # Step 5d: Add to history
        dictPlanetHistory[sName] = dictPersonWeights
        
        # Step 6: Output results in formatted style
        print(f"\n{sName}'s Solar System's Planetary Weights:")
        for sPlanet, fPlanetWeight in dictPersonWeights.items():
            print(f"{sPlanet:<10}: {fPlanetWeight}")
        print("\n")
    
    # Step 7: Pickle the updated history before exiting
    with open(db_filename, 'wb') as f:
        pickle.dump(dictPlanetHistory, f)

# Step 8: Run the main function
if __name__ == "__main__":
    main()

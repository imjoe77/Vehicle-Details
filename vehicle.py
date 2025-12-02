def vehicle_details(vehicle_number, owner_name, vehicle_type, year):
    return (
        f"vehicle_number = {vehicle_number} \n",
        f"owner_name = {owner_name} \n",
        f"vehicle_type = {vehicle_type} \n",
        f"year = {year}"
    )


if __name__ == "__main__":
    # Sample Output
    print(vehicle_details("101", "Rohit", "Car", 2022))

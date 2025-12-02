from vehicle import vehicle_details

def test_vehicle_details():
    expected_output = (
        "vehicle_number = 101 \n",
        "owner_name = Rohit \n",
        "vehicle_type = Car \n",
        "year = 2020"
    )
    
    assert vehicle_details("101", "Rohit", "Car", "2020") == expected_output

from application.parking_service import ParkingService


def run_parking_service_test():
    print("=== ParkingService integration test ===")

    service = ParkingService(
        capacity=2,
        ev_capacity=2,
        level=1
    )

    # Regular car
    slot1 = service.park_vehicle(
        reg_num="REG-001",
        make="Toyota",
        model="Corolla",
        color="Blue",
        is_electric=False,
        is_motorcycle=False
    )
    print(f"Regular Car slot: {slot1}")

    # Motorcycle
    slot2 = service.park_vehicle(
        reg_num="REG-002",
        make="Yamaha",
        model="MT-07",
        color="Black",
        is_electric=False,
        is_motorcycle=True
    )
    print(f"Motorcycle slot: {slot2}")

    # Electric car
    slot3 = service.park_vehicle(
        reg_num="EV-001",
        make="Tesla",
        model="Model 3",
        color="White",
        is_electric=True,
        is_motorcycle=False
    )
    print(f"Electric Car slot: {slot3}")

    # Electric motorcycle
    slot4 = service.park_vehicle(
        reg_num="EV-002",
        make="Zero",
        model="SR/F",
        color="Red",
        is_electric=True,
        is_motorcycle=True
    )
    print(f"Electric Motorcycle slot: {slot4}")

    # Remove regular car
    removed = service.remove_vehicle(slot1, is_ev=False)
    print(f"Removed regular car from slot {slot1}: {removed}")

    print("=== Test finished ===")


if __name__ == "__main__":
    run_parking_service_test()

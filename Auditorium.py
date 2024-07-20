class Auditorium:
    def __init__(self, AuditoriumName=None, EventsList=None, Date=None, Time=None, TotalSeats=None, DepartmentId=None):
        self.AuditoriumName = AuditoriumName
        self.EventsList = EventsList
        self.Date = Date
        self.Time = Time
        self.TotalSeats = TotalSeats
        self.DepartmentId = DepartmentId

    def BookEvents(self, AuditoriumName, EventsList, Date, Time, TotalSeats, DepartmentId):
        try:
            with open("Events.txt", "r") as EventFile:
                lines = EventFile.readlines()
        except FileNotFoundError:
            lines = []

        event_found = False

        for line in lines:
            events = line.strip().split(',')
            if len(events) == 6:
                Auditorium_Name = events[0]
                event_time = events[3]

                if Auditorium_Name == AuditoriumName and event_time == Time:
                    event_found = True
                    break

        if not event_found:
            try:
                with open("Events.txt", "a") as EventFile:
                    EventFile.write(f"{AuditoriumName},")
                    EventFile.write(f"{EventsList},")
                    EventFile.write(f"{Date},")
                    EventFile.write(f"{Time},")
                    EventFile.write(f"{TotalSeats},")
                    EventFile.write(f"{DepartmentId}\n")
                    print("Event added successfully.")
            except FileNotFoundError:
                print("Error: Events.txt not found.")
        else:
            print("Event already exists at the specified time.")







    def __init__(self, guest_name):
        self.gest_name = guest_name

        self.party_location = "Spitwegstr. 4, 81373 München"
        self.party_starttime = datetime.datetime(year=2024, month=1, day=6, hour=19, minute=0)

    def send_invitation(self):
        current_date = datetime.datetime.now().date()

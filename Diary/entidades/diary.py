class Diary:
    def __init__(self, diary_date_day, diary_construction):
        self.__diary_date_day = diary_date_day
        self.__diary_construction = diary_construction

    @property
    def diary_date_day(self):
        return self.__diary_date_day

    @diary_date_day.setter
    def diary_date_day(self, diary_date_day):
        self.__diary_date_day = diary_date_day

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def diary_construction(self):
        return self.__diary_construction

    @diary_construction.setter
    def diary_construction(self, diary_construction):
        self.__diary_construction = diary_construction

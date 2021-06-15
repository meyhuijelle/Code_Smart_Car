from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    # Read the history table of the database.
    @staticmethod
    def read_historiek():
        sql = "SELECT * FROM devicesdb.historiek ORDER BY HistoriekID DESC LIMIT 10"
        return Database.get_rows(sql)

    # Create a history for in the database.
    @staticmethod
    def create_historiek(DeviceID, ActieID, Actiedatum, Waarde, Commentaar):
        sql = "INSERT INTO devicesdb.historiek(DeviceID,ActieID,Actiedatum, Waarde, Commentaar) VALUES(%s,%s,%s,%s,%s)"
        params = [DeviceID, ActieID, Actiedatum, Waarde, Commentaar]
        return Database.execute_sql(sql, params)

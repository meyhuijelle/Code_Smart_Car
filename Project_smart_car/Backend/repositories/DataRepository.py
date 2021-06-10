from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    @staticmethod
    def read_historiek():
        sql = "SELECT * FROM devicesdb.historiek ORDER BY HistoriekID DESC LIMIT 10"
        return Database.get_rows(sql)

    @staticmethod
    def create_historiek(DeviceID, ActieID, Actiedatum, Waarde, Commentaar):
        sql = "INSERT INTO devicesdb.historiek(DeviceID,ActieID,Actiedatum, Waarde, Commentaar) VALUES(%s,%s,%s,%s,%s)"
        params = [DeviceID, ActieID, Actiedatum, Waarde, Commentaar]
        return Database.execute_sql(sql, params)

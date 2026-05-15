from database.DB_connect import DBConnect
from model.border import Border


class DAO():

    @staticmethod
    def getAllBorders(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.state1ab, c1.StateNme as state1nm, c.state2ab, c2.StateNme as state2nm, c.year, c.conttype
                    from contiguity c, country c1, country c2
                    where c.state1ab = c1.StateAbb
                    and c.state2ab = c2.StateAbb
                    and c.year <= %s"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Border(**row))

        cursor.close()
        conn.close()
        return result

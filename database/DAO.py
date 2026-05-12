from database.DB_connect import DBConnect
from model.border import Border


class DAO():

    @staticmethod
    def getAllBorders(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select state1ab, c2.StateNme as state1nm, state2ab, c.year, conttype
                        from contiguity c, country c2 
                        where c.state1ab = c2.StateAbb 
                        and`year` <= %s"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Border(**row))

        cursor.close()
        conn.close()
        return result

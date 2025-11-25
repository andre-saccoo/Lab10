from database.DB_connect import DBConnect
from model.hub import Hub

class DAO:
    """ Implementare tutte le funzioni necessarie a interrogare il database. collegare al model """

    @staticmethod
    def get_hub():
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        result = {}
        query = " SELECT * FROM hub"
        cursor = cnx.cursor(dictionary=True)

        try:
            cursor.execute(query)
            for row in cursor:
                hub=Hub(id=row[0], codice=row[1], nome=row[2], citta=row[3], stato=row[4],latitudine=row[5],longitudine=row[6])
                result[hub.id] = hub

        except Exception as e:
            print(f"Errore durante la query get_tour: {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_tratta():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        result = {}
        query = """ SELECT LEAST(id_hub_origine, id_hub_destinazione) AS hub_norm_origine,
                    GREATEST(id_hub_origine, id_hub_destinazione) AS hub_norm_destinazione, 
                    AVG(valore_merce) AS media_valore_merce
                    FROM spedizione
                    GROUP BY LEAST(id_hub_origine, id_hub_destinazione), GREATEST(id_hub_origine, id_hub_destinazione);"""
        cursor = cnx.cursor(dictionary=True)

        try:
            cursor.execute(query)
            for row in cursor:
                tratta = Tratta(id=row[0], codice=row[1], nome=row[2], citta=row[3], stato=row[4], latitudine=row[5],
                          longitudine=row[6])
                result[hub.id] = hub

        except Exception as e:
            print(f"Errore durante la query get_tour: {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()
        return result
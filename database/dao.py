from database.DB_connect import DBConnect
from Model.hub import Hub
from Model.tratta import Tratta

class DAO:
    """ Implementare tutte le funzioni necessarie a interrogare il database. collegare al Model """

    @staticmethod
    def get_hub():
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        result = []
        query = " SELECT * FROM hub"
        cursor = cnx.cursor(dictionary=True)

        try:
            cursor.execute(query)
            for row in cursor:
                hub=Hub(id=row["id"], codice=row["codice"], nome=row["nome"], citta=row["citta"], stato=row["stato"],latitudine=row["latitudine"],longitudine=row["longitudine"])
                result.append (hub)

        except Exception as e:
            print(f"Errore durante la query get_hub: {e}")
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

        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT LEAST(id_hub_origine, id_hub_destinazione) AS hub_origine,
                    GREATEST(id_hub_origine, id_hub_destinazione) AS hub_destinazione, 
                    AVG(valore_merce) AS media_valore_merce
                    FROM spedizione
                    GROUP BY LEAST(id_hub_origine, id_hub_destinazione), GREATEST(id_hub_origine, id_hub_destinazione);"""

        try:
            cursor.execute(query)
            for row in cursor:
                tratta = Tratta(id_hub_A = row["hub_origine"], id_hub_B = row["hub_destinazione"], guadagno_medio=row["media_valore_merce"])
                result.append(tratta)

        except Exception as e:
            print(f"Errore durante la query get_tratta: {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()
        return result
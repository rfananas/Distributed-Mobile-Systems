from waltisLibrary import *
import mysql.connector

# https://pynative.com/python-mysql-transaction-management-using-commit-rollback/

def showKontoUebersicht(connection, cursor, title="", titleLevel=1):
    
        if titleLevel == 1:
            uChar = "="
            abstand = "\n"
        elif titleLevel == 2:
            uChar = "-"
            abstand = ""

        print(unterstreichen(title, uChar), abstand)
        # zeige Kontosaldos and Bilanzsumme
        sql_show_saldo_query = """select id_bankkonto, saldo from bankkonto;"""
        cursor.execute(sql_show_saldo_query) #cursor objektreferenz
        myresult = cursor.fetchall()
        print("+------+--------------+")
        print("| Id   | Saldo        |")
        print("+------+--------------+")
        bilanzsumme = 0
        for aRec in myresult:
            bilanzsumme += aRec[1]
            print("| {id:4d} |".format(id=aRec[0]), end="")
            print(" {saldo:12.2f} |".format(saldo=aRec[1]), end="")
            print()
        print("+------+--------------+")
        print("| Summe: {summe:12.2f} |".format(summe=bilanzsumme))
        print("+------+--------------+")
        print("Records found:", len(myresult), myresult)


def doKontoUebertrag(connection, cursor, withdrawAmount, fromKontoId, toKontoId, trace=True):
    if trace:
        showKontoUebersicht(connection, cursor, "Vor Kontoübertrag")

    #Abheben von Lohnkonto
    sql_update_query = """UPDATE bankkonto set saldo = saldo - """ + str(withdrawAmount) + """ WHERE id_bankkonto = """ + str(fromKontoId)
    cursor.execute(sql_update_query)

    if trace:
        showKontoUebersicht(connection, cursor, "Abgebucht von Ursprungskonto, aber noch nicht eingebucht in Zielkonto", 2)
        halt("Check with workbench! Then press RETURN to continue!")

    #Einzahlen in Lohnkonto
    sql_update_query = """UPDATE bankkonto set saldo = saldo + """ + str(withdrawAmount) + """ WHERE id_bankkonto = """ + str(toKontoId)
    cursor.execute(sql_update_query)

    if trace:
        showKontoUebersicht(connection, cursor, "Gebucht, aber kein commit", 2)
        halt("Check with workbench! Then press RETURN to continue!")

    #Änderungen commiten
    connection.commit()
    if trace:
        showKontoUebersicht(connection, cursor, "Nach commit", 2)
        halt("Check with workbench! Then press RETURN to continue!")


dbServer = "localhost"
dbSchema = "MyBank"
userName = "root"
password = "admin"

try:
    print(f"Connecting to '{dbSchema:s}' with user '{userName:s}'....", end="", flush=True)
    # https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
    conn = mysql.connector.connect(
        host=dbServer,
        database=dbSchema,
        user=userName,
        passwd=password,
        auth_plugin = 'mysql_native_password'
    )
    print("completed!")

    conn.autocommit = False   # explicit commit and rollback by the application (Front-End)
    cursor = conn.cursor() #globale Variable, wie können wir den Seiteneffekt minimieren? Wir übergeben ein argument "cursor"

    showKontoUebersicht(conn, cursor, "Vor Kontoübertrag")
    fromKonto = readInt("Belastungskonto (From): ", min=1, max=2)
    toKonto   = readInt("Gutschriftskonto (To): ", min=1, max=2)
    withdrawAmount = readFloat("Uebertrags-Betrag: ", min=10, max=10000)

    doKontoUebertrag(conn, cursor, withdrawAmount, fromKontoId=fromKonto, toKontoId=toKonto, trace=False)

    showKontoUebersicht(conn, cursor, "Nach Kontoübertrag")


except mysql.connector.Error as error:
    print("Failed to update record to database rollback: {}".format(error))
    # reverting changes because of exception
    conn.rollback()
finally:
    # closing database connection.
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection is closed")
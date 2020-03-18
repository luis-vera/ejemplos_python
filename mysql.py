#!/usr/bin/env python
#-*- coding: utf-8 -*-
import MySQLdb
import csv

class Mysql:
    """ Clase de base de datos en mysql"""
    servidor = None
    usuario = None
    clave = None
    baseDatos = None
    conexion = None
    resultado = None
    filas = 0
    columnas = 0
    
    # Constructor de la clase
    def __init__(self, srv, usr, clv, bd, prt=3306, encoding=None):
        self.servidor = srv
        self.usuario = usr
        self.clave = clv
        self.baseDatos = bd
        self.port = prt
        try:
            self.conexion = MySQLdb.connect(host = self.servidor, 
                                            user = self.usuario, 
                                            passwd = self.clave, 
                                            db = self.baseDatos,
                                            port = self.port,
                                            charset = encoding)
            self.conexion.autocommit(True)
        except MySQLdb.Error, e:
            raise MySQLdb.Error, e
    
    def __del__(self):
        self.conexion.close()
    # Efectuar Consulta
    def doQuery(self, mysqlQuery):
        try:
            self.conexion.ping()
            self.conexion.query(mysqlQuery)
            self.resultado = self.conexion.store_result()
            if self.resultado:
                self.filas = self.resultado.num_rows()
                self.columnas = self.resultado.num_fields()
            else:
                self.filas = 0
                self.columnas = 0
            
        except MySQLdb.Error, e:
            raise e
    
    # Resultado en array
    def resultadoEnArray(self):
        response = list()
        i=0
        while i< self.filas:
            row = self.resultado.fetch_row()
            response.append(row[0])
            i = i+1
        return response

    # Resultado en csv
    def resultadoEnCsv(self, nombreArchivo):
        try:
            if not self.resultado:
                raise Exception("Resultado vacio")

            columnas = []
            for columna in self.resultado.describe():
                columnas.append(columna[0].capitalize())

            with open(nombreArchivo, "wb") as archivoCsv:
                writer = csv.writer(archivoCsv, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(columnas)
                for i in range(0, self.filas):
                    writer.writerow(self.resultado.fetch_row()[0])
            archivoCsv.close()

        except:
            raise

    # Resultado en diccionario
    def resultadoEnDict(self):
        try:
            if not self.resultado:
                raise Exception("Resultado vacio")

            columnas = []
            for columna in self.resultado.describe():
                columnas.append(columna[0])

            resultado = []
            for i in range(0, self.filas):
                diccionario = {}
                row = self.resultado.fetch_row()[0]
                for j in range(0, self.columnas):
                    diccionario[columnas[j]] = row[j]
                resultado.append(diccionario)
            return resultado

        except:
            raise

    def sanitize(self, param):
        """Si se usa este método para limpiar los parámetros se deben omitir las comillas en la consulta,
        dado que estas forman parte del valor de retorno de este método"""
        return "'%s'"%self.conexion.escape_string(param)

import csv
import datetime
#import mysql

def insertar_fila_problema(uuid):
	fecha = str(datetime.datetime.now())
	fechaOK = fecha[0:19]
	texto_query = "INSERT INTO problemas(conferencia, reviewdate) VALUES ('" + uuid + "','"+fechaOK+"') "
	print(texto_query)

def insertar_fila(uuid, issue):
	texto_query = "INSERT INTO detalles_problemas(conferencia, problema) VALUES ('" + uuid + "','"+issue+"') "
	print(texto_query)


def leer_archivo(nombre):
	with open(nombre, newline='') as csvfile:
		csvObj = csv.DictReader(csvfile)
		for row in csvObj:
			# Leo cada fila del archivo 
			created = row['created']
			call_uuid = row['call_uuid'] 
			call_country_id = row['call_country_id']
			recording_url = row['recording_url']
			# lista de issues por fila
			issue_noise = row['issue_noise']
			issue_silent = row['issue_silent']
			issue_volume_distortion = row['issue_volume_distortion']
			issue_one_way_audio = row['issue_one_way_audio']
			issue_crosstalk = row['issue_crosstalk']
			issue_cut_call = row['issue_cut_call']
			issue_delay = row['issue_delay']
			issue_echo = row['issue_echo']
			issue_intermittent_audio = row['issue_intermittent_audio']
			issue_dropped_call = row['issue_dropped_call']
			issue_low_quality_audio = row['issue_low_quality_audio']
			insertar_fila_problema(call_uuid)
			# ahora tomo las variables que me sirven
			if (issue_noise == "true"):
				insertar_fila(call_uuid,"issue_noise")
			if (issue_silent == "true"):
				insertar_fila(call_uuid,"issue_silent")
			if (issue_volume_distortion == "true"):
				insertar_fila(call_uuid,"issue_volume_distortion")
			if (issue_one_way_audio == "true"):
				insertar_fila(call_uuid,"issue_one_way_audio")
			if (issue_crosstalk == "true"):
				insertar_fila(call_uuid,"issue_crosstalk")
			if (issue_cut_call == "true"):
				insertar_fila(call_uuid,"issue_cut_call")
			if (issue_delay == "true"):
				insertar_fila(call_uuid,"issue_delay")
			if (issue_echo == "true"):
				insertar_fila(call_uuid,"issue_echo")
			if (issue_intermittent_audio == "true"):
				insertar_fila(call_uuid,"issue_intermittent_audio")
			if (issue_dropped_call == "true"):
				insertar_fila(call_uuid,"issue_dropped_call")
			if (issue_low_quality_audio == "true"):
				insertar_fila(call_uuid,"issue_low_quality_audio")
			
			
			
leer_archivo('Calls with issues (human) - last 48 hours - OPSMOVIL.csv')
leer_archivo('Calls with issues (bot) - last 48 hours - OPSMOVIL.csv')
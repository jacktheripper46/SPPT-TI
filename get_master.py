from flask import Flask
from flask import jsonify

import psycopg2
import psycopg2.extras
#import json

app = Flask(__name__)

connection = psycopg2.connect(user="postgres",
                          password="debten",
                          host="192.168.40.37",
                          port="5432",
                          database="puskarda")


@app.route('/agama')
def master_agama():
    PostgreSQL_select_Query = "SELECT kode, nama FROM master_agama"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/alasanpenghentianperkara')
def master_alasan_penghentian_perkara():
    PostgreSQL_select_Query = "select  kode, nama from master_alasan_penghentian_perkara"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenisdokumen')
def master_jenis_dokumen():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_dokumen"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenishukuman')
def master_jenis_hukuman():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_hukuman"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenisidentitas')
def master_jenis_identitas():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_identitas"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenisjaminan')
def master_jenis_jaminan():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_jaminan"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenispenahanan')
def master_jenis_penahanan():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_penahanan"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenisproses')
def master_jenis_proses():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_proses"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenisputusan')
def master_jenis_putusan():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_putusan"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/jenistindakpidana')
def master_jenis_tindak_pidana():
    PostgreSQL_select_Query = "select kode, nama from master_jenis_tindak_pidana"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/negara')
def master_negara():
    PostgreSQL_select_Query = "select kode, nama from master_negara"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/pekerjaan')
def master_pekerjaan():
    PostgreSQL_select_Query = "select kode, nama from master_pekerjaan"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/pemetaansatker')
def master_pemetaan_satker():
    PostgreSQL_select_Query = "select * from master_pemetaan_satker"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode_satker_kepolisian'] = records[x][0]
        row['nama_satker_kepolisian'] = records[x][1]
        row['kode_satker_kejaksaan'] = records[x][2]
        row['nama_satker_kejaksaan'] = records[x][3]
        row['kode_satker_pengadilan'] = records[x][4]
        row['nama_satker_pengadilan'] = records[x][5]
        result.append(row)
    return jsonify(result)

@app.route('/pendidikan')
def master_pendidikan():
    PostgreSQL_select_Query = "select kode, nama from master_pendidikan"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/pihakpenahan')
def master_pihak_penahan():
    PostgreSQL_select_Query = "select kode, nama from master_pihak_penahan"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/satker')
def master_satker():
    PostgreSQL_select_Query = "select kode, nama from master_satker"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/statusnikah')
def master_status_nikah():
    PostgreSQL_select_Query = "select kode, nama from master_status_nikah"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/tingkatpengadilan')
def master_tingkat_pengadilan():
    PostgreSQL_select_Query = "select kode, nama from master_tingkat_pengadilan"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama'] = records[x][1]
        result.append(row)
    return jsonify(result)

@app.route('/wiladmin')
def master_wilayah_administrasi():
    PostgreSQL_select_Query = "select kode, nama_wilayah from master_wilayah_administrasi"
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(PostgreSQL_select_Query)
    records = cursor.fetchall()
    result = []
    for x in range(len(records)):
        row = {}
        row['kode'] = records[x][0]
        row['nama_wilayah'] = records[x][1]
        result.append(row)
    return jsonify(result)

if (__name__ == "__main__"):
	app.run(host = '0.0.0.0', port = 8000)

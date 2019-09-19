#master_dokumen.py
from flask import Flask, request
from flask import jsonify

import psycopg2
import psycopg2.extras
#import json

app = Flask(__name__)



@app.route('/')
def index():
    connection = psycopg2.connect('postgresql://postgres:debten@192.168.10.107:5432/puskarda')
    cursor = connection.cursor()
    return cursor
    return "Hello"
@app.route('/dokumen/<jenis>', methods = ['GET'])
def master_ajax(jenis):
    # if jenis == 'aph_endpoint':
    if jenis == 'spdp':
        #return "halaman spdp"
        #return cursor
        postgreSQL_select_Query = "SELECT * FROM master_jenis_dokumen"
        #postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
        postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
        cursor.execute(postgreSQL_select_Query)
        record_master = cursor.fetchall()
        return jsonify(record_master)
        return "Close"
    else:
        return "Tidak Ada Kode Dokumen Tersebut"
        # postgreSQL_select_Query = "SELECT * FROM dokumen"
        # postgreSQL_select_Query += " WHERE date_part('year', tgl_dok_dibuat) = '" + versi_api + "'"
        # postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
        # cursor.execute(postgreSQL_select_Query)
        # record_master = cursor.fetchall()
        # return jsonify(record_master)
    # elif jenis == 'satker':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_satker"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'wiladmin':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama_wilayah FROM master_wilayah_administrasi"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama_wilayah ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'negara':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_negara"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'pekerjaan':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_pekerjaan"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'agama':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_agama"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'statusnikah':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_status_nikah"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'jenispenahanan':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_jenis_penahanan"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'jenisidentitas':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_jenis_identitas"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'pendidikan':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_pendidikan"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'pihakpenahan':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_pihak_penahan"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'alasanpenghentianperkara':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_alasan_penghentian_perkara"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'jenishukuman':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_jenis_hukuman"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'jenisdokumen':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_jenis_dokumen"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'jenisproses':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_jenis_proses"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'tingkatpengadilan':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_tingkat_pengadilan"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'jenisjaminan':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_jenis_jaminan"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #     return jsonify(record_master)
    # elif jenis == 'jenistindakpidana':
    #     postgreSQL_select_Query = "SELECT max(kode) as kode, nama FROM master_jenis_tindak_pidana"
    #     postgreSQL_select_Query += " WHERE date_part('year', aktifasi) = '" + versi_api + "'"
    #     postgreSQL_select_Query += " GROUP BY nama ORDER BY kode ASC"
    #     cursor.execute(postgreSQL_select_Query)
    #     record_master = cursor.fetchall()
    #    return jsonify(record_master)

if (__name__ == "__main__"):
	app.run(host = '0.0.0.0', port = 8000)

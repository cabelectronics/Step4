import serial
import time
from decimal import Decimal
import gpxpy
import folium
import pandas as pd


latitude_guest = open('Latitude_guest.txt', 'r')
for line in latitude_guest:
    latitude_data = line
#la_gu = Decimal(latitude_data)
latitude_result = Decimal(latitude_data)

'''
if la_gu > 0:
    a1 = la_gu / 100
    a2 = int(a1)
    a3 = a2 * 100
    a4 = a1 - a3
    a5 = a4 / 60
    a6 = a3 + a5
    
    latitude_result = a6 
elif la_gu < 0:
    a1 = la_gu / 100
    a2 = int(a1)
    a3 = a2 * 100
    a4 = a1 - a4
    a5 = a4 / 60
    a6 = a3 + a6
    a7 = a6 * -1

    latitude_result = a7  
'''

longitude_guest = open('Longitude_guest.txt', 'r')
for line in longitude_guest:
    longitude_data = line
#lo_gu = Decimal(longitude_data)
longitude_result = Decimal(longitude_data)

'''
if lo_gu > 0:
    a1 = la_gu / 100
    a2 = int(a1)
    a3 = a2 * 100
    a4 = a1 - a4
    a5 = a4 / 60
    a6 = a3 + a6
    
    longitude_result = a6 

elif lo_gu < 0:
    a1 = la_gu / 100
    a2 = int(a1)
    a3 = a2 * 100
    a4 = a1 - a4
    a5 = a4 / 60
    a6 = a3 + a6
    a7 = a6 * -1

    longitude_result = a7
'''

baud_rate = open('Baudrate.txt', 'r')
for line in baud_rate:
    BAUDRATE = line

moto1_com = open('Moto1com.txt', 'r')
for line in moto1_com:
    MOTO1COM = line

moto2_com = open('Moto2com.txt', 'r')
for line in moto2_com:    
    MOTO2COM = line

moto3_com = open('Moto3com.txt', 'r')
for line in moto3_com:
    MOTO3COM = line

moto4_com = open('Moto4com.txt', 'r')
for line in moto4_com:
    MOTO4COM = line

airplane_com = open('Airplanecom.txt', 'r')
for line in airplane_com:
    AIRPLANECOM = line

helicopter_com = open('Helicoptercom.txt', 'r')
for line in helicopter_com:
    HELICOPTERCOM = line

def LatitudeM1():
    if MOTO1COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = MOTO1COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if latitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto1_latitude = aM7
                    
                elif latitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto1_latitude = aM8

                return moto1_latitude    
            ser.close()
        except:
            pass


def LongitudeM1():  
    if MOTO1COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO1COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if longitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto1_longitude = aM7

                elif longitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto1_longitude = aM8

                return moto1_longitude
            ser.close()
        except:
            pass


def LatitudeM2():
    if MOTO2COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO2COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if latitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto2_latitude = aM7
                elif latitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto2_latitude = aM8

                return moto2_latitude
            ser.close()
        except:
            pass


def LongitudeM2():
    if MOTO2COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO2COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if longitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto2_longitude = aM7

                elif longitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto2_longitude = aM8

                return moto2_longitude
            ser.close()
        except:
            pass


def LatitudeM3():
    if MOTO3COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO3COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if latitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto3_latitude = aM7
                    
                elif latitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto3_latitude = aM8

                return moto3_latitude    
            ser.close()
        except:
            pass


def LongitudeM3():
    if MOTO3COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO3COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if longitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto3_longitude = aM7

                elif longitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto3_longitude = aM8

                return moto3_longitude
            ser.close()
        except:
            pass


def LatitudeM4():
    if MOTO4COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = MOTO4COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if latitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto4_latitude = aM7
                    
                elif latitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto4_latitude = aM8

                return moto4_latitude    
            ser.close()
        except:
            pass

def LongitudeM4():
    if MOTO4COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = MOTO4COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if latitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto4_latitude = aM7
                    
                elif latitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto4_latitude = aM8

                return moto4_latitude    
            ser.close()
        except:
            pass


def LatitudeAir():
    if AIRPLANECOM =="NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = AIRPLANECOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if latitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    airplane_latitude = aM7
                    
                elif latitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    airplane_latitude = aM8

                return airplane_latitude    
            ser.close()
        except:
            pass


def  LongitudeAir():
    if AIRPLANECOM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = AIRPLANECOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if longitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    airplane_longitude = aM7

                elif longitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    airplane_longitude = aM8

                return airplane_longitude
            ser.close()
        except:
            pass


def LatitudeHel():
    if HELICOPTERCOM == "NO":
        pass 
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = HELICOPTERCOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if latitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    helicopter_latitude  = aM7
                    
                elif latitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    helicopter_latitude  = aM8

                return helicopter_latitude    
            ser.close()
        except:
            pass


def LongitudeHel():
    if HELICOPTERCOM == "NO":
            pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = HELICOPTERCOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if longitude_result > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    helicopter_longitude = aM7

                elif longitude_result < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    helicopter_longitude = aM8

                return helicopter_longitude
            ser.close()
        except:
            pass


#El loop de la muerte..
while True:
    moto1_la_data = LatitudeM1()
    try:
        M1LA = Decimal(moto1_la_data)
        file_moto1_la = open('lat1.txt', 'w')
        write_moto1_la = str(M1LA)
        file_moto1_la.write(write_moto1_la)
        file_moto1_la.close()
    except:
        M1flo = open('lat1.txt', 'r')
        v1la = M1flo.readline()
        M1LA = Decimal(v1la)
        M1flo.close()

    moto2_la_data = LatitudeM2()
    try:
        M2LA = Decimal(moto2_la_data)
        file_moto2_la = open('lat2.txt', 'w')
        write_moto2_la = str(M2LA)
        file_moto2_la.write(write_moto2_la)
        file_moto2_la.close()
    except:
        M2flo = open('lat2.txt', 'r')
        v2la = M2flo.readline()
        M2LA = Decimal(v2la)
        M2flo.close()

    moto3_la_data = LatitudeM3()
    try:
        M3LA = Decimal(moto3_la_data)
        file_moto3_la = open('lat3.txt', 'w')
        write_moto3_la = str(M3LA)
        file_moto3_la.write(write_moto3_la)
        file_moto3_la.close()
    except:
        M3flo = open('lat3.txt', 'r')
        v3la = M3flo.readline()
        M3LA = Decimal(v3la)
        M3flo.close()

    moto4_la_data = LatitudeM4()
    try:
        M4LA = Decimal(moto4_la_data)
        file_moto4_la = open('lat4.txt', 'w')
        write_moto4_la = str(M4LA)
        file_moto4_la.write(write_moto4_la)
        file_moto4_la.close()
    except:
        M4flo = open('lat4.txt', 'r')
        v4la = M4flo.readline()
        M4LA = Decimal(v4la)
        M4flo.close()

    airplane_la_data = LatitudeAir()
    try:
        AirLA = Decimal(airplane_la_data)
        file_air_la = open('latair.txt', 'w')
        write_air_la = str(AirLA)
        file_air_la.write(write_air_la)
        file_air_la.close()
    except:
        Airflo = open('latair.txt', 'r')
        vairla = Airflo.readline()
        AirLA = Decimal(vairla)
        Airflo.close()

    hel_la_data = LatitudeHel()
    try:
        HelLA = Decimal(hel_la_data)
        file_hel_la = open('lathel.txt', 'w')
        write_hel_la = str(HelLA)
        file_hel_la.write(write_hel_la)
        file_hel_la.close()
    except:
        Helflo = open('lathel.txt', 'r')
        vhella = Helflo.readline()
        HelLA = Decimal(vhella)
        Helflo.close()

    #Brecha espacio temporal
    time.sleep(2)
    #Empezamos con la longitud

    moto1_lo_data = LongitudeM1()
    try:
        M1LO = Decimal(moto1_lo_data)
        file_moto1_lo = open('lon1.txt', 'w')
        write_moto1_lo = str(M1LO)
        file_moto1_lo.write(write_moto1_lo)
        file_moto1_lo.closse()
    except:
        file_moto1_lo = open('lon1.txt', 'r')
        read_moto1_lo = file_moto1_lo.readline()
        M1LO = Decimal(read_moto1_lo)
        file_moto1_lo.close()

    moto2_lo_data = LongitudeM2()
    try:
        M2LO = Decimal(moto2_lo_data)
        file_moto2_lo = open('lon2.txt', 'w')
        write_moto2_lo = str(M2LO)
        file_moto2_lo.write(write_moto2_lo)
        file_moto2_lo.close()
    except:
        file_moto2_lo = open('lon2.txt', 'r')
        read_moto2_lo = file_moto2_lo.readline()
        M2LO = Decimal(read_moto2_lo)
        file_moto2_lo.close()

    moto3_lo_data = LongitudeM3()
    try:
        M3LO = Decimal(moto3_lo_data)
        file_moto3_lo = open('lon3.txt', 'w')
        write_moto3_lo = str(M3LO)
        file_moto3_lo.write(write_moto3_lo)
        file_moto3_lo.close()
    except:
        file_moto3_lo = open('lon3.txt', 'r')
        read_moto3_lo = file_moto3_lo.readline()
        M3LO = Decimal(read_moto3_lo)
        file_moto3_lo.close()

    moto4_lo_data = LongitudeM4()
    try:
        M4LO = Decimal(moto4_lo_data)
        file_moto4_lo = open('lon4.txt', 'w')
        write_moto4_lo = str(M4LO)
        file_moto4_lo.write(write_moto4_lo)
        file_moto4_lo.close()
    except:
        file_moto4_lo = open('lon4.txt', 'r')
        read_moto4_lo = file_moto4_lo.readline()
        M4LO = Decimal(read_moto4_lo)
        file_moto4_lo.close()

    airplane_lo_data = LongitudeAir()
    try:
        AirLo = Decimal(airplane_lo_data)
        file_air_lo = open('lonair.txt', 'w')
        write_air_lo = str(AirLo)
        file_air_lo.write(write_air_lo)
        file_air_lo.close()
    except:
        Airflo = open('lonair.txt', 'r')
        vairlo = Airflo.readline()
        AirLo = Decimal(vairlo)
        Airflo.close()
    
    hel_lo_data = LongitudeHel()
    try:
        HelLo = Decimal(hel_lo_data)
        file_hel_lo = open('lonhel.txt', 'w')
        write_hel_lo = str(HelLo)
        file_hel_lo.write(write_hel_lo)
        file_hel_lo.close()
    except:
        Helflo = open('lonhel.txt', 'r')
        vhello = Helflo.readline()
        HelLo = Decimal(vhello)
        Helflo.close()

    #Open the gpx  file
    file_gpx_browse = open('Gpx_browse.txt', 'r')
    for line in file_gpx_browse:
        gpxbrowse = line

    gpx = gpxpy.parse(open(gpxbrowse))

    track = gpx.tracks[0]
    segment = track.segments[0]

    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.longitude, point.latitude, point.elevation, point.time, segment.get_speed(point_idx)])

    columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
    df = pd.DataFrame(data, columns=columns)

    #Folium
    mymap = folium.Map(location=[ latitude_result, longitude_result], zoom_start=11)

    for coord in df[['Latitude', 'Longitude']].values:
        folium.CircleMarker(location=[coord[0],coord[1]], radius=1, color='red').add_to(mymap)

    try:
        folium.CircleMarker(location=[latitude_result, longitude_result],  radius= 2, color='blue').add_to(mymap)
    except:
        pass

    try:
        folium.CircleMarker(location=[M1LA, M1LO],  radius= 2, color='blue').add_to(mymap)
    except:
        pass

    try:
        folium.CircleMarker(location=[M2LA, M2LO],  radius= 2, color='green').add_to(mymap)
    except:
        pass

    try:
        folium.CircleMarker(location=[M3LA, M3LO],  radius= 2, color='purple').add_to(mymap)
    except:
        pass

    try:
        folium.CircleMarker(location=[M4LA, M4LO],  radius= 2, color='pink').add_to(mymap)
    except:
        pass
    
    try:
        folium.CircleMarker(location=[HelLA, HelLo],  radius= 2, color='black').add_to(mymap)
    except:
        pass

    try:
        folium.CircleMarker(location=[AirLA, AirLo],  radius= 2, color='green').add_to(mymap)
    except:
        pass

    mymap.save('index.html')
    time.sleep(1)

    

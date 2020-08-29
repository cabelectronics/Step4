
'''
 def LatitudeM1():
            ser = serial.Serial()
            ser.baudrate = 9600
            ser.port= MOTO1COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")

                #Convert Latitude from GPRMC to Decimal Grades
                a1 = Decimal(line[3])
                a2 = a1 / 100
                a3 = int(a2)
                a4 = a3 * 100
                a5 = a1 - a4
                a6 = a5 / 60
                a7 = a3 + a6
                
                return a7
            ser.close()

        def LongitudeM1():
            ser = serial.Serial()
            ser.baudrate = 9600
            ser.port= MOTO1COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "GPRMC" in line:
                line = line.split(",")

                    #Convert Longitude from GPRMC to Decimal Grades
                b1 = Decimal(line[5])
                b2 = b1 / 100
                b3 = int(b2)
                b4 = b3 * 100
                b5 = b1 - b4
                b6 = b5 / 60
                b7 = b3 + b6
                b8 = b7 * -1
                    
                return b8

            ser.close()
        subprocess.call(['open.bat'])
        while True:
            M1a7 = LatitudeM1()
            try:
                M1LA = Decimal(M1a7)
                file_moto1_la = open('lat1.txt', 'w')
                write_moto1_la = str(M1LA)
                file_moto1_la.write(write_moto1_la)
                file_moto1_la.close()
            except:
                M1flo = open('lat1.txt', 'r')
                v1la = M1flo.readline()
                M1LA = Decimal(v1la)
                M1flo.close()

            time.sleep(2)

            M1b8 = LongitudeM1()
            try:
                M1LO = Decimal(M1b8)
                M1plo = open('lon1.txt', 'w')
                M1wrlo = str(M1LO)
                M1plo.write(M1wrlo)
                M1plo.close()
            except:
                M1plo = open('lon1.txt', 'r')
                v1lo = M1plo.readline()
                M1LO = Decimal(v1lo)
                M1plo.close()

            #GPX file on the map
            gpx = gpxpy.parse(open(gpx_browse))
            
            track = gpx.tracks[0]
            segment = track.segments[0]

            data = []
            segment_length = segment.length_3d()
            for point_idx, point in enumerate(segment.points):
                data.append([point.longitude, point.latitude, point.elevation, point.time, segment.get_speed(point_idx)])

            columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
            df = pd.DataFrame(data, columns=columns)

            #Folium
            mymap = folium.Map(location=[ M1LA, M1LO], zoom_start=14)

            for coord in df[['Latitude', 'Longitude']].values:
                folium.CircleMarker(location=[coord[0],coord[1]], radius=1, color='red').add_to(mymap)

            folium.CircleMarker(location=[M1LA, M1LO],  radius= 2, color='blue').add_to(mymap)

            mymap.save('index.html')
            time.sleep(3)
'''
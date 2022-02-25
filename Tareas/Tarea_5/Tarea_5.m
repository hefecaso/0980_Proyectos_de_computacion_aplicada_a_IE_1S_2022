pkg load database

conn = pq_connect(setdbopts('dbname','redes','host','localhost',
'port','5432','user','postgres','password','123456'))

N=pq_exec_params(conn, "insert into redes values ('Fernando','201700923');") %insertar datos en la tabla

N=pq_exec_params(conn, 'select * from redes;')
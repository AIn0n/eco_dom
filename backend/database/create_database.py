import pg8000.native
PASSWORD = "123"

con = pg8000.native.Connection("postgres", password=PASSWORD)

#create rooms table
con.run("""
CREATE TABLE rooms
(
    id serial NOT NULL,
    name text NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS rooms
    OWNER to postgres;

ADD CONSTRAINT ct_name UNIQUE (name);
""")

#create enum type
con.run("""
CREATE TYPE energy_class_type AS ENUM
    ('A++', 'A+', 'B', 'C', 'D', 'E', 'F', 'G');

ALTER TYPE energy_class_type
    OWNER TO postgres;
""")

con.run("""
    CREATE TABLE devices
    (
        id serial NOT NULL,
        name text NOT NULL,
        power integer NOT NULL,
        start_time time without time zone NOT NULL,
        end_time time without time zone NOT NULL,
        energy_class energy_class_type NOT NULL,
        room_id serial NOT NULL,
        PRIMARY KEY (id),
        CONSTRAINT fk_room FOREIGN KEY (room_id)
            REFERENCES public.rooms (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
            NOT VALID
    );

    ALTER TABLE IF EXISTS devices
        OWNER to postgres;
""")

con.close()
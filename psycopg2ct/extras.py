import psycopg2ct
import uuid


def register_uuid(oids=None, conn_or_curs=None):
    """Create the UUID type and an uuid.UUID adapter"""
    def adapter(val, cursor):
        return uuid.UUID(val)

    oids = oids if oids is not None else [2950]
    UUID = psycopg2ct.extensions.new_type(oids, "UUID", adapter)
    psycopg2ct.extensions.register_type(UUID, conn_or_curs)

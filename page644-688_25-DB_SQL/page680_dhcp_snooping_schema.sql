-- PAGE678 for a file create_sqlite_ver1.py.

create table if not exists dhcp (
    mac          text not NULL primary key,
    ip           text,
    vlan         text,
    interface    text
);

-- Schema for dhcp-snopping parsing example.

create table dhcp (
    mac          text primary key,
    ip           text,
    vlan         text,
    interface    text,
    switch       text not null references switches(hostname),
    active       text
);

create table switches (
    hostname    text not null primary key,
    location    text
);
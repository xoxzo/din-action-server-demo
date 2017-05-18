#!/bin/sh
sqlite3 db.sqlite3 <<EOF
delete from din_action_dinaction;
insert into din_action_dinaction (id, action_text) values (1,"playback http://anonaka.github.io/100baigaeshi.mp3");
insert into din_action_dinaction (id, action_text) values (2,"playback http://anonaka.github.io/ppap-short.mp3");
insert into din_action_dinaction (id, action_text) values (3,"playback http://anonaka.github.io/oshiokiyo.mp3");
insert into din_action_dinaction (id, action_text) values (4,"playback http://anonaka.github.io/you-are-dead.mp3");
insert into din_action_dinaction (id, action_text) values (5,"transfer +81336042000");
select * from din_action_dinaction;
EOF

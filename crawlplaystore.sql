use crawlplaystore;

create table Website_App_Brain(Application_Rank int(100),Application_Name text, Hyperlink text, date timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

create table Google_Playstore_Data(Application_Name text, Hyperlink text,DocumentID varchar(300), date timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
select * from Google_Playstore_Data;

select * from Website_App_Brain;

create table FossBytes_Data(Application_Name text, Hyperlink text, date timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
select * from FossBytes_Data;


/* To the CUSTOMERS table, add, CUSTOMER_EMAIL, CUSTOMER_LOGIN , CUSTOMER_PASSWORD. Login can be the same as the email, but no two customers can have the same
login.*/

--T1. 

ALTER TABLE CUSTOMERS
ADD CUSTOMER_PLAN VARCHAR(6) NOT NULL
ADD CUSTOMER_EMAIL VARCHAR2(50) UNIQUE
ADD CUSTOMER_LOGIN VARCHAR2(50) UNIQUE
ADD CUSTOMER_PASSWORD VARCHAR2(50);

CREATE TABLE SONGS(
	SONG_ID NUMBER NOT NULL PRIMARY KEY,
  	ITEM_ID NUMBER NOT NULL,
	SONG_NAME VARCHAR2(20) NOT NULL,
	SONG_ALBUM_ONLY VARCHAR2(3) NOT NULL,
	CONSTRAINT chk_yn CHECK (SONG_ALBUM_ONLY='YES' OR SONG_ALBUM_ONLY = 'NO'),
	CONSTRAINT fk_Itemid FOREIGN KEY (ITEM_ID)
    REFERENCES ITEMS(ITEM_ID)
)

CREATE TABLE PLANS(
	PLAN_NAME VARCHAR2(20) NOT NULL PRIMARY KEY,
	PLAN_PLAYS NUMBER NOT NULL,
	PLAN_FEE VARCHAR2(5) NOT NULL
)

CREATE TABLE STREAMS(
	STREAM_ID NUMBER NOT NULL PRIMARY KEY,
	CUSTOMER_ID NUMBER NOT NULL,
	SONG_ID NUMBER NOT NULL,
	STREAM_STATUS VARCHAR2(8) NOT NULL,
	CONSTRAINT chk_stat CHECK (STREAM_STATUS='ACTIVE' OR STREAM_STATUS='INACTIVE'),
	CONSTRAINT fk_Customer FOREIGN KEY (CUSTOMER_ID),
	CONSTRAINT fk_Song FOREIGN KEY (SONG_ID),
	REFERENCES SONGS(SONG_ID)
	REFERENCES CUSTOMERS(CUSTOMER_ID)
)

INSERT INTO PLANS(GOLD,50,50)
INSERT INTO PLANS(SILVER,25,25)
INSERT INTO PLANS(BRONZE,10,10)

UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '1@gmail.com', CUSTOMER_LOGIN = 'MRONE', CUSTOMER_PASSWORD = 'MRONE' CUSTOMER_PLAN = 'GOLD'
WHERE CUSTOMER_ID = 1;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '2@gmail.com', CUSTOMER_LOGIN = 'mr2', CUSTOMER_PASSWORD = 'mr2', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 2;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '3@gmail.com', CUSTOMER_LOGIN = 'mr3', CUSTOMER_PASSWORD = 'mr3', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 3;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '4@gmail.com', CUSTOMER_LOGIN = 'mr4', CUSTOMER_PASSWORD = 'mr4', CUSTOMER_PLAN = 'GOLD'
WHERE CUSTOMER_ID = 4;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '5@gmail.com', CUSTOMER_LOGIN = 'mr5', CUSTOMER_PASSWORD = 'mr5', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 5;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '6@gmail.com', CUSTOMER_LOGIN = 'mr6', CUSTOMER_PASSWORD = 'mr6', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 6;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '7@gmail.com', CUSTOMER_LOGIN = 'mr7', CUSTOMER_PASSWORD = 'mr7', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 7;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '8@gmail.com', CUSTOMER_LOGIN = 'mr8', CUSTOMER_PASSWORD = 'mr8', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 8;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '9@gmail.com', CUSTOMER_LOGIN = 'mr9', CUSTOMER_PASSWORD = 'mr9', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 9;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '10@gmail.com', CUSTOMER_LOGIN = 'mr10', CUSTOMER_PASSWORD = 'mr10', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 10;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '11@gmail.com', CUSTOMER_LOGIN = 'mr11', CUSTOMER_PASSWORD = 'mr11', CUSTOMER_PLAN = 'GOLD'
WHERE CUSTOMER_ID = 11;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '12@gmail.com', CUSTOMER_LOGIN = 'mr12', CUSTOMER_PASSWORD = 'mr12', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 12;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '13@gmail.com', CUSTOMER_LOGIN = 'mr13', CUSTOMER_PASSWORD = 'mr13', CUSTOMER_PLAN = 'GOLD'
WHERE CUSTOMER_ID = 13;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '14@gmail.com', CUSTOMER_LOGIN = 'mr14', CUSTOMER_PASSWORD = 'mr14', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 14;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '15@gmail.com', CUSTOMER_LOGIN = 'mr15', CUSTOMER_PASSWORD = 'mr15', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 15;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '16@gmail.com', CUSTOMER_LOGIN = 'mr16', CUSTOMER_PASSWORD = 'mr16', CUSTOMER_PLAN = 'GOLD'
WHERE CUSTOMER_ID = 16;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '17@gmail.com', CUSTOMER_LOGIN = 'mr17', CUSTOMER_PASSWORD = 'mr17', CUSTOMER_PLAN = 'GOLD'
WHERE CUSTOMER_ID = 17;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '18@gmail.com', CUSTOMER_LOGIN = 'mr18', CUSTOMER_PASSWORD = 'mr18', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 18;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '19@gmail.com', CUSTOMER_LOGIN = 'mr19', CUSTOMER_PASSWORD = 'mr19', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 19;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '20@gmail.com', CUSTOMER_LOGIN = 'mr20', CUSTOMER_PASSWORD = 'mr20', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 20;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '21@gmail.com', CUSTOMER_LOGIN = 'mr21', CUSTOMER_PASSWORD = 'mr21', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 21;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '22@gmail.com', CUSTOMER_LOGIN = 'mr22', CUSTOMER_PASSWORD = 'mr22', CUSTOMER_PLAN = 'SILVER'
WHERE CUSTOMER_ID = 22;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '23@gmail.com', CUSTOMER_LOGIN = 'mr23', CUSTOMER_PASSWORD = 'mr23', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 23;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '24@gmail.com', CUSTOMER_LOGIN = 'mr24', CUSTOMER_PASSWORD = 'mr24', CUSTOMER_PLAN = 'BRONZE'
WHERE CUSTOMER_ID = 24;
UPDATE CUSTOMERS
SET CUSTOMER_EMAIL = '25@gmail.com', CUSTOMER_LOGIN = 'mr25', CUSTOMER_PASSWORD = 'mr25', CUSTOMER_PLAN = 'GOLD'
WHERE CUSTOMER_ID = 25;

INSERT INTO SONGS
VALUES ('1','7', 'them whistle comfort', 'NO');
INSERT INTO SONGS
VALUES ('2','3', 'is wont they', 'YES');
INSERT INTO SONGS
VALUES ('3','9', 'they whistle cloak', 'NO');
INSERT INTO SONGS
VALUES ('4','7', 'strained strained this', 'YES');
INSERT INTO SONGS
VALUES ('5','8', 'team team desire', 'NO');
INSERT INTO SONGS
VALUES ('6','10', 'raging a finaly', 'YES');
INSERT INTO SONGS
VALUES ('7','5', 'is whistle desire', 'YES');
INSERT INTO SONGS
VALUES ('8','10', 'wont team is', 'NO');
INSERT INTO SONGS
VALUES ('9','6', 'they them cloak', 'NO');
INSERT INTO SONGS
VALUES ('10','1', 'it whistle team', 'YES');
INSERT INTO SONGS
VALUES ('11','5', 'lonely team this', 'NO');
INSERT INTO SONGS
VALUES ('12','3', 'bird this cloak', 'YES');
INSERT INTO SONGS
VALUES ('13','1', 'team them aspire', 'NO');
INSERT INTO SONGS
VALUES ('14','6', 'desire the that', 'NO');
INSERT INTO SONGS
VALUES ('15','1', 'lonely team team', 'YES');
INSERT INTO SONGS
VALUES ('16','9', 'finaly team desire', 'YES');
INSERT INTO SONGS
VALUES ('17','10', 'lonely whistle bird', 'YES');
INSERT INTO SONGS
VALUES ('18','1', 'it comfort it', 'YES');
INSERT INTO SONGS
VALUES ('19','7', 'desire finaly a', 'NO');
INSERT INTO SONGS
VALUES ('20','4', 'finaly it them', 'YES');

INSERT INTO STREAMS
VALUES ('1','15', '15', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('2','4', '5', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('3','20', '9', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('4','4', '2', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('5','14', '17', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('6','15', '9', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('7','12', '5', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('8','12', '17', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('9','8', '11', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('10','23', '16', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('11','24', '11', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('12','24', '15', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('13','6', '5', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('14','1', '6', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('15','11', '2', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('16','8', '17', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('17','4', '7', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('18','20', '2', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('19','2', '3', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('20','20', '8', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('21','3', '2', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('22','21', '9', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('23','12', '13', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('24','10', '10', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('25','11', '16', 'ACTIVE');
INSERT INTO STREAMS
VALUES ('26','13', '11', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('27','20', '15', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('28','5', '11', 'INACTIVE');
INSERT INTO STREAMS
VALUES ('29','10', '1', 'ACTIVE');

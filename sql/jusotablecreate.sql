CREATE TABLE `juso` (
	dorocode VARCHAR(12) NOT NULL COMMENT '도로명코드 PK1',
	doro VARCHAR(80) NOT NULL comment '도로명이름',
	dororoma VARCHAR(80) comment '도로명 로마자',
    emdserial VARCHAR(2) COMMENT '읍면동 일련번호 PK2',
	sido VARCHAR(20) COMMENT '시도명',
	sidoroma VARCHAR(40) COMMENT '시도 로마자',
	sigungo VARCHAR(20) COMMENT'시군구명',
	sigungoroma VARCHAR(40) COMMENT '시군구 로마자',
	emd VARCHAR(20) COMMENT '읍면동명',
	emdroma VARCHAR(40) COMMENT '읍면동 로마자',
	emdid VARCHAR(1) COMMENT '읍면동 구분 0:읍면, 1:동, 2:미부여',
	emdcode VARCHAR(3) COMMENT '읍면동코드',
	used VARCHAR(1) COMMENT '사용여부 0:사용, 1:미사용',
    primary key(dorocode, emdserial)
);
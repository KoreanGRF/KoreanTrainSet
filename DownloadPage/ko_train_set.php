<?php
	$_TL['section'] = 'ottd > newgrf';
	$_TL['page_title'] = 'OpenTTD > NewGRF > 한국 열차 세트';

	// 기본 설정
	$default = array(
		'grfcode' => 'ko_train_set',
		'filename_base' => 'Korean_Train_Set',
		'github' => 'https://github.com/KoreanGRF/KoreanTrainSet',
	);

	// 헤더
	require_once '../../../head.php';

	// 언어
	$lang_list = array('kr', 'en', 'jp', 'es');

	// 추가되는 차량
	$added_vehicles = array('MET1N', 'MET2N', 'MET3N', 'MET4N', 'MET59', 'METBN', 'METKC', 'KCITX', 'METAR', 'D000N',
				'ICNM1',
				'DAEGU1', 'DAEGU2',
				'BUSAN1', 'BUSAN2', 'BUSAN3', 'BUSAN4',
				'K4400', 'K7000', 'K7x00', 'K8000', 'K8100', 'K8200', 'K8500', 'SMEPP', 'ITXSME',
				'NURIRO', 'CDC', 'NDC',
				'KTX1N', 'KTX2N', 'FLATC', 'HOPPERC', 'SMALLCARGO', 'NRRCW', 'KTXCW', 'SMECW', 'MGHCW', 'CAFECW', 'TILCW',
				'SUBCW', 'GENCW', 'CDCCW');

	// 공통 부분 삽입
	require_once './inc.common_header.php';
	require_once './inc.common_body.php';

	require_once '../../../foot.php';
?>
# Don't try to understand the logic, just roll with it.
seat_mappings = {
    '230':'U1-100',
    '229':'U1-99',
    '228':'U1-98',
    '227':'U1-97',
    '226':'U1-96',
    '225':'U1-95',
    '224':'U1-94',
    '223':'U1-93',
    '222':'U1-92',
    '221':'U1-91',
    '220':'U1-90',
    '219':'U1-89',
    '218':'U1-88',
    '217':'U1-87',
    '216':'U1-86',
    '215':'U1-85',
    '214':'U1-84',
    '213':'U1-83',
    '212':'U1-82',
    '211':'U1-81',
    '210':'U1-80',
    '208':'U1-78',
    '207':'U1-77',
    '206':'U1-76',
    '205':'U1-75',
    '204':'U1-74',
    '203':'U1-73',
    '202':'U1-72',
    '201':'U1-71',
    '200':'U1-70',
    '199':'U1-69',
    '198':'U1-68',
    '197':'U1-67',
    '196':'U1-66',
    '195':'U1-65',
    '194':'U1-64',
    '193':'U1-63',
    '192':'U1-62',
    '191':'U1-61',
    '190':'U1-60',
    '189':'U1-59',
    '188':'U1-58',
    '187':'U1-57',
    '186':'U1-56',
    '185':'U1-55',
    '184':'U1-54',
    '183':'U1-53',
    '182':'U1-52',
    '181':'U1-51',
    '180':'D1-100',
    '179':'D1-99',
    '178':'D1-98',
    '177':'D1-97',
    '176':'D1-95',
    '175':'D1-96',
    '174':'D1-94',
    '173':'D1-93',
    '172':'D1-92',
    '171':'D1-91',
    '170':'D1-90',
    '169':'D1-89',
    '168':'D1-88',
    '167':'D1-87',
    '166':'D1-86',
    '165':'D1-85',
    '164':'D1-84',
    '163':'D1-83',
    '162':'D1-82',
    '161':'D1-81',
    '160':'D1-80',
    '159':'D1-79',
    '158':'D1-78',
    '156':'D1-77',
    '155':'D1-76',
    '154':'D1-75',
    '153':'D1-74',
    '152':'D1-73',
    '151':'D1-72',
    '150':'D1-71',
    '149':'D1-70',
    '148':'D1-69',
    '147':'D1-68',
    '146':'D1-67',
    '145':'D1-66',
    '144':'D1-65',
    '143':'D1-64',
    '142':'D1-63',
    '141':'D1-62',
    '140':'D1-61',
    '139':'D1-60',
    '138':'D1-59',
    '137':'D1-58',
    '136':'D1-57',
    '135':'D1-56',
    '134':'D1-55',
    '133':'D1-54',
    '132':'D1-53',
    '131':'D1-52',
    '130':'D1-51',
    '129':'D1-50',
    '128':'D1-49',
    '127':'D1-48',
    '126':'D1-47',
    '125':'D1-46',
    '124':'D1-45',
    '123':'D1-44',
    '122':'D1-43',
    '121':'D1-42',
    '120':'D1-41',
    '119':'U1-50',
    '118':'U1-49',
    '117':'U1-48',
    '116':'U1-47',
    '115':'U1-46',
    '114':'U1-45',
    '113':'U1-44',
    '112':'U1-43',
    '111':'U1-42',
    '110':'U1-41',
    '109':'D1-40',
    '108':'D1-39',
    '107':'D1-38',
    '106':'D1-37',
    '105':'D1-36',
    '104':'D1-35',
    '103':'D1-34',
    '102':'D1-33',
    '101':'D1-32',
    '100':'D1-31',
    '99' :'U1-40',
    '98' :'U1-39',
    '97' :'U1-38',
    '96' :'U1-37',
    '95' :'U1-36',
    '94' :'U1-35',
    '93' :'U1-34',
    '92' :'U1-33',
    '91' :'U1-32',
    '90' :'U1-31',
    '89' :'U1-30',
    '88' :'U1-29',
    '87' :'U1-28',
    '86' :'U1-27',
    '85' :'U1-26',
    '84' :'U1-25',
    '83' :'U1-24',
    '82' :'U1-23',
    '81' :'U1-22',
    '80' :'U1-21',
    '79' :'D1-30',
    '78' :'D1-29',
    '77' :'D1-28',
    '76' :'D1-27',
    '75' :'D1-26',
    '74' :'D1-25',
    '73' :'D1-24',
    '72' :'D1-23',
    '71' :'D1-22',
    '70' :'D1-21',
    '69' :'D1-20',
    '68' :'D1-19',
    '67' :'D1-18',
    '66' :'D1-17',
    '65' :'D1-16',
    '64' :'D1-15',
    '63' :'D1-14',
    '62' :'D1-13',
    '61' :'D1-12',
    '60' :'D1-11',
    '59' :'D1-10',
    '58' :'D1-09',
    '57' :'D1-08',
    '56' :'D1-07',
    '55' :'D1-06',
    '54' :'D1-05',
    '53' :'D1-04',
    '52' :'D1-03',
    '51' :'D1-02',
    '50' :'D1-01',
    '49' :'U1-20',
    '48' :'U1-19',
    '47' :'U1-18',
    '46' :'U1-17',
    '45' :'U1-16',
    '44' :'U1-15',
    '43' :'U1-14',
    '42' :'U1-13',
    '41' :'U1-12',
    '40' :'U1-11',
    '39' :'U1-10',
    '38' :'U1-09',
    '37' :'U1-08',
    '36' :'U1-07',
    '35' :'U1-06',
    '34' :'U1-05',
    '33' :'U1-04',
    '32' :'U1-03',
    '31' :'U1-02',
    '30' :'U1-01'
}
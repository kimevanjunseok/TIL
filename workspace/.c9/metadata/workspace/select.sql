{"changed":true,"filter":false,"title":"select.sql","tooltip":"/select.sql","value":"-- 테이블값 모두 가져오기\nSELECT * FROM classmate;\n\n-- 테이블의 특정컬럼만 가져오기\nSELECT id, name FROM classmate;\n\n-- 가져오는 row(레코드)개수 지정하기\nSELECT id, name FROM classmate LIMIT 2;\n\n-- 가져오는 레코드에 시작점 지정(2칸 뛰고 1개 출력)\nSELECT * FROM classmate LIMIT 1 OFFSET 2;\n\n-- 특정한 값을 가진 row만 조회하기\nSELECT * FROM classmate WHERE address='서울';\nSELECT * FROM classmate WHERE id=2;\n\n-- 서울에 사는 사람의 이름은?\nSELECT name FROM classmate WHERE address='서울';","undoManager":{"mark":81,"position":100,"stack":[[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["오"],"id":103}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["는"],"id":105}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":[" "],"id":106}],[{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["r"],"id":107},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["o"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["w"]}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":13},"action":"insert","lines":["()"],"id":108}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["f"],"id":109},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["p"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["z"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["h"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["e"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["m"],"id":110},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["e"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["h"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["z"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["p"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["f"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["레"],"id":114}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["코"],"id":117}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["드"],"id":118}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["r"],"id":119},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["o"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["t"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":[" "],"id":120},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["w"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["l"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["w"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["j"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["d"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["g"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["k"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["w"]}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"remove","lines":["w"],"id":121},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"remove","lines":["k"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"remove","lines":["g"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"remove","lines":["d"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["j"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["w"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["l"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["w"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":[" "]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["n"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["t"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["o"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["r"]}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["개"],"id":125}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["수"],"id":126}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":[" "],"id":127}],[{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["지"],"id":131}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["정"],"id":133}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["하"],"id":137}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["기"],"id":138}],[{"start":{"row":7,"column":39},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":139},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":3},"action":"insert","lines":["-- "],"id":140}],[{"start":{"row":9,"column":3},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":141}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":41},"action":"insert","lines":["SELECT * FROM classmate LIMIT 1 OFFSET 2;"],"id":142}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["2"],"id":143}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"remove","lines":["2"],"id":144},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"remove","lines":[" "]}],[{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":[" "],"id":145},{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["r"]},{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["k"]},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["w"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["u"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["d"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["h"]}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"remove","lines":["h"],"id":146},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"remove","lines":["d"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"remove","lines":["u"]},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"remove","lines":["w"]},{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"remove","lines":["k"]},{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"remove","lines":["r"]}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["가"],"id":150}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["져"],"id":153}],[{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["오"],"id":156}],[{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["는"],"id":158}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":[" "],"id":159}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["레"],"id":163}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["코"],"id":166}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["드"],"id":169}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["에"],"id":170}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":[" "],"id":171}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["시"],"id":175}],[{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["작"],"id":177}],[{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["점"],"id":180}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":[" "],"id":181}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["지"],"id":185}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["정"],"id":187}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":21},"action":"insert","lines":["()"],"id":188}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["2"],"id":189},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["z"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["k"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["s"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["E"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["N"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["l"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["r"]}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["h"],"id":190}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":[" "],"id":191}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":[" "],"id":192},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"remove","lines":["h"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"remove","lines":["r"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["l"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["N"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["E"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["s"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["k"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["z"]}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["칸"],"id":195}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":[" "],"id":196}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["뛰"],"id":201}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["고"],"id":202}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":[" "],"id":203}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["1"],"id":204}],[{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["개"],"id":206}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":[" "],"id":207}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["출"],"id":210}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["력"],"id":214}],[{"start":{"row":10,"column":41},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":215},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":216}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":43},"action":"insert","lines":["SELECT * FROM classmate WHERE address='서울';"],"id":217}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":3},"action":"insert","lines":["-- "],"id":218}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"insert","lines":["특"],"id":221}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["정"],"id":224}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["한"],"id":227}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":[" "],"id":228}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["값"],"id":235}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["을"],"id":238}],[{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":[" "],"id":239}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["가"],"id":243}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["진"],"id":245}],[{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":[" "],"id":246}],[{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["r"],"id":247},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["o"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["w"]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["만"],"id":250}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":[" "],"id":251}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["조"],"id":255}],[{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["회"],"id":259}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["하"],"id":262}],[{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["기"],"id":263}],[{"start":{"row":13,"column":43},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":264}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":35},"action":"insert","lines":["SELECT * FROM classmate WHERE id=2;"],"id":265}],[{"start":{"row":14,"column":35},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":266},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":3},"action":"insert","lines":["-- "],"id":267}],[{"start":{"row":16,"column":3},"end":{"row":16,"column":4},"action":"insert","lines":["서"],"id":271}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["울"],"id":273}],[{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["에"],"id":275}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":[" "],"id":276}],[{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["사"],"id":280}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["는"],"id":282}],[{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":[" "],"id":283}],[{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["사"],"id":287}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["람"],"id":289}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["의"],"id":292}],[{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":[" "],"id":293}],[{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["이"],"id":297}],[{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["름"],"id":299}],[{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["은"],"id":302}],[{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":["?"],"id":303}],[{"start":{"row":16,"column":18},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":304}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":46},"action":"insert","lines":["SELECT name FROM classmate WHERE address='서울';"],"id":305}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":18},"end":{"row":16,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1548923191462}
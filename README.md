# ThaiAgroPriceScraper
# โปรแกรมดึงข้อมูลราคาสินค้าเกษจรจากเวบไซท์ http://www.pandinthong.com/price/
Thai agricultural product price scraper from Thai Central Agricultural Price website (They not open this API to public, we need to use it then scrape it by ourself)
โปรแกรมนี้เป็นตัวอย่างการเขียนโปรแกรม python เพื่อดึงข้อมูลจากหน้าเวบไซท์เพื่อนำไปใช้ประโยชน์ในด้านอื่นต่อไป โดยตัวอย่างในที่นี่เป็นการดึงข้อมูลราคาสินค้าเกษตรประจำกันจากเวบไซท์ http://www.pandinthong.com/price/ ซึ่งแสดงราคาสินค้าเกษตรประจำวัน แต่ไม่เปิด API ให้นักพัฒนาภายนอกนำข้อมูลราคาสินค้าประจำวันไปพัฒนาต่อได้ ตัวอย่างโปรแกรม python นี้จึงเป็นการนำข้อมูลราคาสินค้าบนเวบไซท์แห่งนี้แปลงออกมาให้อยู่ในรูปแบบ JSON ซึ่งจะสามารถนำข้อมูลราคาสินค้าเกษตรเหล่านี้ไปใช้ประโยชน์ต่อได้อีกมากมาย

![workflow image](https://user-images.githubusercontent.com/466386/30801039-2d0c4648-a20c-11e7-9b29-0c737d1c0cec.png)

## Example out put printing 
## ตัวอย่างข้อมูลที่แสดงจากโปรแกรม

```javascript
Order: 0001, ProvinceTH: ขอนแก่น, ProvinceEN: Khon Kaen, Market: ท่าข้าว ธกส. ขอนแก่น, TypeTH	: ข้าวหอมมะลิ 105 (ต้นข้าว 35 กรัม), TypeEN	: Jasmine Rice 105, Price (Baht): 12,500.00, unitTH	: บาท/ตัน, Change	: -300.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0002, ProvinceTH: ศรีสะเกษ, ProvinceEN: Si Sa Ket, Market: ตลาดกลางพืชไร่ ศรีสะเกษ, TypeTH	: ข้าวหอมมะลิ 105 (ต้นข้าว 35 กรัม), TypeEN	: Jasmine Rice 105, Price (Baht): 13,000.00, unitTH	: บาท/ตัน, Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0003, ProvinceTH: นครราชสีมา, ProvinceEN: Nakhon Ratchasima, Market: บริษัท สงวนวงศ์อุตสาหกรรม จำกัด, TypeTH	: มันสำปะหลังสด แป้ง 30%, TypeEN	: Fresh cassava starch 30%, Price (Baht): 1.95, unitTH	: บาท/กก., Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0004, ProvinceTH: นครราชสีมา, ProvinceEN: Nakhon Ratchasima, Market: บริษัท สงวนวงศ์อุตสาหกรรม จำกัด, TypeTH	: มันสำปะหลังสด แป้ง 25%, TypeEN	: Fresh cassava flour 25%, Price (Baht): 1.70, unitTH	: บาท/กก., Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0005, ProvinceTH: ยโสธร, ProvinceEN: Yasothon, Market: โรงสีกิจทวียโสธร, TypeTH	: ข้าวหอมมะลิ 105 (ต้นข้าว 35 กรัม), TypeEN	: Jasmine Rice 105, Price (Baht): 13,900.00, unitTH	: บาท/ตัน, Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0006, ProvinceTH: บุรีรัมย์, ProvinceEN: Buri Ram, Market: โรงสีสหพัฒนา, TypeTH	: ข้าวหอมมะลิ 105 (ต้นข้าว 35 กรัม), TypeEN	: Jasmine Rice 105, Price (Baht): 13,000.00, unitTH	: บาท/ตัน, Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0007, ProvinceTH: สุรินทร์, ProvinceEN: Surin, Market: โรงสีเต็กเฮง, TypeTH	: ข้าวหอมมะลิ 105 (ต้นข้าว 35 กรัม), TypeEN	: Jasmine Rice 105, Price (Baht): 13,000.00, unitTH	: บาท/ตัน, Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0008, ProvinceTH: ร้อยเอ็ด, ProvinceEN: Roi Et, Market: โรงสีสหกรณ์การเกษตรสุวรรณภูมิ, TypeTH	: ข้าวหอมมะลิ 105 (ต้นข้าว 35 กรัม), TypeEN	: Jasmine Rice 105, Price (Baht): 13,000.00, unitTH	: บาท/ตัน, Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0021, ProvinceTH: นครศรีธรรมราช, ProvinceEN: Nakhon Si Thammarat, Market: ตลาดกลางยางพารา นครศรีธรรมราช, TypeTH	: ยางแผ่นดิบชั้น 3, TypeEN	: Raw sheet rubber, floor 3, Price (Baht): 50.29, unitTH	: บาท/กก., Change	: -0.34, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0022, ProvinceTH: สุราษฎร์ธานี, ProvinceEN: Surat Thani, Market: สัมฤทธิ์การยาง, TypeTH	: ยางแผ่นดิบชั้น 3, TypeEN	: Raw sheet rubber, floor 3, Price (Baht): 49.00, unitTH	: บาท/กก., Change	: 1.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0023, ProvinceTH: ระยอง, ProvinceEN: Rayong, Market: ร้านสินการยาง, TypeTH	: ยางแผ่นดิบชั้น 3, TypeEN	: Raw sheet rubber, floor 3, Price (Baht): 50.00, unitTH	: บาท/กก., Change	: -1.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0024, ProvinceTH: ระยอง, ProvinceEN: Rayong, Market: บริษัท ไทยรับเบอร์ลาเท็กกรุ๊ป, TypeTH	: น้ำยางสด, TypeEN	: Fresh La Tex, Price (Baht): 38.00, unitTH	: บาท/กก., Change	: -2.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0025, ProvinceTH: สมุทรสาคร, ProvinceEN: Samut Sakhon, Market: ตลาดกลางกุ้งสมุทรสาคร, TypeTH	: กุ้งขนาด 50 ตัว/กก., TypeEN	: Shrimp size 50/kg., Price (Baht): 190.00, unitTH	: บาท/กก., Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0035, ProvinceTH: ปราจีนบุรี, ProvinceEN: Prachin Buri, Market: จุกพืชไร่, TypeTH	: ข้าวหอมมะลิจังหวัด, TypeEN	: Province of jasmine rice, Price (Baht): 8,500.00, unitTH	: บาท/ตัน, Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0050, ProvinceTH: ชลบุรี, ProvinceEN: Chon Buri, Market: โรงงานอาหารสยาม, TypeTH	: สับปะรดโรงงาน, TypeEN	: Pineapple plant, Price (Baht): 4.30, unitTH	: บาท/กก., Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0051, ProvinceTH: ระยอง, ProvinceEN: Rayong, Market: บริษัท SAICO จำกัด, TypeTH	: สับปะรดโรงงาน, TypeEN	: Pineapple plant, Price (Baht): 4.60, unitTH	: บาท/กก., Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0052, ProvinceTH: ราชบุรี, ProvinceEN: Ratchaburi, Market: กลุ่มสหกรณ์ผู้ปลูกสับปะรด, TypeTH	: สับปะรดโรงงาน, TypeEN	: Pineapple plant, Price (Baht): 4.30, unitTH	: บาท/กก., Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
Order: 0053, ProvinceTH: ประจวบคีรีขันธ์, ProvinceEN: Prachuap Khiri Khan, Market: บริษัท กุยบุรีผลไม้กระป๋อง จำกัด (เค.เอฟ.ซี.), TypeTH	: สับปะรดโรงงาน, TypeEN	: Pineapple plant, Price (Baht): 4.40, unitTH	: บาท/กก., Change	: 0.00, DateTH	: 25 ก.ย. 2560 ,DateEN	: 2017-09-25, Source	: สศก., epoch	: 1506272400
```

## Example of output in JSON format
## ตัวอย่างข้อมูลในรูปแบบ JSON
```
[{
	'province_th': u'\u0e02\u0e2d\u0e19\u0e41\u0e01\u0e48\u0e19',
	'timestamp': 1506272400,
	'price': u'12,
	500.00',
	'oid': u'0001',
	'date_th': u'25\u0e01.\u0e22.2560',
	'market': u'\u0e17\u0e48\u0e32\u0e02\u0e49\u0e32\u0e27\u0e18\u0e01\u0e2a.\u0e02\u0e2d\u0e19\u0e41\u0e01\u0e48\u0e19',
	'product_en': u'JasmineRice105',
	'unit': u'\u0e1a\u0e32\u0e17/\u0e15\u0e31\u0e19',
	'date_en': u'2017-09-25',
	'product_th': u'\u0e02\u0e49\u0e32\u0e27\u0e2b\u0e2d\u0e21\u0e21\u0e30\u0e25\u0e34105(\u0e15\u0e49\u0e19\u0e02\u0e49\u0e32\u0e2735\u0e01\u0e23\u0e31\u0e21)',
	'source': u'\u0e2a\u0e28\u0e01.',
	'province_en': u'KhonKaen',
	'change': u'-300.00'
},
{
	'province_th': u'\u0e0a\u0e25\u0e1a\u0e38\u0e23\u0e35',
	'timestamp': 1506272400,
	'price': u'4.30',
	'oid': u'0039',
	'date_th': u'25\u0e01.\u0e22.2560',
	'market': u'\u0e42\u0e23\u0e07\u0e07\u0e32\u0e19\u0e2d\u0e32\u0e2b\u0e32\u0e23\u0e2a\u0e22\u0e32\u0e21',
	'product_en': u'Pineappleplant',
	'unit': u'\u0e1a\u0e32\u0e17/\u0e01\u0e01.',
	'date_en': u'2017-09-25',
	'product_th': u'\u0e2a\u0e31\u0e1a\u0e1b\u0e30\u0e23\u0e14\u0e42\u0e23\u0e07\u0e07\u0e32\u0e19',
	'source': u'\u0e2a\u0e28\u0e01.',
	'province_en': u'ChonBuri',
	'change': u'0.00'
},
{
	'province_th': u'\u0e23\u0e30\u0e22\u0e2d\u0e07',
	'timestamp': 1506272400,
	'price': u'4.60',
	'oid': u'0040',
	'date_th': u'25\u0e01.\u0e22.2560',
	'market': u'\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17SAICO\u0e08\u0e33\u0e01\u0e31\u0e14',
	'product_en': u'Pineappleplant',
	'unit': u'\u0e1a\u0e32\u0e17/\u0e01\u0e01.',
	'date_en': u'2017-09-25',
	'product_th': u'\u0e2a\u0e31\u0e1a\u0e1b\u0e30\u0e23\u0e14\u0e42\u0e23\u0e07\u0e07\u0e32\u0e19',
	'source': u'\u0e2a\u0e28\u0e01.',
	'province_en': u'Rayong',
	'change': u'0.00'
},
{
	'province_th': u'\u0e09\u0e30\u0e40\u0e0a\u0e34\u0e07\u0e40\u0e17\u0e23\u0e32',
	'timestamp': 1506013200,
	'price': u'190.00',
	'oid': u'0075',
	'date_th': u'22\u0e01.\u0e22.2560',
	'market': u'\u0e23\u0e49\u0e32\u0e19\u0e2a\u0e34\u0e19\u0e07\u0e2d\u0e01\u0e07\u0e32\u0e21',
	'product_en': u'Shrimpsize50/kg.',
	'unit': u'\u0e1a\u0e32\u0e17/\u0e01\u0e01.',
	'date_en': u'2017-09-22',
	'product_th': u'\u0e01\u0e38\u0e49\u0e07\u0e02\u0e19\u0e32\u0e1450\u0e15\u0e31\u0e27/\u0e01\u0e01.',
	'source': u'\u0e2a\u0e28\u0e01.',
	'province_en': u'Chachoengsao',
	'change': u'0.00'
},
{
	'province_th': u'\u0e09\u0e30\u0e40\u0e0a\u0e34\u0e07\u0e40\u0e17\u0e23\u0e32',
	'timestamp': 1506013200,
	'price': u'170.00',
	'oid': u'0076',
	'date_th': u'22\u0e01.\u0e22.2560',
	'market': u'\u0e23\u0e49\u0e32\u0e19\u0e2a\u0e34\u0e19\u0e07\u0e2d\u0e01\u0e07\u0e32\u0e21',
	'product_en': u'Shrimpsize60/kg.',
	'unit': u'\u0e1a\u0e32\u0e17/\u0e01\u0e01.',
	'date_en': u'2017-09-22',
	'product_th': u'\u0e01\u0e38\u0e49\u0e07\u0e02\u0e19\u0e32\u0e1460\u0e15\u0e31\u0e27/\u0e01\u0e01.',
	'source': u'\u0e2a\u0e28\u0e01.',
	'province_en': u'Chachoengsao',
	'change': u'0.00'
},
{
	'province_th': u'\u0e19\u0e04\u0e23\u0e1b\u0e10\u0e21',
	'timestamp': 1506013200,
	'price': u'150.00',
	'oid': u'0100',
	'date_th': u'22\u0e01.\u0e22.2560',
	'market': u'\u0e15\u0e25\u0e32\u0e14\u0e1b\u0e10\u0e21\u0e21\u0e07\u0e04\u0e25\u0e17\u0e48\u0e32\u0e23\u0e16\u0e1a\u0e02\u0e2a.',
	'product_en': u'The\xa0largeLemon',
	'unit': u'\u0e1a\u0e32\u0e17/\u0e23\u0e49\u0e2d\u0e22\u0e1c\u0e25',
	'date_en': u'2017-09-22',
	'product_th': u'\u0e21\u0e30\u0e19\u0e32\u0e27\u0e1c\u0e25\u0e02\u0e19\u0e32\u0e14\u0e43\u0e2b\u0e0d\u0e48',
	'source': u'\u0e2a\u0e28\u0e01.',
	'province_en': u'NakhonPathom',
	'change': u'0.00'
}]
```

# สุดท้ายนี้โปรแกรมนี้จัดทำขึ้นเพื่อให้ประโยชน์ด้านการศึกษาการพัฒนาโปรแกรม python เท่านั้น ไม้ได้นำข้อมูลที่แกะออกมาไปใช้ประโยชน์ในเชิงพาณิชย์แต่อย่างใด

import 'package:flutter/material.dart';
import 'package:tave/screens/result.dart';
import 'package:tave/controller/functions.dart';

class WebPage extends StatefulWidget {
  @override
  _WebPageState createState() => _WebPageState();
}

class _WebPageState extends State<WebPage> {
  String? dropdownValue;
  final WebtoonService webtoonService = WebtoonService('http://192.168.0.42');
  TextEditingController textEditingController = TextEditingController();
  List<String> dropdownOptions = []; //dropdownOptions 필드를 추가


  Future<void> _getWebtoonCharacters(TextEditingController controller) async {
    String webtoonTitle = controller.text;
    WebtoonService webtoonService = WebtoonService('http://192.168.0.42');

    try {
      List<String> characters = await webtoonService.fetchCharacters(webtoonTitle);
      setState(() {
         dropdownOptions = characters;
      });
    } catch (e) {
      print('캐릭터 목록 가져오기 실패: $e');
    }
  }


  void _navigateToResult() async {
    String selectedText = textEditingController.text;

    // 사용자가 웹툰 주연 캐릭터를 선택하지 않았다면 에러 메시지를 표시
    if (dropdownValue == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('캐릭터를 선택해주세요'),
          backgroundColor: Colors.orange,
        ),
      );
      return;
    }

    // 사용자가 웹툰 제목을 입력하지 않았다면 에러 메시지를 표시
    if (selectedText.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('웹툰 제목을 입력해주세요'),
          backgroundColor: Colors.orange,
        ),
      );
      return;
    }

    try {
      final Map<String, dynamic> characterInfo = await webtoonService.fetchCharacterInfo(dropdownValue ?? 'default_value');

      // 결과 페이지로 이동하면서 선택된 웹툰 제목과 캐릭터 정보를 전달합니다.
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ResultPage(
            webtoonTitle: selectedText,
            characterInfo: characterInfo,
          ),
        ),
      );
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Character information could not be fetched. Please try again.'),
          backgroundColor: Colors.red,
        ),
      );
      print('Error fetching character info: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    // 이미지의 가로 길이를 기준으로 전체 너비를 계산합니다.
    double totalWidth = MediaQuery.of(context).size.width - 300; // 전체 너비 - 양쪽 패딩

    // 폰트 스타일 정의
    TextStyle FontStyle1 = TextStyle(
      fontFamily: 'Yeongdeok Snow Crab',
      fontSize: 20, // 원하는 폰트 사이즈로 조정
    );

    TextStyle FontStyle2 = TextStyle(
      fontFamily: 'Yeongdeok Sea',
      fontSize: 20, // 원하는 폰트 사이즈로 조정
    );

    Color backgroundColor = Color.fromRGBO(102, 255, 102, 0.4);

    return Scaffold(
      backgroundColor: backgroundColor,

      appBar: AppBar(
        toolbarHeight: 80,
        backgroundColor: backgroundColor, // AppBar의 배경색을 변경합니다.
        title: Column(
          mainAxisSize: MainAxisSize.min, // Column의 크기를 내용물에 맞춤
          crossAxisAlignment: CrossAxisAlignment.center, // 가로축을 중앙 정렬
          children: <Widget>[
            Text(
              'Hello 캐릭 TO 리얼 World !',
              style: FontStyle2.copyWith(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              '여러분이 원하는 웹툰의 정보로 배우를 추천해줘요!', // 추가하고 싶은 텍스트
              style: FontStyle2, // 이 부분은 원하는 스타일로 변경 가능
            ),
          ],
        ),
        centerTitle: true, // 제목을 중앙에 정렬합니다.
      ),

      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            SizedBox(height: 20),
            // 이미지 로딩 부분
        Center(
        child: Stack(
          children: <Widget>[
          Container(
          height: 450,
          width: totalWidth,
          decoration: BoxDecoration(
            // 이미지 주변에 흰색 테두리를 추가합니다.
            border: Border.all(color: Colors.white, width: 3.0),
            borderRadius: BorderRadius.circular(12.0), // 테두리를 둥글게 만들고 싶다면 값을 조정하세요.
          ),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(12.0), // Container의 borderRadius와 일치시키세요.
            child: Image.asset(
              'assets/images/tavefinal.png',
              fit: BoxFit.fitWidth,
            ),
          ),
        ),
        Positioned.fill(
          child: Image.asset(
            'assets/images/recommand_final.png',
            color: Colors.white.withOpacity(0.95),
            fit: BoxFit.fitWidth,
          ),
        ),
        ],
      ),
    ),
            SizedBox(height: 50),
            // 텍스트 필드 및 드롭다운
            Center( // 텍스트 필드와 드롭다운을 중앙에 위치시킵니다.
              child: Container(
                width: totalWidth,
                child: Row(
                  children: <Widget>[
                    Expanded(
                      child: TextField(
                        controller: textEditingController,
                        decoration: InputDecoration(
                          labelText: '웹툰 제목 입력',
                          labelStyle: FontStyle2,
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(15.0),
                          ),
                        ),
                        onSubmitted: (value) {
                          _getWebtoonCharacters(textEditingController);
                        },
                      ),
                    ),
                    SizedBox(width: 40),
                    Expanded(
                      child: DropdownButtonFormField<String>(
                        hint: Text('웹툰 주연 선택'),
                        value: dropdownValue,
                        style: FontStyle2,
                        decoration: InputDecoration(
                          labelText: '웹툰 주연 선택',
                          labelStyle: FontStyle2,
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(15.0),
                          ),
                        ),
                        onChanged: (String? newValue) {
                          setState(() {
                            dropdownValue = newValue!;
                          });
                        },
                        items: dropdownOptions.map<DropdownMenuItem<String>>((String value) {
                          return DropdownMenuItem<String>(
                            value: value,
                            child: Text(value, style: FontStyle2),
                          );
                        }).toList(),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            // 결과 페이지로 이동하는 버튼
            SizedBox(height:40),
            Center(
              child: ElevatedButton(
                onPressed: () {
                  _navigateToResult(); // 이 부분을 수정했습니다.
                },
                child: Text('배우 보러 가기'),
                style: ElevatedButton.styleFrom(
                  primary: Color.fromRGBO(0, 204, 0, 0.5),
                  onPrimary: Color.fromRGBO(255, 255, 255, 1.0),
                  textStyle: FontStyle2,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
